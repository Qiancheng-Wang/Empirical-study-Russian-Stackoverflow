import pymysql.cursors
import datetime
import time

config = {
        'host' : 'localhost',
        'port' : 3306,
        'user' : 'root',
        'password' : '0472',
        'db': 'testdb',
        'charset' : 'utf8mb4',
        'cursorclass' : pymysql.cursors.DictCursor,

    }


connection = pymysql.connect(**config)



try :
    with connection.cursor() as cursor :




        sql1 = 'select accountId from stacktorussiancoreuser ;'
        cursor.execute(sql1)
        result1 = cursor.fetchall()

        dateDataUpdate = datetime.datetime.strptime('2017-3-15 00:00:00', '%Y-%m-%d %H:%M:%S')


        russian_post_active = 0
        russian_post_inactive = 0
        russian_answer_active = 0
        russian_answer_inactive = 0
        russian_question_active = 0
        russian_question_inactive = 0

        stack_post_active = 0
        stack_post_inactive = 0
        stack_answer_active = 0
        stack_answer_inactive = 0
        stack_question_active = 0
        stack_question_inactive = 0

        total_post_active = 0
        total_post_inactive = 0
        total_answer_active = 0
        total_answer_inactive = 0
        total_question_active = 0
        total_question_inactive = 0
        flag1 = 0
        while flag1 < len(result1):
            print(flag1)

            thisaccoutidstr = result1[flag1]
            thisaccoutid = thisaccoutidstr['accountId']

            sql2 = 'select afterMigrationRussianAnswer, afterMigrationRussianquestion,beforeMigrationStackAnswer,beforeMigrationStackQuestion,afterMigrationStackAnswer,afterMigrationStackQuestion,stackcreationdate,russiancreationdate from postanalysis2 where accountId = %s;' % thisaccoutid
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            result2 = result2[0]
            userstackcreationdate = str(result2['stackcreationdate'])[0:10] + ' ' + str(
                result2['stackcreationdate'])[11:19]
            userstackcreationdate = datetime.datetime.strptime(userstackcreationdate, '%Y-%m-%d %H:%M:%S')
            userrussiancreationdate = str(result2['russiancreationdate'])[0:10] + ' ' + str(
                result2['russiancreationdate'])[11:19]
            userrussiancreationdate = datetime.datetime.strptime(userrussiancreationdate, '%Y-%m-%d %H:%M:%S')
            gaptime = userrussiancreationdate - userstackcreationdate
            usingrussiantime = dateDataUpdate - userrussiancreationdate
            proportion = usingrussiantime / gaptime
            print(proportion)

            afterCreatedRussianAccount_Answer = float(result2['afterMigrationStackAnswer'])
            beforeCreatedRussianAccount_Answer = float(result2['beforeMigrationStackAnswer'])
            afterCreatedRussianAccount_Question = float(result2['afterMigrationStackQuestion'])
            beforeCreatedRussianAccount_Question = float(result2['beforeMigrationStackQuestion'])
            afterCreatedRussianAccount_Russian_Answer = float(result2['afterMigrationRussianAnswer'])
            afterCreatedRussianAccount_Russian_Question = float(result2['afterMigrationRussianquestion'])

            '''print(afterCreatedRussianAccount_Answer, beforeCreatedRussianAccount_Answer ,
                  afterCreatedRussianAccount_Question ,beforeCreatedRussianAccount_Question ,
                  afterCreatedRussianAccount_Russian_Answer , afterCreatedRussianAccount_Russian_Question)
            '''
            comparenumber_answer = beforeCreatedRussianAccount_Answer*proportion
            comparenumber_question = beforeCreatedRussianAccount_Question*proportion
            comparenumber_post = (beforeCreatedRussianAccount_Answer + beforeCreatedRussianAccount_Question)*proportion
            print("comparenumber_answer,comparenumber_question,comparenumber_post",comparenumber_answer,comparenumber_question,comparenumber_post)

            if comparenumber_answer > afterCreatedRussianAccount_Russian_Answer:
                #print(afterCreatedRussianAccount_Russian_Answer)
                russian_answer_inactive += 1
            else:
                #print(afterCreatedRussianAccount_Russian_Answer)
                russian_answer_active += 1

            if comparenumber_question > afterCreatedRussianAccount_Russian_Question:
                #print(afterCreatedRussianAccount_Russian_Question)
                russian_question_inactive += 1
            else:
                #print(afterCreatedRussianAccount_Russian_Question)
                russian_question_active += 1

            if comparenumber_post > (afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question):
                #print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                russian_post_inactive += 1
            else:
                #print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                russian_post_active += 1
            ####################################
            ####################################
            ####################################

            if comparenumber_answer > afterCreatedRussianAccount_Answer :
                stack_answer_inactive += 1
            else:
                stack_answer_active += 1

            if comparenumber_question >  afterCreatedRussianAccount_Question:
                stack_question_inactive += 1
            else:
                stack_question_active += 1

            if comparenumber_post >(afterCreatedRussianAccount_Answer + afterCreatedRussianAccount_Question):
                stack_post_inactive += 1
            else:
                stack_post_active += 1

            ####################################
            ####################################
            ####################################

            if comparenumber_answer > (afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Answer):
                total_answer_inactive += 1
            else:
                total_answer_active += 1

            if comparenumber_question > (afterCreatedRussianAccount_Russian_Question + afterCreatedRussianAccount_Question):
                total_question_inactive += 1
            else:
                total_question_active += 1

            if comparenumber_post > (afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question + afterCreatedRussianAccount_Answer + afterCreatedRussianAccount_Question):
                total_post_inactive += 1
            else:
                total_post_active += 1

            flag1 += 1

            connection.commit()

        print(" russian_post_active is ",russian_post_active ,"\n",
              "russian_post_inactive is ",russian_post_inactive ,"\n",
              "russian_answer_active is ",russian_answer_active ,"\n",
              "russian_answer_inactive is ",russian_answer_inactive ,"\n",
              "russian_question_active is ",russian_question_active ,"\n",
              "russian_question_inactive is ",russian_question_inactive ,"\n")
        print(" stack_post_active is ", stack_post_active, "\n",
              "stack_post_inactive is ", stack_post_inactive, "\n",
              "stack_answer_active is ", stack_answer_active, "\n",
              "stack_answer_inactive is ", stack_answer_inactive, "\n",
              "stack_question_active is ", stack_question_active, "\n",
              "stack_question_inactive is ", stack_question_inactive, "\n")
        print(" total_post_active is ", total_post_active, "\n",
              "total_post_inactive is ", total_post_inactive, "\n",
              "total_answer_active is ", total_answer_active, "\n",
              "total_answer_inactive is ", total_answer_inactive, "\n",
              "total_question_active is ", total_question_active, "\n",
              "total_question_inactive is ", total_question_inactive, "\n")

finally:
    connection.close()



