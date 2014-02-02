# -*- coding: utf-8 -*-

from datetime import *  
import time  
import sqlite3
import sys

def listnest(dcon,mCursor):
    mCursor.execute("select * from wb order by datetime desc")
    for item in mCursor:
		print item[1]
    print ' '

def haveaidea(dcon):
    msgcontent = raw_input("有所思： ").decode(sys.stdin.encoding) 
    msgdate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print msgdate,msgcontent
    dcon.execute("INSERT INTO wb(content,datetime)\
			VALUES (?,?)" ,(msgcontent,datetime.now()))
    dcon.commit()
    print '###',msgcontent,'###'

conn=sqlite3.connect('main.db')
# conn = sqlite3.connect(":memory:")
cu=conn.cursor()

aaa='1'
while aaa<>'0' :

    aaa = raw_input("选择 0退出，1插入，2搜索，3历史: ")

    if aaa=='1' :
        haveaidea(conn)
    if aaa=='2' :
        print '2 ',' search '
    if aaa=='3' :
        print listnest(conn,cu)

conn.close


