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

        rustack_num = -1
        stack_num = 0
        rustack_count = 0
        stack_count = 0

        while rustack_num < 62878 :

            rustack_num += 2
            stack_num += 2
            #print(rustack_num, stack_num)


            sql1 = 'select CreationDate from FinalCompare where rownum = %s' % rustack_num
            cursor.execute(sql1)
            result1 = cursor.fetchone()
            rucreation_date = str(result1['CreationDate'])[0:10] + ' ' +str(result1['CreationDate'])[11:19]
            rucreation_date = datetime.datetime.strptime(rucreation_date, '%Y-%m-%d %H:%M:%S')
            #print("ru date  ", rustack_num , rucreation_date)
            sql2 = 'select CreationDate from FinalCompare where rownum = %s' % stack_num
            cursor.execute(sql2)
            result2 = cursor.fetchone()
            creation_date = str(result2['CreationDate'])[0:10] + ' ' +str(result2['CreationDate'])[11:19]
            creation_date = datetime.datetime.strptime(creation_date, '%Y-%m-%d %H:%M:%S')
            #print("stack date  ",stack_num , creation_date)

            if creation_date < rucreation_date:
                #print("该用户先注册stackoverflow")
                #print("========================")
                stack_count += 1
            else:
                #print("该用户先注册ru.stackoverflow")
                #print("========================")
                rustack_count += 1
            print(rustack_num)
        print( "先注册stackoverflow的人数为 " , stack_count)
        print( "先注册ru.stackoverflow的人数为 ", rustack_count)
    connection.commit()

finally:
    connection.close()




