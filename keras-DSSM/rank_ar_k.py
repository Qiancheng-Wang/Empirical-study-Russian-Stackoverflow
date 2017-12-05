from __future__ import print_function
import numpy as np
import csv, datetime, time, json
from zipfile import ZipFile
from os.path import expanduser, exists
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import text_to_word_sequence

from keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import Input, TimeDistributed, Dense, Lambda, concatenate, Dropout, BatchNormalization
from keras.layers.embeddings import Embedding
from keras.regularizers import l2
from keras.callbacks import Callback, ModelCheckpoint
from keras.utils.data_utils import get_file
from keras import backend as K
from sklearn.model_selection import train_test_split
import heapq
import operator
import pymysql.cursors

# Initialize global variables
KERAS_DATASETS_DIR = expanduser('/Users/wqc/Desktop/keras-quora-question-pairs-master/')

QUESTION_PAIRS_FILE = 'testing_query.json'
TAGS_FILE = 'alltags.json'
GLOVE_ZIP_FILE_URL = 'http://nlp.stanford.edu/data/glove.840B.300d.zip'
GLOVE_ZIP_FILE = 'glove.840B.300d.zip'
GLOVE_FILE = 'glove.840B.300d.txt'
Q1_TRAINING_DATA_FILE = 'q1_train.npy'
Q2_TRAINING_DATA_FILE = 'q2_train.npy'
LABEL_TRAINING_DATA_FILE = 'label_train.npy'
WORD_EMBEDDING_MATRIX_FILE = 'word_embedding_matrix.npy'
NB_WORDS_DATA_FILE = 'nb_words.json'
MAX_NB_WORDS = 220000
MAX_SEQUENCE_LENGTH = 25
EMBEDDING_DIM = 300
MODEL_WEIGHTS_FILE = 'stack_pairs_weights.h5'
VALIDATION_SPLIT = 0.1
TEST_SPLIT = 0.1
RNG_SEED = 13371447
NB_EPOCHS = 25
DROPOUT = 0.2
BATCH_SIZE = 32
OPTIMIZER = 'adam'


