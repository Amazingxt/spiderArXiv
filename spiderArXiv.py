# encoding:utf-8

import Query as Qu
import Send_Info as Se
import re
import datetime

i = datetime.datetime.now()

dbName = './Web_in_dash/DataBase/personQueryInfo.db'


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
        for title_key, title_value in articleInfo['title'].items():

            if ((len(re.findall(person_value + ' ', title_value, flags=re.IGNORECASE)) +
                 len(re.findall(' ' + person_value + ' ', title_value, flags=re.IGNORECASE)) +
                    len(re.findall(' ' + person_value, title_value, flags=re.IGNORECASE))) > 0):

                try:
                    personIndex[person_key].add(title_key)
                except:
                    personIndex[person_key] = set()
                    personIndex[person_key].add(title_key)

    for person_key, person_value in personsInfo['keyWords'].items():
        for abs_key, abs_value in articleInfo['abstract'].items():

            if (len(re.findall(person_value + ' ', str(abs_value), flags=re.IGNORECASE)) +
                len(re.findall(' ' + person_value + ' ', str(abs_value), flags=re.IGNORECASE)) +
                    len(re.findall(' ' + person_value, str(abs_value), flags=re.IGNORECASE)) > 0):

                try:
                    personIndex[person_key].add(abs_key)
                except:
                    personIndex[person_key] = set()
                    personIndex[person_key].add(abs_key)

    for person_key, person_value in personsInfo['authors'].items():

        for author_key, author_value in articleInfo['authors'].items():

            if re.findall(person_value, author_value, flags=re.IGNORECASE):

                try:
                    personIndex[person_key].add(author_key)

                except:
                    personIndex[person_key] = set()
                    personIndex[person_key].add(author_key)

    return personIndex


def merge_Info(articleInfo, index):

    index = list(index)
    cutline = '--------------------------------------------------------------\n'
    infomation = ''
    for ind in index:
        title = articleInfo['title'][ind]
        authors = articleInfo['authors'][ind]
        abstract = articleInfo['abstract'][ind]
        url = articleInfo['url'][ind]
        info = ("title: %s\n" + "authors: %s\n" + "url: %s\n" +
                "abstract: %s\n") % (title, authors, url, abstract) + cutline
        infomation += info
    return infomation


def draw_Info(articleInfo, personsInfo, personIndex):

    Info = {}
    for index, article_index in personIndex.items():
        if personsInfo['major_interest'][index] == articleInfo['major'][index]:
            infomation = merge_Info(articleInfo, article_index)

            Info[personsInfo['email'][index]] = infomation

    return Info


def send_emails(Info):

    today = str(i.year) + '-' + str(i.month) + '-' + str(i.day)
    subject = 'arXiv articles in quant-ph on ' + today

    for email, info in Info.items():
        print email
        s1 = Se.Send_Email(email)
        s1.send_info(info, subject)


if __name__ == "__main__":

    articleInfo = get_articleInfo()
    personsInfo = get_personsInfo(dbName)
    personIndex = find_Infointerset(articleInfo, personsInfo)
    Info = draw_Info(articleInfo, personsInfo, personIndex)
    # print Info
    send_emails(Info)
    # print personIndex
    # print personsInfo['email']
    # s1 = Se.Send_Email(receivers)
    # s1.send_info(self, mainText, subject)
