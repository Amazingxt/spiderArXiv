# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sqlite3
import datetime

i = datetime.datetime.now()

class ArxivPipeline(object):

    def __init__(self):

        self.today = str(i.year)+'-'+str(i.month)+'-'+str(i.day)+'-articles.db'
        self.conn = sqlite3.connect('./Web_in_dash/DataBase/' + self.today)
        self.c = self.conn.cursor()

    def close_spider(self,spider):

        self.conn.commit()
        self.c.close()
        self.conn.close()

    def process_item(self, item, spider):

        try:
            self.c.execute('''create table user_tb(
                _id integer primary key autoincrement,
                title text,
                abstract text,
                url text,
                authors text,
                major text)
                ''')
        except:
            pass

        self.c.execute('insert into user_tb values(null, ?, ?, ?, ?,?)',
            ((item['title'],item['abstract'],item['url'],item['authors'],item['major'])))