def create_model():
    if exists(Q1_TRAINING_DATA_FILE) and exists(Q2_TRAINING_DATA_FILE) and exists(LABEL_TRAINING_DATA_FILE) and exists(
            NB_WORDS_DATA_FILE) and exists(WORD_EMBEDDING_MATRIX_FILE):
        # Then load them
        q1_data = np.load(open(Q1_TRAINING_DATA_FILE, 'rb'))
        q2_data = np.load(open(Q2_TRAINING_DATA_FILE, 'rb'))
        labels = np.load(open(LABEL_TRAINING_DATA_FILE, 'rb'))
        word_embedding_matrix = np.load(open(WORD_EMBEDDING_MATRIX_FILE, 'rb'))
        with open(NB_WORDS_DATA_FILE, 'r') as f:
            nb_words = json.load(f)['nb_words']
    else:
        # Else download and extract questions pairs data
        # if not exists(KERAS_DATASETS_DIR + QUESTION_PAIRS_FILE):
        #   get_file(QUESTION_PAIRS_FILE, QUESTION_PAIRS_FILE_URL)

        print("Processing", QUESTION_PAIRS_FILE)

        question1 = []
        question2 = []
        is_duplicate = []
        with open(KERAS_DATASETS_DIR + QUESTION_PAIRS_FILE, encoding='utf-8') as jsondata:
            file = json.load(jsondata)
            flag = 0
            for row in file:
                if row['is_duplicate'] != 0 and row['is_duplicate'] != 1:
                    pass
                else:
                    question1.append(row['question1'])
                    question2.append(row['question2'])
                    is_duplicate.append(row['is_duplicate'])

        print('Question pairs: %d' % len(question1))

        # Build tokenized word index
        questions = question1 + question2
        tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
        tokenizer.fit_on_texts(questions)
        question1_word_sequences = tokenizer.texts_to_sequences(question1)
        question2_word_sequences = tokenizer.texts_to_sequences(question2)
        word_index = tokenizer.word_index

        print("Words in index: %d" % len(word_index))

        # Download and process GloVe embeddings
        '''if not exists(KERAS_DATASETS_DIR + GLOVE_ZIP_FILE):
            zipfile = ZipFile(get_file(GLOVE_ZIP_FILE, GLOVE_ZIP_FILE_URL))
            zipfile.extract(GLOVE_FILE, path=KERAS_DATASETS_DIR)
            '''
        print("Processing", GLOVE_FILE)

        embeddings_index = {}
        with open(KERAS_DATASETS_DIR + GLOVE_FILE, encoding='utf-8') as f:
            for line in f:
                values = line.split(' ')
                word = values[0]
                embedding = np.asarray(values[1:], dtype='float32')
                embeddings_index[word] = embedding

        print('Word embeddings: %d' % len(embeddings_index))

        # Prepare word embedding matrix
        nb_words = min(MAX_NB_WORDS, len(word_index))
        word_embedding_matrix = np.zeros((nb_words + 1, EMBEDDING_DIM))
        for word, i in word_index.items():
            if i > MAX_NB_WORDS:
                continue
            embedding_vector = embeddings_index.get(word)
            if embedding_vector is not None:
                word_embedding_matrix[i] = embedding_vector

        print('Null word embeddings: %d' % np.sum(np.sum(word_embedding_matrix, axis=1) == 0))

        # Prepare training data tensors
        q1_data = pad_sequences(question1_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
        q2_data = pad_sequences(question2_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
        labels = np.array(is_duplicate, dtype=int)
        print('Shape of question1 data tensor:', q1_data.shape)
        print('Shape of question2 data tensor:', q2_data.shape)
        print('Shape of label tensor:', labels.shape)

        # Persist training and configuration data to files
        np.save(open(Q1_TRAINING_DATA_FILE, 'wb'), q1_data)
        np.save(open(Q2_TRAINING_DATA_FILE, 'wb'), q2_data)
        np.save(open(LABEL_TRAINING_DATA_FILE, 'wb'), labels)
        np.save(open(WORD_EMBEDDING_MATRIX_FILE, 'wb'), word_embedding_matrix)
        with open(NB_WORDS_DATA_FILE, 'w') as f:
            json.dump({'nb_words': nb_words}, f)

    # Partition the dataset into train and test sets
    X = np.stack((q1_data, q2_data), axis=1)
    y = labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SPLIT, random_state=RNG_SEED)
    Q1_train = X_train[:, 0]
    Q2_train = X_train[:, 1]
    Q1_test = X_test[:, 0]
    Q2_test = X_test[:, 1]

    # Define the model
    question1 = Input(shape=(MAX_SEQUENCE_LENGTH,))
    question2 = Input(shape=(MAX_SEQUENCE_LENGTH,))

    q1 = Embedding(nb_words + 1,
                   EMBEDDING_DIM,
                   weights=[word_embedding_matrix],
                   input_length=MAX_SEQUENCE_LENGTH,
                   trainable=False)(question1)
    q1 = TimeDistributed(Dense(EMBEDDING_DIM, activation='relu'))(q1)
    q1 = Lambda(lambda x: K.max(x, axis=1), output_shape=(EMBEDDING_DIM,))(q1)

    q2 = Embedding(nb_words + 1,
                   EMBEDDING_DIM,
                   weights=[word_embedding_matrix],
                   input_length=MAX_SEQUENCE_LENGTH,
                   trainable=False)(question2)
    q2 = TimeDistributed(Dense(EMBEDDING_DIM, activation='relu'))(q2)
    q2 = Lambda(lambda x: K.max(x, axis=1), output_shape=(EMBEDDING_DIM,))(q2)

    merged = concatenate([q1, q2])
    merged = Dense(200, activation='relu')(merged)
    merged = Dropout(DROPOUT)(merged)
    merged = BatchNormalization()(merged)
    merged = Dense(200, activation='relu')(merged)
    merged = Dropout(DROPOUT)(merged)
    merged = BatchNormalization()(merged)
    merged = Dense(200, activation='relu')(merged)
    merged = Dropout(DROPOUT)(merged)
    merged = BatchNormalization()(merged)
    merged = Dense(200, activation='relu')(merged)
    merged = Dropout(DROPOUT)(merged)
    merged = BatchNormalization()(merged)

    is_duplicate = Dense(1, activation='sigmoid')(merged)

    model = Model(inputs=[question1, question2], outputs=is_duplicate)
    model.compile(loss='binary_crossentropy', optimizer=OPTIMIZER, metrics=['accuracy'])

    return model


def load_model(path):
    model = create_model()
    model.load_weights(path)
    return model

def generate_tags(string):
    new_string = string.replace('<','')
    new_string = new_string.replace('>',' ')
    str_list = new_string.split()
    return str_list


model = load_model('stack_pairs_weights.h5')

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '0472',
    'db': 'testdb',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,

}


