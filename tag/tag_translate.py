#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import pymysql.cursors
import datetime
import time
from translate import Translator

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

        htmlfile = open('C:\\Users\\Administrator\\Desktop\\2.html', encoding="utf-8")
        htmlpage = htmlfile.read()
        soap = BeautifulSoup(htmlpage, "html.parser")
        text = soap.find_all('td')

        flag=0
        for i in text:
            flag+=1
            russiantag = i.string
            print(flag)
            translator = Translator(from_lang="ru" ,to_lang="en")
            tag_translation = translator.translate(russiantag)

            print(russiantag , tag_translation)
            sql1 = 'update russiantagsinrussian set translate_tagname=\'%s\' where tagname = \'%s\' ;' %(tag_translation,str(russiantag))
            cursor.execute(sql1)
            connection.commit()

        print("\n\nAll translated\n\n")


finally:
    connection.close()

