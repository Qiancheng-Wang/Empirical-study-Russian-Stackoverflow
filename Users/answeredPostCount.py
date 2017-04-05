# mysqldb doesn't support python3.X, so I use the PyMySQL.
# user the datetime library can easily compare strings of date.



import pymysql.cursors
import datetime
import time


config = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'wqc050868',
    'db':'test',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
    }

# Connect to the database
connection = pymysql.connect(**config)
try:
    with connection.cursor() as cursor:

        flag = 51
        while flag < 71500 :
            flag += 2
            print(flag)


            sql1 = 'select id from FinalCompare where rownum = %s' % flag
            cursor.execute(sql1)
            result1 = cursor.fetchone()
            result1 = result1['id']

            #print(result1)

            sql2 = 'select count(*) from RussianPost where OwnerUserId = %s' % result1
            cursor.execute(sql2)
            result2 = cursor.fetchone()
            result2 = result2['count(*)']
            #print(result2)

            sql3 = 'update FinalCompare set PostCount = %s where id = %s' % (result2, result1)
            cursor.execute(sql3)
            #print (sql3)


    connection.commit()

finally:
    connection.close()