connection = pymysql.connect(**config)

try:
    with connection.cursor() as cursor:


        all_query = []
        all_groud_truth = []
        all_tags = []
        with open('testing_query.json', encoding='utf-8') as jsondata:
            file = json.load(jsondata)
            for row in file:

                all_query.append(row['question1'])
                all_groud_truth.append(row['question2'])
                all_tags.append(row['tagname1'])

        precision1 = 0
        precision5 = 0
        precision10 = 0
        map_sum = 0
        for this in range(len(all_query)):

            if this % 50 == 0 :
                print("This is query %d" % this)
                if this != 0:
                    print(precision1/this,(precision5+precision1)/this,(precision10+precision5+precision1)/this)
                    print(map_sum/this)
            tags = generate_tags(all_tags[this])

            query = all_query[this]
            groud_truth = all_groud_truth[this]
            if len(tags) == 2:
                sql1 = "select title from mainsite_questions where tags like \'%" + tags[0] + '%\' and tags like \'%' + tags[1] +'%\' limit 100;'
            elif len(tags)== 3:
                sql1 = "select title from mainsite_questions where tags like \'%" + tags[0] + '%\' and tags like \'%' + tags[1] +'%\' and tags like \'%' +tags[2] +'%\' limit 100;'
            elif len(tags) == 4:
                sql1 = "select title from mainsite_questions where tags like \'%" + tags[0] + '%\' and tags like \'%' + tags[1] +'%\' and tags like \'%' +tags[2]  + '%\' and tags like \'%' + tags[3] +'%\' limit 100;'
            elif len(tags) >= 5:
                sql1 = "select title from mainsite_questions where tags like \'%" + tags[0] + '%\' and tags like \'%' + tags[1] +'%\' and tags like \'%' +tags[2]  + '%\' and tags like \'%' + tags[3]  + '%\' and tags like \'%' + tags[4] +'%\' limit 100;'
            

            #print(sql1)
            cursor.execute(sql1)
            result1 = cursor.fetchall()
            #print (len(result1))

            question1 = []
            for leng in range(len(result1)+1):
                question1.append(query)

            question2 = []
            question2.append(groud_truth)
            for num in range(len(result1)):
                this_question = result1[num]['title']
                question2.append(this_question)
            #print(len(question2))

            questions = question1 + question2
            #print(questions)
            tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
            tokenizer.fit_on_texts(questions)
            question1_word_sequences = tokenizer.texts_to_sequences(question1)
            question2_word_sequences = tokenizer.texts_to_sequences(question2)

            q1_data = pad_sequences(question1_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
            q2_data = pad_sequences(question2_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)

            X = np.stack((q1_data, q2_data), axis=1)
            Q1_test = X[:, 0]
            Q2_test = X[:, 1]
            results = model.predict([Q1_test, Q2_test], batch_size=32, verbose=0)
            #for i in range(3):
            #    print( results[i], question2[i])
            g_t = results[0][0]
            pa1 = heapq.nlargest(1, results)
            pa5 = heapq.nlargest(5, results)
            pa10 = heapq.nlargest(10, results)
            min1 = min(pa1)[0]
            min5 = min(pa5)[0]
            min10 = min(pa10)[0]
            this_result = []
            for i in range(len(result1)+1):
                this_result.append(results[i][0])

            this_result.sort(reverse = True)
            #print(this_result)
            #print(g_t)
            #if this_result.index(g_t) == 1:
                #print(pa5)
            p=float(this_result.index(g_t)+1)

            #print (p)
            map_sum += 1/p
            #print(g_t,min1,min5,min10)
            if g_t >= min1:
                precision1 += 1
            elif g_t >= min5:
                precision5 += 1
            elif g_t >= min10:
                precision10 += 1
            question1 = []
            question2 = []
            result1 = []
            results = []
            questions = []
            q1_data = []
            q2_data = []
        print(all_query,precision1,precision5,precision10)
        print("Precision @ 1: %f" %(precision1/len(all_query)))
        print("Precision @ 5: %f" %(precision5/len(all_query)))
        print("Precision @ 10: %f" %(precision10/len(all_query)))

finally:
    connection.close()






