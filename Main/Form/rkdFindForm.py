# encoding: utf-8
'''
Created on 2015年8月19日

@author: Administrator
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Control import rkdOperate
class rkdFindForm(QDialog):
    '''
    入库单查找
    '''
    def __init__(self,parent = None):
        super(rkdFindForm,self).__init__(parent)
        self.parent = parent
        self.setWindowTitle(u'查找')
        self.findDialogLayout = QGridLayout(self)
        self.findDialogLayout.setContentsMargins(20, 5, 20, 5)
        self.findargv = [(u'docno',u'入库单号',u'string'),
                         (u'custom',u'客户',u'string'),
                         (u'Item',u'料品规格',u'string'),
                         ]
        row = 1
        col = 1
        for line in self.findargv:
            if col >= 4:
                col =1
                row +=1
            temp = QLabel(self)
            temp.setObjectName(u'find'+line[0])
            temp.setMinimumWidth(70)
            temp.setMaximumWidth(100)
            temp.setText(line[1]+u':')
            temp.setMargin(5)
            self.findDialogLayout.addWidget(self.findChild(QLabel,u'find'+line[0]),row,col)
            col +=1
            if line[2] == u'string' :
                temp = QLineEdit()
            elif line[2] == u'date' :
                temp = QDateEdit(QDate.currentDate())              
            else:
                pass
            
            temp.setObjectName(u'find'+line[0])
            
            temp.setMinimumWidth(100)
            temp.setMaximumWidth(150)
            self.findDialogLayout.addWidget(temp,row,col)
            col +=1
        
        self.findButton = QPushButton(self)
        self.findButton.setText(u'查找')
        self.findDialogLayout.addWidget(self.findButton,row+1,3)
        
        self.tableView = QTableView(self)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.findDialogLayout.addWidget(self.tableView,row+2,1,4,10)
        rkdOperate.queryRkd(self.tableView)
        self.connect(self.findButton, SIGNAL('clicked()'),self.refreshTable)
        #self.connect(self.tableView,SIGNAL('clicked()'),self.finded)
        self.tableView.doubleClicked.connect(self.finded)
        self.setLayout(self.findDialogLayout)
        
    def getFilter(self):
        strFilter = ''
        a = 0
        while a < len(self.findargv):
            arg = self.findargv[a]
            if arg[2] == u'string' :
                
                qg = self.findChild(QLineEdit,u'find'+arg[0])
                if qg.text() != '':
                    strFilter = strFilter + arg[0] + ' = \'' + qg.text() + '\' ' + ' and '
                       
            elif arg[2] == u'date' :
                qg = self.findChild(QDateEdit, u'find'+arg[0])
                date = qg.date().toString('yyyy-MM-dd') 
                strFilter = strFilter + arg[0] + ' = \'' + date + '\' ' +' and '
            
            
            a = a +1
        
        strFilter = strFilter[:-5]   
        return strFilter
    
    def finded(self,index):
        rkdOperate.findedRkdForm(self,index)
    

    def refreshTable(self): 
        rkdOperate.queryRkdfilter(self.tableView, self.getFilter())
        