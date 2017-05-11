# mysqldb doesn't support python3.X, so I use the PyMySQL.
# user the datetime library can easily compare strings of date.

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


try:
    with connection.cursor() as cursor:


        sql1 = 'select id,accountId from test ;'
        cursor.execute(sql1)
        result1 = cursor.fetchall()

        flag1 = 0
        while flag1 < len(result1):
            print(flag1)

            thisaccoutidstr = result1[flag1]
            thisaccoutid = thisaccoutidstr['accountId']
            thisid = thisaccoutidstr['id']
            #print(thisaccoutid,thisid)

            sql2 = 'select count(*) from stackcoreComment where UserId = %s' % thisid
            cursor.execute(sql2)
            result2 = cursor.fetchone()
            result2 = result2['count(*)']
            #print(result2)

            sqlfinal = 'insert into stackcommentcount values(\'%s\',\'%s\',\'%s\');' %(thisaccoutid,thisid,result2)
            cursor.execute(sqlfinal)

            flag1+=1
            connection.commit()

finally:
    connection.close()




