#-*- coding: UTF-8 -*-
import os
import sqlite3

conn = sqlite3.connect('test.db')
print("success conn")
cursor = conn.cursor()
sql1 = "create table user (id varchar(20) primary key, name varchar(20),tel varchar(200),QQ int(10)," \
       "beizhu varchar(500))"

cursor.execute(sql1)
print("table has been create")
