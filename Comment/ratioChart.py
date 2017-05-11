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
            #print(flag1)

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


            afterMigrationRussianPost = float(result2['afterMigrationRussianPost'])
            beforeMigrationStackPost = float(result2['beforeMigrationStackPost'])
            afterMigrationStackpost = float(result2['afterMigrationStackpost'])
            ratio = gaptime/usingrussiantime

            if beforeMigrationStackPost ==0:
                proportion = 1200
            else:
                proportion = (afterMigrationRussianPost/beforeMigrationStackPost)*ratio
            print(proportion)
            flag1 += 1
            sqlfinal = 'insert into russianactivityratio values(\'%s\',\'%s\');' % (thisaccoutid, proportion)
            cursor.execute(sqlfinal)
            connection.commit()



finally:
    connection.close()



