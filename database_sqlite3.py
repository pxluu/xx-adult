#-*- coding: UTF-8 -*-
#-*- coding: UTF-8 -*-
import os
import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()
# 删除表
cursor.execute("drop table if exists user ")
print("delete success conn")
sql1 = "create table user (id varchar(20) primary key, name varchar(20),tel varchar(200),QQ int(10)," \
       "beizhu varchar(500))"

cursor.execute(sql1)

cursor.close()
conn.commit()
conn.close()
print("table has been create")
