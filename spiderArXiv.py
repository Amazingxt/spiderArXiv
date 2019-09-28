# encoding:utf-8

import Query as Qu
import re

dbName = 'personQueryInfo.db'


def get_articleInfo():

    articles = Qu.Query_articleInfo()
    articles.connect_db()
    articleKeys = articles.get_keys()
    articleInfo = articles.query_info(articleKeys)
    articles.close_db()
    return articleInfo


def get_personsInfo(dbName):

    persons = Qu.Query_personInfo(dbName)
    persons.connect_db()
    personsKeys = persons.get_keys()
    personsInfo = persons.query_info(personsKeys)
    persons.close_db()
    return personsInfo


def find_Infointerset(articleInfo, personsInfo):

    personIndex = {}
    for person_key, person_value in personsInfo['keyWords'].items():
        for article_key, article_value in articleInfo['title'].items():

            if re.findall(person_value, article_value, flags=re.IGNORECASE):

                try:
                    personIndex[person_key].add(article_key)
                except:
                    personIndex[person_key] = set()
                    personIndex[person_key].add(article_key)

        for article_key, article_value in articleInfo['abstract'].items():

            print article_value
            if re.findall(person_value, article_value, flags=re.IGNORECASE):

                try:
                    personIndex[person_key].add(article_key)
                except:
                    personIndex[person_key] = set()
                    personIndex[person_key].add(article_key)

    for person_key, person_value in personsInfo['authors'].items():
        for article_key, article_value in articleInfo['authors'].items():

            if re.findall(person_value, article_value, flags=re.IGNORECASE):

                try:
                    personIndex[person_key].add(article_key)

                except:
                    personIndex[person_key] = set()
                    personIndex[person_key].add(article_key)

    return personIndex


articleInfo = get_articleInfo()
personsInfo = get_personsInfo(dbName)
# personIndex = find_Infointerset(articleInfo, personsInfo)
print articleInfo['abstract']
