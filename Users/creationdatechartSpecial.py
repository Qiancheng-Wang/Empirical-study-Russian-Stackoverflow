import pymysql.cursors
import datetime
import time

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'wqc050868',
    'db': 'test',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,

}

connection = pymysql.connect(**config)

try:
    with connection.cursor() as cursor:
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

        flag = -1
        while 1:
            flag += 2
            print(flag)
            if flag > 71502:
                break

            sql1 = 'select CreationDate,AccountID from FinalCompare where rownum = %s ;' % flag
            cursor.execute(sql1)
            result = cursor.fetchone()
            creationdate = str(result['CreationDate'])[0:10] + ' ' + str(result['CreationDate'])[11:19]
            creationdate = datetime.datetime.strptime(creationdate, '%Y-%m-%d %H:%M:%S')
            accountId = result['accountId']

            sql2 = 'select rownum from FinalCompare where rownum = %s ;'

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
                month2010count['January'] += 1

        print("This is 2017", month2017_count)
        print("This is 2016", month2016_count)
        print("This is 2015", month2015_count)
        print("This is 2014", month2014_count)
        print("This is 2013", month2013_count)
        print("This is 2012", month2012_count)
        print("This is 2011", month2011_count)
        print("This is 2010", month2010_count)

    connection.commit()

finally:
    connection.close()



