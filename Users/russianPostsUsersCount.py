
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

        postcount_0 = 0
        postcount_5 = 0
        postcount_20 = 0
        postcount_50 = 0
        postcount_100 = 0
        postcount_250 = 0
        postcount_500 = 0
        flag = -1
        while flag < 71500 :
            flag += 2
            print(flag)

            sql1 = 'select postcount from FinalCompare where rownum = %s' % flag
            cursor.execute(sql1)
            result1 = cursor.fetchone()
            result1 = result1['postcount']
            result1 = float(result1)
            print(result1)
            if result1 > 500:
                postcount_500 +=1
            elif result1 > 250:
                postcount_250 += 1
            elif result1 > 100:
                postcount_100 += 1
            elif result1 > 50:
                postcount_50 += 1
            elif result1 > 20:
                postcount_20 += 1
            elif result1 > 5:
                postcount_5 += 1
            else:
                postcount_0 += 1

        print("postcount_0 ,postcount_5 ,postcount_20 , postcount_50 ,postcount_100 ,postcount_250 ,postcount_500 \n",
        postcount_0 ,postcount_5 ,postcount_20 , postcount_50 ,postcount_100 ,postcount_250 ,postcount_500 )



    connection.commit()

finally:
    connection.close()




