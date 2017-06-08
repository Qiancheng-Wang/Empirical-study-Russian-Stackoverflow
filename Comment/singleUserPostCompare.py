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

        month2010_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2011_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2012_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2013_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2014_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2015_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2016_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2017_count = {'January': 0, 'February': 0, 'March': 0}

        date17_1 = datetime.datetime.strptime('2017-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date17_2 = datetime.datetime.strptime('2017-2-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date17_3 = datetime.datetime.strptime('2017-3-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_1 = datetime.datetime.strptime('2016-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_2 = datetime.datetime.strptime('2016-2-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_3 = datetime.datetime.strptime('2016-3-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_4 = datetime.datetime.strptime('2016-4-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_5 = datetime.datetime.strptime('2016-5-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_6 = datetime.datetime.strptime('2016-6-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_7 = datetime.datetime.strptime('2016-7-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_8 = datetime.datetime.strptime('2016-8-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_9 = datetime.datetime.strptime('2016-9-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_10 = datetime.datetime.strptime('2016-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_11 = datetime.datetime.strptime('2016-11-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date16_12 = datetime.datetime.strptime('2016-12-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_1 = datetime.datetime.strptime('2015-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_2 = datetime.datetime.strptime('2015-2-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_3 = datetime.datetime.strptime('2015-3-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_4 = datetime.datetime.strptime('2015-4-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_5 = datetime.datetime.strptime('2015-5-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_6 = datetime.datetime.strptime('2015-6-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_7 = datetime.datetime.strptime('2015-7-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_8 = datetime.datetime.strptime('2015-8-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_9 = datetime.datetime.strptime('2015-9-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_10 = datetime.datetime.strptime('2015-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_11 = datetime.datetime.strptime('2015-11-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date15_12 = datetime.datetime.strptime('2015-12-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_1 = datetime.datetime.strptime('2014-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_2 = datetime.datetime.strptime('2014-2-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_3 = datetime.datetime.strptime('2014-3-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_4 = datetime.datetime.strptime('2014-4-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_5 = datetime.datetime.strptime('2014-5-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_6 = datetime.datetime.strptime('2014-6-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_7 = datetime.datetime.strptime('2014-7-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_8 = datetime.datetime.strptime('2014-8-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_9 = datetime.datetime.strptime('2014-9-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_10 = datetime.datetime.strptime('2014-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_11 = datetime.datetime.strptime('2014-11-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date14_12 = datetime.datetime.strptime('2014-12-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_1 = datetime.datetime.strptime('2013-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_2 = datetime.datetime.strptime('2013-2-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_3 = datetime.datetime.strptime('2013-3-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_4 = datetime.datetime.strptime('2013-4-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_5 = datetime.datetime.strptime('2013-5-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_6 = datetime.datetime.strptime('2013-6-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_7 = datetime.datetime.strptime('2013-7-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_8 = datetime.datetime.strptime('2013-8-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_9 = datetime.datetime.strptime('2013-9-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_10 = datetime.datetime.strptime('2013-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_11 = datetime.datetime.strptime('2013-11-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date13_12 = datetime.datetime.strptime('2013-12-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_1 = datetime.datetime.strptime('2012-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_2 = datetime.datetime.strptime('2012-2-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_3 = datetime.datetime.strptime('2012-3-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_4 = datetime.datetime.strptime('2012-4-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_5 = datetime.datetime.strptime('2012-5-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_6 = datetime.datetime.strptime('2012-6-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_7 = datetime.datetime.strptime('2012-7-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_8 = datetime.datetime.strptime('2012-8-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_9 = datetime.datetime.strptime('2012-9-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_10 = datetime.datetime.strptime('2012-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_11 = datetime.datetime.strptime('2012-11-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date12_12 = datetime.datetime.strptime('2012-12-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_1 = datetime.datetime.strptime('2011-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_2 = datetime.datetime.strptime('2011-2-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_3 = datetime.datetime.strptime('2011-3-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_4 = datetime.datetime.strptime('2011-4-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_5 = datetime.datetime.strptime('2011-5-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_6 = datetime.datetime.strptime('2011-6-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_7 = datetime.datetime.strptime('2011-7-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_8 = datetime.datetime.strptime('2011-8-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_9 = datetime.datetime.strptime('2011-9-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_10 = datetime.datetime.strptime('2011-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_11 = datetime.datetime.strptime('2011-11-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date11_12 = datetime.datetime.strptime('2011-12-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_1 = datetime.datetime.strptime('2010-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_2 = datetime.datetime.strptime('2010-2-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_3 = datetime.datetime.strptime('2010-3-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_4 = datetime.datetime.strptime('2010-4-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_5 = datetime.datetime.strptime('2010-5-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_6 = datetime.datetime.strptime('2010-6-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_7 = datetime.datetime.strptime('2010-7-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_8 = datetime.datetime.strptime('2010-8-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_9 = datetime.datetime.strptime('2010-9-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_10 = datetime.datetime.strptime('2010-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_11 = datetime.datetime.strptime('2010-11-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        date10_12 = datetime.datetime.strptime('2010-12-1 00:00:00', '%Y-%m-%d %H:%M:%S')

        beforeCreatedRussianAccount = 0
        afterCreatedRussianAccount = 0

        flag = 1
        sql1 = 'select CreationDate from Russiancorepost where owneruserid = 23044  ;'
        cursor.execute(sql1)
        result1 = cursor.fetchall()

        sql2 = 'select creationdate from russianuserinfo where Id = 23044  ;'
        cursor.execute(sql2)
        result3 = cursor.fetchone()
        print(result3)
        usercreationdate = str(result3['creationdate'])[0:10] + ' ' + str(result3['creationdate'])[11:19]
        usercreationdate = datetime.datetime.strptime(usercreationdate, '%Y-%m-%d %H:%M:%S')

        while flag < len(result1):
            print(flag)
            result2 = result1[flag]
            creationdate = str(result2['CreationDate'])[0:10] + ' ' + str(result2['CreationDate'])[11:19]
            creationdate = datetime.datetime.strptime(creationdate, '%Y-%m-%d %H:%M:%S')
            print(creationdate)

            if creationdate > usercreationdate:
                afterCreatedRussianAccount += 1
            else:
                beforeCreatedRussianAccount += 1


            if creationdate > date17_3 :

                month2017_count['March'] += 1

            elif creationdate > date17_2 :

                month2017_count['February'] += 1

            elif creationdate > date17_1:

                month2017_count['January'] += 1





            elif creationdate > date16_12 :

                month2016_count['December'] += 1

            elif creationdate > date16_11 :

                month2016_count['November'] += 1

            elif creationdate > date16_10:

                month2016_count['October'] += 1

            elif creationdate > date16_9:

                month2016_count['September'] += 1

            elif creationdate > date16_8:

                month2016_count['August'] += 1

            elif creationdate > date16_7:

                month2016_count['July'] += 1

            elif creationdate > date16_6:

                month2016_count['June'] += 1

            elif creationdate > date16_5:

                month2016_count['May'] += 1

            elif creationdate > date16_4:

                month2016_count['April'] += 1

            elif creationdate > date16_3 :

                month2016_count['March'] += 1

            elif creationdate > date16_2 :

                month2016_count['February'] += 1

            elif creationdate > date16_1:

                month2016_count['January'] += 1





            elif creationdate > date15_12 :

                month2015_count['December'] += 1

            elif creationdate > date15_11 :

                month2015_count['November'] += 1

            elif creationdate > date15_10:

                month2015_count['October'] += 1

            elif creationdate > date15_9:

                month2015_count['September'] += 1

            elif creationdate > date15_8:

                month2015_count['August'] += 1

            elif creationdate > date15_7:

                month2015_count['July'] += 1

            elif creationdate > date15_6:

                month2015_count['June'] += 1

            elif creationdate > date15_5:

                month2015_count['May'] += 1

            elif creationdate > date15_4:

                month2015_count['April'] += 1

            elif creationdate > date15_3 :

                month2015_count['March'] += 1

            elif creationdate > date15_2 :

                month2015_count['February'] += 1

            elif creationdate > date15_1:

                month2015_count['January'] += 1



            elif creationdate > date14_12:

                month2014_count['December'] += 1

            elif creationdate > date14_11:

                month2014_count['November'] += 1

            elif creationdate > date14_10:

                month2014_count['October'] += 1

            elif creationdate > date14_9:

                month2014_count['September'] += 1

            elif creationdate > date14_8:

                month2014_count['August'] += 1

            elif creationdate > date14_7:

                month2014_count['July'] += 1

            elif creationdate > date14_6:

                month2014_count['June'] += 1

            elif creationdate > date14_5:

                month2014_count['May'] += 1

            elif creationdate > date14_4:

                month2014_count['April'] += 1

            elif creationdate > date14_3:

                month2014_count['March'] += 1

            elif creationdate > date14_2:

                month2014_count['February'] += 1

            elif creationdate > date14_1:

                month2014_count['January'] += 1



            elif creationdate > date13_12:

                month2013_count['December'] += 1

            elif creationdate > date13_11:

                month2013_count['November'] += 1

            elif creationdate > date13_10:

                month2013_count['October'] += 1

            elif creationdate > date13_9:

                month2013_count['September'] += 1

            elif creationdate > date13_8:

                month2013_count['August'] += 1

            elif creationdate > date13_7:

                month2013_count['July'] += 1

            elif creationdate > date13_6:

                month2013_count['June'] += 1

            elif creationdate > date13_5:

                month2013_count['May'] += 1

            elif creationdate > date13_4:

                month2013_count['April'] += 1

            elif creationdate > date13_3:

                month2013_count['March'] += 1

            elif creationdate > date13_2:

                month2013_count['February'] += 1

            elif creationdate > date13_1:

                month2013_count['January'] += 1



            elif creationdate > date12_12:

                month2012_count['December'] += 1

            elif creationdate > date12_11:

                month2012_count['November'] += 1

            elif creationdate > date12_10:

                month2012_count['October'] += 1

            elif creationdate > date12_9:

                month2012_count['September'] += 1

            elif creationdate > date12_8:

                month2012_count['August'] += 1

            elif creationdate > date12_7:

                month2012_count['July'] += 1

            elif creationdate > date12_6:

                month2012_count['June'] += 1

            elif creationdate > date12_5:

                month2012_count['May'] += 1

            elif creationdate > date12_4:

                month2012_count['April'] += 1

            elif creationdate > date12_3:

                month2012_count['March'] += 1

            elif creationdate > date12_2:

                month2012_count['February'] += 1

            elif creationdate > date12_1:

                month2012_count['January'] += 1



            elif creationdate > date11_12:

                month2011_count['December'] += 1

            elif creationdate > date11_11:

                month2011_count['November'] += 1

            elif creationdate > date11_10:

                month2011_count['October'] += 1

            elif creationdate > date11_9:

                month2011_count['September'] += 1

            elif creationdate > date11_8:

                month2011_count['August'] += 1

            elif creationdate > date11_7:

                month2011_count['July'] += 1

            elif creationdate > date11_6:

                month2011_count['June'] += 1

            elif creationdate > date11_5:

                month2011_count['May'] += 1

            elif creationdate > date11_4:

                month2011_count['April'] += 1

            elif creationdate > date11_3:

                month2011_count['March'] += 1

            elif creationdate > date11_2:

                month2011_count['February'] += 1

            elif creationdate > date11_1:

                month2011_count['January'] += 1



            elif creationdate > date10_12:

                month2010_count['December'] += 1

            elif creationdate > date10_11:

                month2010_count['November'] += 1

            elif creationdate > date10_10:

                month2010_count['October'] += 1

            elif creationdate > date10_9:

                month2010_count['September'] += 1

            elif creationdate > date10_8:

                month2010_count['August'] += 1

            elif creationdate > date10_7:

                month2010_count['July'] += 1

            elif creationdate > date10_6:

                month2010_count['June'] += 1

            elif creationdate > date10_5:

                month2010_count['May'] += 1

            elif creationdate > date10_4:

                month2010_count['April'] += 1

            elif creationdate > date10_3:

                month2010_count['March'] += 1

            elif creationdate > date10_2:

                month2010_count['February'] += 1

            elif creationdate > date10_1:

                month2010count['January'] += 1
            flag += 1


        print("This is 2017", month2017_count)

        print("This is 2016", month2016_count)

        print("This is 2015", month2015_count)

        print("This is 2014", month2014_count)

        print("This is 2013", month2013_count)

        print("This is 2012", month2012_count)

        print("This is 2011", month2011_count)

        print("This is 2010", month2010_count)

        print("beforeCreatedRussianAccount",beforeCreatedRussianAccount,
              "\n","afterCreatedRussianAccount",
                afterCreatedRussianAccount )

        trace1 =  go.Bar(
                    x = ['2010_1','2010_2','2010_3','2010_4','2010_5','2010_6',
                         '2010_7', '2010_8', '2010_9', '2010_10', '2010_11', '2010_12',

                         '2011_1', '2011_2', '2011_3', '2011_4', '2011_5', '2011_6',
                         '2011_7', '2011_8', '2011_9', '2011_10', '2011_11', '2011_12',

                         '2012_1', '2012_2', '2012_3', '2012_4', '2012_5', '2012_6',
                         '2012_7', '2012_8', '2012_9', '2012_10', '2012_11', '2012_12',

                         '2013_1', '2013_2', '2013_3', '2013_4', '2013_5', '2013_6',
                         '2013_7', '2013_8', '2013_9', '2013_10', '2013_11', '2013_12',

                         '2014_1', '2014_2', '2014_3', '2014_4', '2014_5', '2014_6',
                         '2014_7', '2014_8', '2014_9', '2014_10', '2014_11', '2014_12',

                         '2015_1', '2015_2', '2015_3', '2015_4', '2015_5', '2015_6',
                         '2015_7', '2015_8', '2015_9', '2015_10', '2015_11', '2015_12',

                         '2016_1', '2016_2', '2016_3', '2016_4', '2016_5', '2016_6',
                         '2016_7', '2016_8', '2016_9', '2016_10', '2016_11', '2016_12',

                         '2017_1', '2017_2', '2017_3'
                         ],
                    y = [ month2010_count['January'], month2010_count['February'],
                          month2010_count['March'], month2010_count['April'],
                          month2010_count['May'], month2010_count['June'],
                          month2010_count['July'],month2010_count['August'],
                          month2010_count['September'], month2010_count['October'],
                          month2010_count['November'], month2010_count['December'],

                          month2011_count['January'], month2011_count['February'],
                          month2011_count['March'], month2011_count['April'],
                          month2011_count['May'], month2011_count['June'],
                          month2011_count['July'], month2011_count['August'],
                          month2011_count['September'], month2011_count['October'],
                          month2011_count['November'], month2011_count['December'],

                          month2012_count['January'], month2012_count['February'],
                          month2012_count['March'], month2012_count['April'],
                          month2012_count['May'], month2012_count['June'],
                          month2012_count['July'], month2012_count['August'],
                          month2012_count['September'], month2012_count['October'],
                          month2012_count['November'], month2012_count['December'],

                          month2013_count['January'], month2013_count['February'],
                          month2013_count['March'], month2013_count['April'],
                          month2013_count['May'], month2013_count['June'],
                          month2013_count['July'], month2013_count['August'],
                          month2013_count['September'], month2013_count['October'],
                          month2013_count['November'], month2013_count['December'],

                          month2014_count['January'], month2014_count['February'],
                          month2014_count['March'], month2014_count['April'],
                          month2014_count['May'], month2014_count['June'],
                          month2014_count['July'], month2014_count['August'],
                          month2014_count['September'], month2014_count['October'],
                          month2014_count['November'], month2014_count['December'],

                          month2015_count['January'], month2015_count['February'],
                          month2015_count['March'], month2015_count['April'],
                          month2015_count['May'], month2015_count['June'],
                          month2015_count['July'], month2015_count['August'],
                          month2015_count['September'], month2015_count['October'],
                          month2015_count['November'], month2015_count['December'],

                          month2016_count['January'], month2016_count['February'],
                          month2016_count['March'], month2016_count['April'],
                          month2016_count['May'], month2016_count['June'],
                          month2016_count['July'], month2016_count['August'],
                          month2016_count['September'], month2016_count['October'],
                          month2016_count['November'], month2016_count['December'],

                          month2017_count['January'], month2017_count['February'],
                          month2017_count['March']
                          ]

        )
        beforeCreatedRussianAccount = 0
        afterCreatedRussianAccount = 0
        month2010_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2011_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2012_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2013_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2014_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2015_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2016_count = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,

                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

        month2017_count = {'January': 0, 'February': 0, 'March': 0}
        flag = 1
        sql1 = 'select CreationDate from stackcorepost where owneruserid = 4279 ;'
        cursor.execute(sql1)
        result1 = cursor.fetchall()

        sql2 = 'select creationdate from russiancoreuser where Id = 23044   ;'
        cursor.execute(sql2)
        result3 = cursor.fetchone()
        print(result3)
        usercreationdate = str(result3['creationdate'])[0:10] + ' ' + str(result3['creationdate'])[11:19]
        usercreationdate = datetime.datetime.strptime(usercreationdate, '%Y-%m-%d %H:%M:%S')

        while flag < len(result1):
            print(flag)
            result2 = result1[flag]
            creationdate = str(result2['CreationDate'])[0:10] + ' ' + str(result2['CreationDate'])[11:19]
            creationdate = datetime.datetime.strptime(creationdate, '%Y-%m-%d %H:%M:%S')
            print(creationdate)

            if creationdate > usercreationdate:
                afterCreatedRussianAccount += 1
            else:
                beforeCreatedRussianAccount += 1

            if creationdate > date17_3:

                month2017_count['March'] += 1

            elif creationdate > date17_2:

                month2017_count['February'] += 1

            elif creationdate > date17_1:

                month2017_count['January'] += 1





            elif creationdate > date16_12:

                month2016_count['December'] += 1

            elif creationdate > date16_11:

                month2016_count['November'] += 1

            elif creationdate > date16_10:

                month2016_count['October'] += 1

            elif creationdate > date16_9:

                month2016_count['September'] += 1

            elif creationdate > date16_8:

                month2016_count['August'] += 1

            elif creationdate > date16_7:

                month2016_count['July'] += 1

            elif creationdate > date16_6:

                month2016_count['June'] += 1

            elif creationdate > date16_5:

                month2016_count['May'] += 1

            elif creationdate > date16_4:

                month2016_count['April'] += 1

            elif creationdate > date16_3:

                month2016_count['March'] += 1

            elif creationdate > date16_2:

                month2016_count['February'] += 1

            elif creationdate > date16_1:

                month2016_count['January'] += 1





            elif creationdate > date15_12:

                month2015_count['December'] += 1

            elif creationdate > date15_11:

                month2015_count['November'] += 1

            elif creationdate > date15_10:

                month2015_count['October'] += 1

            elif creationdate > date15_9:

                month2015_count['September'] += 1

            elif creationdate > date15_8:

                month2015_count['August'] += 1

            elif creationdate > date15_7:

                month2015_count['July'] += 1

            elif creationdate > date15_6:

                month2015_count['June'] += 1

            elif creationdate > date15_5:

                month2015_count['May'] += 1

            elif creationdate > date15_4:

                month2015_count['April'] += 1

            elif creationdate > date15_3:

                month2015_count['March'] += 1

            elif creationdate > date15_2:

                month2015_count['February'] += 1

            elif creationdate > date15_1:

                month2015_count['January'] += 1



            elif creationdate > date14_12:

                month2014_count['December'] += 1

            elif creationdate > date14_11:

                month2014_count['November'] += 1

            elif creationdate > date14_10:

                month2014_count['October'] += 1

            elif creationdate > date14_9:

                month2014_count['September'] += 1

            elif creationdate > date14_8:

                month2014_count['August'] += 1

            elif creationdate > date14_7:

                month2014_count['July'] += 1

            elif creationdate > date14_6:

                month2014_count['June'] += 1

            elif creationdate > date14_5:

                month2014_count['May'] += 1

            elif creationdate > date14_4:

                month2014_count['April'] += 1

            elif creationdate > date14_3:

                month2014_count['March'] += 1

            elif creationdate > date14_2:

                month2014_count['February'] += 1

            elif creationdate > date14_1:

                month2014_count['January'] += 1



            elif creationdate > date13_12:

                month2013_count['December'] += 1

            elif creationdate > date13_11:

                month2013_count['November'] += 1

            elif creationdate > date13_10:

                month2013_count['October'] += 1

            elif creationdate > date13_9:

                month2013_count['September'] += 1

            elif creationdate > date13_8:

                month2013_count['August'] += 1

            elif creationdate > date13_7:

                month2013_count['July'] += 1

            elif creationdate > date13_6:

                month2013_count['June'] += 1

            elif creationdate > date13_5:

                month2013_count['May'] += 1

            elif creationdate > date13_4:

                month2013_count['April'] += 1

            elif creationdate > date13_3:

                month2013_count['March'] += 1

            elif creationdate > date13_2:

                month2013_count['February'] += 1

            elif creationdate > date13_1:

                month2013_count['January'] += 1



            elif creationdate > date12_12:

                month2012_count['December'] += 1

            elif creationdate > date12_11:

                month2012_count['November'] += 1

            elif creationdate > date12_10:

                month2012_count['October'] += 1

            elif creationdate > date12_9:

                month2012_count['September'] += 1

            elif creationdate > date12_8:

                month2012_count['August'] += 1

            elif creationdate > date12_7:

                month2012_count['July'] += 1

            elif creationdate > date12_6:

                month2012_count['June'] += 1

            elif creationdate > date12_5:

                month2012_count['May'] += 1

            elif creationdate > date12_4:

                month2012_count['April'] += 1

            elif creationdate > date12_3:

                month2012_count['March'] += 1

            elif creationdate > date12_2:

                month2012_count['February'] += 1

            elif creationdate > date12_1:

                month2012_count['January'] += 1



            elif creationdate > date11_12:

                month2011_count['December'] += 1

            elif creationdate > date11_11:

                month2011_count['November'] += 1

            elif creationdate > date11_10:

                month2011_count['October'] += 1

            elif creationdate > date11_9:

                month2011_count['September'] += 1

            elif creationdate > date11_8:

                month2011_count['August'] += 1

            elif creationdate > date11_7:

                month2011_count['July'] += 1

            elif creationdate > date11_6:

                month2011_count['June'] += 1

            elif creationdate > date11_5:

                month2011_count['May'] += 1

            elif creationdate > date11_4:

                month2011_count['April'] += 1

            elif creationdate > date11_3:

                month2011_count['March'] += 1

            elif creationdate > date11_2:

                month2011_count['February'] += 1

            elif creationdate > date11_1:

                month2011_count['January'] += 1



            elif creationdate > date10_12:

                month2010_count['December'] += 1

            elif creationdate > date10_11:

                month2010_count['November'] += 1

            elif creationdate > date10_10:

                month2010_count['October'] += 1

            elif creationdate > date10_9:

                month2010_count['September'] += 1

            elif creationdate > date10_8:

                month2010_count['August'] += 1

            elif creationdate > date10_7:

                month2010_count['July'] += 1

            elif creationdate > date10_6:

                month2010_count['June'] += 1

            elif creationdate > date10_5:

                month2010_count['May'] += 1

            elif creationdate > date10_4:

                month2010_count['April'] += 1

            elif creationdate > date10_3:

                month2010_count['March'] += 1

            elif creationdate > date10_2:

                month2010_count['February'] += 1

            elif creationdate > date10_1:

                month2010_count['January'] += 1
            flag += 1

        print("This is 2017", month2017_count)

        print("This is 2016", month2016_count)

        print("This is 2015", month2015_count)

        print("This is 2014", month2014_count)

        print("This is 2013", month2013_count)

        print("This is 2012", month2012_count)

        print("This is 2011", month2011_count)

        print("This is 2010", month2010_count)

        print("beforeCreatedRussianAccount", beforeCreatedRussianAccount,
              "\n", "afterCreatedRussianAccount",
              afterCreatedRussianAccount)

        trace2 = go.Bar(
            x=['2010_1', '2010_2', '2010_3', '2010_4', '2010_5', '2010_6',
               '2010_7', '2010_8', '2010_9', '2010_10', '2010_11', '2010_12',

               '2011_1', '2011_2', '2011_3', '2011_4', '2011_5', '2011_6',
               '2011_7', '2011_8', '2011_9', '2011_10', '2011_11', '2011_12',

               '2012_1', '2012_2', '2012_3', '2012_4', '2012_5', '2012_6',
               '2012_7', '2012_8', '2012_9', '2012_10', '2012_11', '2012_12',

               '2013_1', '2013_2', '2013_3', '2013_4', '2013_5', '2013_6',
               '2013_7', '2013_8', '2013_9', '2013_10', '2013_11', '2013_12',

               '2014_1', '2014_2', '2014_3', '2014_4', '2014_5', '2014_6',
               '2014_7', '2014_8', '2014_9', '2014_10', '2014_11', '2014_12',

               '2015_1', '2015_2', '2015_3', '2015_4', '2015_5', '2015_6',
               '2015_7', '2015_8', '2015_9', '2015_10', '2015_11', '2015_12',

               '2016_1', '2016_2', '2016_3', '2016_4', '2016_5', '2016_6',
               '2016_7', '2016_8', '2016_9', '2016_10', '2016_11', '2016_12',

               '2017_1', '2017_2', '2017_3'
               ],
            y=[month2010_count['January'], month2010_count['February'],
               month2010_count['March'], month2010_count['April'],
               month2010_count['May'], month2010_count['June'],
               month2010_count['July'], month2010_count['August'],
               month2010_count['September'], month2010_count['October'],
               month2010_count['November'], month2010_count['December'],

               month2011_count['January'], month2011_count['February'],
               month2011_count['March'], month2011_count['April'],
               month2011_count['May'], month2011_count['June'],
               month2011_count['July'], month2011_count['August'],
               month2011_count['September'], month2011_count['October'],
               month2011_count['November'], month2011_count['December'],

               month2012_count['January'], month2012_count['February'],
               month2012_count['March'], month2012_count['April'],
               month2012_count['May'], month2012_count['June'],
               month2012_count['July'], month2012_count['August'],
               month2012_count['September'], month2012_count['October'],
               month2012_count['November'], month2012_count['December'],

               month2013_count['January'], month2013_count['February'],
               month2013_count['March'], month2013_count['April'],
               month2013_count['May'], month2013_count['June'],
               month2013_count['July'], month2013_count['August'],
               month2013_count['September'], month2013_count['October'],
               month2013_count['November'], month2013_count['December'],

               month2014_count['January'], month2014_count['February'],
               month2014_count['March'], month2014_count['April'],
               month2014_count['May'], month2014_count['June'],
               month2014_count['July'], month2014_count['August'],
               month2014_count['September'], month2014_count['October'],
               month2014_count['November'], month2014_count['December'],

               month2015_count['January'], month2015_count['February'],
               month2015_count['March'], month2015_count['April'],
               month2015_count['May'], month2015_count['June'],
               month2015_count['July'], month2015_count['August'],
               month2015_count['September'], month2015_count['October'],
               month2015_count['November'], month2015_count['December'],

               month2016_count['January'], month2016_count['February'],
               month2016_count['March'], month2016_count['April'],
               month2016_count['May'], month2016_count['June'],
               month2016_count['July'], month2016_count['August'],
               month2016_count['September'], month2016_count['October'],
               month2016_count['November'], month2016_count['December'],

               month2017_count['January'], month2017_count['February'],
               month2017_count['March']
               ]

        )

        data = [trace1,trace2]
        layout = go.Layout(
            barmode='group'
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='bothInactive')


    connection.commit()

finally:
    connection.close()



