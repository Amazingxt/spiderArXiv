# encoding:utf-8

# import sqlite3

# conn = sqlite3.connect('personQueryInfo.db')
# c = conn.cursor()

# try:
#     c.execute('''create table user_tb(
#         _id integer primary key autoincrement,
#         keyWords text,
#         authors text,
#         email text)
#         ''')
# except:
#     pass
# c.executemany('insert into user_tb values(null, ?, ?, ?)',
#               (('atom', 'stefan', 'amz@mail.ustc.edu.cn'),
#               ('computers', 'devoret', 'aimingzhong@foxmail.com')))
# conn.commit()
# c.close()
# conn.close()
import re

a = 'pythonl'
print len(re.findall(a,'python python',flags=re.IGNORECASE))