# encoding:utf-8

import sqlite3
import datetime


class Query_articleInfo(object):

    def __init__(self):

        self.i = datetime.datetime.now()

        self.today = str(self.i.year) + '-' + str(self.i.month) + \
            '-' + str(self.i.day) + '-quant-ph.db'

    def connect_db(self):

        try:
            self.conn = sqlite3.connect(self.today)
            self.c = self.conn.cursor()
            print 'connect article database success!'
        except:
            raise 'connect article database failed'

    def close_db(self):

        self.c.close()
        self.conn.close()

    def query_info(self, keys):

        self.c.execute('select * from user_tb where _id > ?', (0,))
        info = {}
        title = {}
        abstract = {}
        url = {}
        authors = {}
        while True:
            row = self.c.fetchone()
            if not row:
                break
            title[row[0]] = row[1]
            abstract[row[0]] = row[2]
            url[row[0]] = row[3]
            authors[row[0]] = row[4]

        info[keys[1]] = title
        info[keys[2]] = abstract
        info[keys[3]] = url
        info[keys[4]] = authors

        return info

    def get_rowNumber(self):

        return self.c.rowcount

    def get_keys(self):

        keys = []
        self.c.execute('select * from user_tb where _id > ?', (0,))
        for col in (self.c.description):
            keys.append(col[0])
        return keys


class Query_personInfo(object):

    def __init__(self,dbName):
        self.dbName = dbName

    def connect_db(self):

        try:
            self.conn = sqlite3.connect(self.dbName)
            self.c = self.conn.cursor()
            print 'connect person database success!'
        except:
            raise 'connect person database failed'

    def close_db(self):

        self.c.close()
        self.conn.close()

    def query_info(self, keys):

        self.c.execute('select * from user_tb where _id > ?', (0,))
        info = {}

        keyWords = {}
        authors = {}
        email = {}

        while True:
            row = self.c.fetchone()
            if not row:
                break
            keyWords[row[0]] = row[1]
            authors[row[0]] = row[2]
            email[row[0]] = row[3]

        info[keys[1]] = keyWords
        info[keys[2]] = authors
        info[keys[3]] = email

        return info

    def get_rowNumber(self):

        return self.c.rowcount

    def get_keys(self):

        keys = []
        self.c.execute('select * from user_tb where _id > ?', (0,))
        for col in (self.c.description):
            keys.append(col[0])
        return keys
