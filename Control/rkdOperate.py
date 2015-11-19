# encoding: utf-8
'''
Created on 2015年8月5日

@author: hedge31
'''
import sqlite3
from PyQt4.QtCore import QDate,QString
from PyQt4.QtGui import QMessageBox,QDialog,QGridLayout,QLabel,QLineEdit,QAbstractItemView
from PyQt4.QtSql import *
import Dialog
#打开SQLITE连接
def connectDB():
    dataConnect = sqlite3.connect('data.db')
    return dataConnect,dataConnect.cursor()

#关闭SQLITE连接
def closeDB(DBConnect,cur):
    cur.close()
    DBConnect.commit()
    DBConnect.close()
    
#新增入库单
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




#重新载入入库单
def retrieveRkd(rkdForm,docno):
    DBconnect,cur = connectDB()
    sql = u'select docno,custom,item,weight,indate,stock from rkd where docno = \'%s\''%(docno)
    cur.execute(sql)
    row = cur.fetchone()
    rkdForm.rkdDocNoText.setText(row[0])
    if isinstance(row[1], int) or isinstance(row[1], float):
        rkdForm.CustomText.setText(str(row[1]))
    else:
        rkdForm.CustomText.setText(row[1])
    
    if isinstance(row[2], int) or isinstance(row[2], float):
        rkdForm.ItemText.setText(str(row[2]))
    else:
        rkdForm.ItemText.setText(row[2])
    rkdForm.weightText.setText(str(row[3]))
    rkdForm.inDateEdit.setDate(QDate().fromString(row[4],'yyyy-MM-DD'))
    rkdForm.stockText.setText(str(row[5]))
    closeDB(DBconnect,cur)

#更新入库单
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

        cur.execute(sql)
        closeDB(DBconnect,cur)
        retrieveRkd(rkdForm, docno)
        QMessageBox.information(rkdForm,"Information",u'保存成功')

#删除入库单       
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


#清除或初始化入库单界面
def clearRkd(rkdForm):
    rkdForm.rkdDocNoText.setText(u'自动编号')
    rkdForm.CustomText.clear()
    rkdForm.ItemText.clear()
    rkdForm.weightText.clear()
    rkdForm.inDateEdit.setDate(QDate.currentDate())
    rkdForm.stockText.clear()
    
def createConnection(): 
    if QSqlDatabase.contains('qt_sql_default_connection'):
        db = QSqlDatabase.database("qt_sql_default_connection")
    else:
        #选择数据库类型，这里为sqlite3数据库
        db=QSqlDatabase.addDatabase("QSQLITE") 
        #创建数据库data.db,如果存在则打开，否则创建该数据库
        db.setDatabaseName("data.db") 
    #打开数据库
    db.open() 
    
    return db

def queryRkd(tableView): 
    createConnection()
    model = QSqlTableModel()
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.setTable(u'rkd')
    model.removeColumns(0,1)
    model.setFilter('')
    model.select()
    tableView.setModel(model)
    tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

def queryRkdfilter(tableView,thisfilter): 
    createConnection()
    model = QSqlTableModel()
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.setTable(u'rkd')
    model.removeColumns(0,1)
    model.setFilter(thisfilter)
    model.select()
    tableView.setModel(model)
    tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

def findedRkdForm(dialog,Index):
    model = dialog.tableView.model()
    record = model.record(Index.row())
    docno = record.value(u'docno').toString()
    retrieveRkd(dialog.parent, docno)
    dialog.close()

    
