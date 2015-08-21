# encoding: utf-8
'''
Created on 2015年8月5日

@author: hedge31
'''


import sqlite3
from PyQt4.QtGui import QMessageBox


def meteData():
    answer=QMessageBox.question(None,u"数据库初始化",  
                                u"已到达文档结尾,是否从头查找?",  
                                QMessageBox.Ok|QMessageBox.Cancel,  
                                QMessageBox.Ok)
    
    if answer == QMessageBox.Ok:
        dataConnect = sqlite3.connect('data.db')
        cursor = dataConnect.cursor()
        cursor.execute(u'DROP TABLE IF EXISTS rkd')
        cursor.execute(u'create table rkd (ID integer PRIMARY KEY autoincrement,DocNO c,Custom c,Item c,Weight e,InDate i,Stock f  ) ')
        cursor.execute(u'pragma table_info(rkd)')
        cursor.fetchall()
        cursor.close()
        dataConnect.close()
        QMessageBox.information(None,u'数据库初始化',u'初始化数据库成功！')
    else:
        return

    
    