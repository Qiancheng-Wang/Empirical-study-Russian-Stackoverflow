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




        sql1 = 'select accountId from postanalysis2 ;'
        cursor.execute(sql1)
        result1 = cursor.fetchall()

        dateDataUpdate = datetime.datetime.strptime('2017-3-15 00:00:00', '%Y-%m-%d %H:%M:%S')


        russian_post_active = 0
        russian_post_equal = 0
        russian_post_inactive = 0

        stack_post_active = 0
        stack_post_equal = 0
        stack_post_inactive = 0

        both_active = 0
        both_equal = 0
        bothe_inactive = 0

        total_post_active = 0
        total_post_equal = 0
        total_post_inactive = 0

        flag1 = 0
        while flag1 < len(result1):
            print(flag1)

            thisaccoutidstr = result1[flag1]
            thisaccoutid = thisaccoutidstr['accountId']

            sql2 = 'select afterMigrationRussianPost,beforeMigrationStackPost,afterMigrationStackpost,stackcreationdate,russiancreationdate from postanalysis2 where accountId = %s;' % thisaccoutid
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


            afterMigrationRussianPost = float(result2['afterMigrationRussianPost'])
            beforeMigrationStackPost = float(result2['beforeMigrationStackPost'])
            afterMigrationStackpost = float(result2['afterMigrationStackpost'])

            comparenumber_post = beforeMigrationStackPost*proportion

            print(proportion, comparenumber_post,"\n",
            afterMigrationRussianPost,afterMigrationStackpost,afterMigrationRussianPost + afterMigrationStackpost)

            if afterMigrationRussianPost >=  1.1* comparenumber_post :
                #print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                russian_post_active += 1

            elif afterMigrationRussianPost >= 0.9 * comparenumber_post:
                russian_post_equal += 1
            else:
                #print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                russian_post_inactive += 1
            ####################################
            ####################################
            ####################################

            if afterMigrationStackpost >=  1.1* comparenumber_post :
                #print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                stack_post_active += 1

            elif afterMigrationStackpost >= 0.9 * comparenumber_post:
                stack_post_equal += 1
            else:
                #print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                stack_post_inactive += 1

            ####################################
            ####################################
            ####################################


            if (afterMigrationRussianPost + afterMigrationStackpost ) >=  1.1* comparenumber_post :
                #print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                total_post_active += 1
                if afterMigrationStackpost >= 1.1 * comparenumber_post:
                    # print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                    both_active += 1
            elif (afterMigrationRussianPost + afterMigrationStackpost ) >= 0.9 * comparenumber_post:
                total_post_equal += 1
                if afterMigrationStackpost >= 0.9 * comparenumber_post:
                    both_equal += 1
            else:
                #print(afterCreatedRussianAccount_Russian_Answer + afterCreatedRussianAccount_Russian_Question)
                total_post_inactive += 1
                if afterMigrationStackpost < 0.9 * comparenumber_post:
                    bothe_inactive += 1

            flag1 += 1

            connection.commit()

        print(" russian_post_active is ",russian_post_active ,"\n",
              "russian_post_equal is", russian_post_equal,"\n"
              "russian_post_inactive is ",russian_post_inactive ,"\n")

        print(" stack_post_active is ", stack_post_active, "\n",
              "stack_post_equal is", stack_post_equal, "\n"
                "stack_post_inactive is ", stack_post_inactive, "\n")

        print(" total_post_active is ", total_post_active, "\n",
              "total_post_equal is", total_post_equal,"\n"
              "total_post_inactive is ", total_post_inactive, "\n")

        print(" both_active is ", both_active, "\n",
              "both_equal is", both_equal, "\n"
                "both_inactive is ", bothe_inactive, "\n")


finally:
    connection.close()



