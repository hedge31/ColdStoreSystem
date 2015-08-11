# encoding: utf-8
'''
Created on 2015年8月5日

@author: hedge31
'''
import sqlite3
from PyQt4.QtCore import QDate
from PyQt4.QtGui import QMessageBox,QDialog,QGridLayout,QLabel,QLineEdit
def connectDB():
    dataConnect = sqlite3.connect('data.db')
    return dataConnect,dataConnect.cursor()

def closeDB(DBConnect,cur):
    cur.close()
    DBConnect.commit()
    DBConnect.close()
    

def insertRkd(rkdForm):
     
    DBconnect,cur = connectDB()
    cur.execute('select Max(id) from rkd')
    maxid = cur.fetchone()
    if maxid[0] == None :
        max = 1
    else:
        max = maxid[0]+1
    
#     BusinessDate = rkd.inDateEdit.date()
    docno = u'IN'+u'%s%04d'%(rkdForm.inDateEdit.date().toString('yyyyMMdd'),max)
    custom = rkdForm.CustomText.text()
    item = rkdForm.ItemText.text()
    Weight = rkdForm.weightText.text()
    InDate = rkdForm.inDateEdit.date().toString('yyyy-MM-dd')
    sql = u'insert into rkd (DocNo,Custom,Item,Weight,InDate,Stock) values (\'%s\',\'%s\',\'%s\',%s,\'%s\',%s)'%(docno,custom,item,Weight,InDate,Weight)
    cur.execute(sql)
    closeDB(DBconnect,cur)
    retrieveRkd(rkdForm,docno)
    QMessageBox.information(rkdForm,"Information",u'新增成功')
    
def retrieveRkd(rkdForm,docno):
    DBconnect,cur = connectDB()
    sql = u'select docno,custom,item,weight,indate,stock from rkd where docno = \'%s\''%(docno)
    cur.execute(sql)
    row = cur.fetchone()
    rkdForm.rkdDocNoText.setText(str(row[0]))
    rkdForm.CustomText.setText(str(row[1]))
    rkdForm.ItemText.setText(str(row[2]))
    rkdForm.weightText.setText(str(row[3]))
    rkdForm.inDateEdit.setDate(QDate().fromString(str(row[4]),'yyyy-MM-DD'))
    rkdForm.stockText.setText(str(row[5]))
    closeDB(DBconnect,cur)

def updateRkd(rkdForm):
    if rkdForm.rkdDocNoText.text() == u'自动编号':
        return insertRkd(rkdForm)
    else:
        DBconnect,cur = connectDB()
        docno = rkdForm.rkdDocNoText.text()
        custom = rkdForm.CustomText.text()
        item = rkdForm.ItemText.text()
        Weight = rkdForm.weightText.text()
        InDate = rkdForm.inDateEdit.date().toString('yyyy-MM-dd')
        sql = u'update rkd set custom = \'%s\',item = \'%s\',weight = %s,indate = \'%s\' where docno =  \'%s\''%(custom,item,Weight,InDate,docno)
        cur.execute(str(sql))
        closeDB(DBconnect,cur)
        retrieveRkd(rkdForm, docno)
        QMessageBox.information(rkdForm,"Information",u'保存成功')
        
def deleteRkd(rkdForm):
    DBconnect,cur = connectDB()
    docno = rkdForm.rkdDocNoText.text()
    sql = u'delete from rkd where docno = \'%s\''%(docno)
    cur.execute(sql)
    if cur.rowcount != 0 :
        mess = u'删除成功'
    else:
        mess = u'没有找到对应的单据'
    closeDB(DBconnect,cur)
    clearRkd(rkdForm)
    QMessageBox.information(rkdForm,"Information",mess)

def clearRkd(rkdForm):
    rkdForm.rkdDocNoText.setText(u'自动编号')
    rkdForm.CustomText.clear()
    rkdForm.ItemText.clear()
    rkdForm.weightText.clear()
    rkdForm.inDateEdit.setDate(QDate.currentDate())
    rkdForm.stockText.clear()
    

    