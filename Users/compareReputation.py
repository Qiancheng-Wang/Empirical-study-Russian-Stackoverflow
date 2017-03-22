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
        over100_rustack_count = 0
        over100_stack_count = 0
        over100_equal_count = 0
        over500_rustack_count = 0
        over500_stack_count = 0
        over500_equal_count = 0
        over1000_rustack_count = 0
        over1000_stack_count = 0
        over1000_equal_count = 0
        inactive_rustack_count = 0
        inactive_stack_count = 0
        inactive_equal_count = 0

        while rustack_num < 62878:
            rustack_num += 2
            stack_num += 2
            print(rustack_num)
            sql1 = 'select Reputation from FinalCompare where rownum = %s' % rustack_num
            cursor.execute(sql1)
            result1 = cursor.fetchone()
            result1 = float(result1['Reputation'])
            #print(result1)
            sql2 = 'select Reputation from FinalCompare where rownum = %s' % stack_num
            cursor.execute(sql2)
            result2 = cursor.fetchone()
            result2 = float(result2['Reputation'])
            #print(result2)

            if result1 > result2:
                #print("ru reputation is greater than stack's")
                if result1 > 1000:
                    over1000_rustack_count += 1
                elif result1 > 500 and result1 <=1000:
                    over500_rustack_count += 1
                elif result1 > 100 and result1 <= 500:
                    over100_rustack_count += 1
                else:
                    inactive_rustack_count += 1
            elif result1 == result2:
                #print("ru reputation equals with stack's")
                if result1 > 1000 :
                    over1000_equal_count += 1
                elif result1 > 500 and result1 <=1000:
                    over500_equal_count += 1
                elif result1 > 100 and result1 <= 500:
                    over100_equal_count += 1
                else:
                    inactive_equal_count += 1
            else:
                #print("stack reputation is greater than ru's")
                if result2 > 1000:
                    over1000_stack_count += 1
                elif result2 > 500 and result1 <= 1000:
                    over500_stack_count += 1
                elif result2 > 100 and result1 <= 500:
                    over100_stack_count += 1
                else:
                    inactive_stack_count += 1

        print("rustack_count ", inactive_rustack_count,over100_rustack_count,over500_rustack_count,over1000_rustack_count)
        print ("equal_count", inactive_equal_count, over100_equal_count,over500_equal_count,over1000_equal_count)
        print("stack_count ", inactive_stack_count,over100_stack_count,over500_stack_count,over1000_stack_count)

    connection.commit()

finally:
    connection.close()




