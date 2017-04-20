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


        flag = 0
        while 1:

            flag += 1
            print(flag)
            if flag == 8361:
                break


            sql1 = 'select CreationDate from RussianCoreUserInfo where rownum = %s ;' % flag
            cursor.execute(sql1)
            result1 = cursor.fetchone()
            rucreation_date = str(result1['CreationDate'])[0:10] + ' ' + str(result1['CreationDate'])[11:19]
            rucreation_date = datetime.datetime.strptime(rucreation_date, '%Y-%m-%d %H:%M:%S')

            sql2 = 'select CreationDate from StackCoreUserInfo where rownum = %s ;' % flag
            cursor.execute(sql2)
            result2 = cursor.fetchone()
            creation_date = str(result2['CreationDate'])[0:10] + ' ' + str(result2['CreationDate'])[11:19]
            creation_date = datetime.datetime.strptime(creation_date, '%Y-%m-%d %H:%M:%S')

            if creation_date < rucreation_date:
                #print("该用户先注册stackoverflow")
                #print("========================")
                sql3 = 'insert into stacktorussiancoreuser select * from StackCoreUserInfo where rownum = %s ;' % flag
                cursor.execute(sql3)
            else:
                #print("该用户先注册ru.stackoverflow")
                #print("========================")
                sql4 = 'insert into russiantostackcoreuser select * from RussianCoreUserInfo where rownum = %s ;' % flag
                cursor.execute(sql4)


    connection.commit()

finally:
    connection.close()



