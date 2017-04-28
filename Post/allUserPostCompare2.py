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




        sql1 = 'select accountId from russiancoreuserfrommainsite ;'
        cursor.execute(sql1)
        result1 = cursor.fetchall()


        flag1 = 0
        while flag1 < len(result1):
            print(flag1)
            afterCreatedRussianAccount = 0
            beforeCreatedRussianAccount = 0

            afterCreatedRussianAccount_Russian = 0

            thisaccoutidstr = result1[flag1]
            thisaccoutid = thisaccoutidstr['accountId']

            sql2 = 'select id,creationdate from finalcompare where accountId = %s and origin = \'Stackoverflow\';' % thisaccoutid
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            result2 = result2[0]
            thisstackid = result2['id']
            userstackcreationdate = str(result2['creationdate'])[0:10] + ' ' + str(
                result2['creationdate'])[11:19]
            userstackcreationdate = datetime.datetime.strptime(userstackcreationdate, '%Y-%m-%d %H:%M:%S')

            sql3 = 'select id,creationdate from finalcompare where accountId = %s and origin = \'RussianStackoverflow\';' % thisaccoutid
            cursor.execute(sql3)
            result3 = cursor.fetchall()
            result3 = result3[0]
            thisrussianid = result3['id']
            userrussiancreationdate = str(result3['creationdate'])[0:10] + ' ' + str(
                result3['creationdate'])[11:19]
            userrussiancreationdate = datetime.datetime.strptime(userrussiancreationdate, '%Y-%m-%d %H:%M:%S')

            gaptime = str( userrussiancreationdate - userstackcreationdate)

            dateDataUpdate = datetime.datetime.strptime('2017-3-15 00:00:00', '%Y-%m-%d %H:%M:%S')
            timeusingRussianstackaccount = dateDataUpdate - userrussiancreationdate
            timeusingstackaccount = dateDataUpdate - userstackcreationdate
            print(timeusingRussianstackaccount,timeusingstackaccount)

            flag2 = 0
            sql4 = 'select CreationDate from stackcorepost where owneruserid = %s ;' % thisstackid
            cursor.execute(sql4)
            allstackanswer = cursor.fetchall()

            while flag2 < len(allstackanswer) :

                currentcreationdate = allstackanswer[flag2]
                creationdate = str(currentcreationdate['CreationDate'])[0:10] + ' ' + str(
                    currentcreationdate['CreationDate'])[11:19]
                creationdate = datetime.datetime.strptime(creationdate, '%Y-%m-%d %H:%M:%S')
                # print("This answer creationdate is", creationdate)


                if creationdate > userrussiancreationdate:
                    afterCreatedRussianAccount += 1
                else:
                    beforeCreatedRussianAccount += 1
                flag2 += 1



            sql6 = 'select count(*) from russiancorepost where owneruserid = %s ;' % thisrussianid
            cursor.execute(sql6)
            allrussainpost = cursor.fetchall()
            allrussainpost = allrussainpost[0]
            allrussainpost = allrussainpost['count(*)']

            flag1 += 1
            sql_final = 'insert into postanalysis2 values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\', \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');' % (
            thisaccoutid, thisstackid, userstackcreationdate, thisrussianid, userrussiancreationdate, gaptime,

            allrussainpost, beforeCreatedRussianAccount,afterCreatedRussianAccount, timeusingRussianstackaccount,timeusingstackaccount)
            cursor.execute(sql_final)
            connection.commit()

finally:
    connection.close()



