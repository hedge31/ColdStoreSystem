# encoding: utf-8
'''
Created on 2015年8月5日

@author: hedge31
'''


import sqlite3


def meteData():
    dataConnect = sqlite3.connect('data.db')
    cursor = dataConnect.cursor()
    cursor.execute(u'DROP TABLE IF EXISTS rkd')
    cursor.execute(u'create table rkd (ID integer PRIMARY KEY autoincrement,DocNO c,Custom c,Item c,Weight e,InDate i,Stock f  ) ')
    cursor.execute(u'pragma table_info(rkd)')
    
    print cursor.fetchall()
    cursor.close()
    dataConnect.close()
    print u'数据库初始化成功'
    

    
    