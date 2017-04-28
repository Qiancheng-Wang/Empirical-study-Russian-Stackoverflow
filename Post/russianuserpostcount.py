import pymysql.cursors
import datetime
import time

import plotly
plotly.tools.set_credentials_file(username='wqc', api_key='XEJwAY8cBDGyyuyNrjSt')
import plotly.plotly as py
import plotly.graph_objs as go

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


        post0 = 0
        post1 = 0
        post2 = 0
        post3 = 0
        post4 = 0
        post5 = 0
        post6 = 0
        post7 = 0
        post8 = 0
        post9 = 0
        post10 = 0
        post11 = 0
        post12 = 0
        post13 = 0
        post14 = 0
        post15 = 0
        post16 = 0
        post17 = 0
        post18 = 0
        post19 = 0
        post20 = 0
        post_over_20 = 0

        flag1 = 0
        sql1 = 'select postcount,accountid from russianuserpostcount;'
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        while flag1 < len(result1):
            print(flag1)

            this = result1[flag1]
            thispostcount = this['postcount']
            print (thispostcount)
            if thispostcount == '0':
                post0 += 1
            elif thispostcount == '1':
                post1 += 1
            elif thispostcount == '2':
                post2 += 1
            elif thispostcount == '3':
                post3 += 1
            elif thispostcount == '4':
                post4 += 1
            elif thispostcount == '5':
                post5 += 1
            elif thispostcount == '6':
                post6 += 1
            elif thispostcount == '7':
                post7 += 1
            elif thispostcount == '8':
                post8 += 1
            elif thispostcount == '9':
                post9 += 1
            elif thispostcount == '10':
                post10 += 1
            elif thispostcount == '11':
                post11 += 1
            elif thispostcount == '12':
                post12 += 1
            elif thispostcount == '13':
                post13 += 1
            elif thispostcount == '14':
                post14 += 1
            elif thispostcount == '15':
                post15 += 1
            elif thispostcount == '16':
                post16 += 1
            elif thispostcount == '17':
                post17 += 1
            elif thispostcount == '18':
                post18 += 1
            elif thispostcount == '19':
                post19 += 1
            elif thispostcount == '20':
                post20 += 1
            else:
                post_over_20 += 1

            flag1 += 1

            connection.commit()
        print("post0, post1 ,post2 ,post3 ,post4 ,post5 ,post6 ,post7 ,post8 ,post9 ,post10 ,post11 "
              ",post12 ,post13 ,post14,post15 ,post16, post12 ,post13 ,post14,post15 ,post16, post_over_20 ",
              post0,
            post1 ,
            post2 ,
            post3 ,
            post4 ,
            post5 ,
            post6 ,
            post7 ,
            post8 ,
            post9 ,
            post10 ,
            post11 ,
            post12 ,
              post13,
              post14,
              post15,
              post16,
              post17,
              post18,
              post19,
              post20,
            post_over_20 )

finally:
    connection.close()



