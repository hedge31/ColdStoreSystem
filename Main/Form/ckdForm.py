# encoding: utf-8
'''
Created on 2015年8月5日

@author: hedge31
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
<<<<<<< HEAD
from Control import rkdOperate
from ckdFindForm import ckdFindForm
=======
import datetime

>>>>>>> parent of 364297f... 1.2
class UI_ckd(QWidget):
    def __init__(self,parent = None):
        super(UI_ckd,self).__init__(parent)
        self.resize(200,200)
        self.setGeometry(QRect(20, 20, 246, 141))
        self.setMinimumSize(200, 200)
        self.CkdInput = QVBoxLayout(self)
        self.CkdInput.setMargin(5)
        self.CkdInput.setObjectName(u"CkdInput")
        
        #入库单主布局设置
        self.CkdInput.addLayout(self.createCKDDocNoLine())
        self.CkdInput.addLayout(self.createCustomLine())
        self.CkdInput.addLayout(self.createItemLine())
        self.CkdInput.addLayout(self.createWeightLine())
        self.CkdInput.addLayout(self.createOutDateLine())
        self.CkdInput.addLayout(self.createButtonLine())
        self.CkdInput.addStretch()
        
        #主界面添加布局
        self.setLayout(self.CkdInput)
    
    def createCKDDocNoLine(self):
        self.ckdDocNoLine = QHBoxLayout()
        self.ckdDocNoLine.setObjectName(u"ckdDocNOLine")
        self.ckdDocNoLable = QLabel(self)
        self.ckdDocNoLable.setObjectName(u"ckdDocNOLable")
        self.ckdDocNoLable.setText(u'入库单号:')
        self.ckdDocNoLable.setMinimumWidth(70)
        self.ckdDocNoLable.setMargin(5)
        self.spacerCustom = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ckdDocNoText = QLineEdit(self)
        self.ckdDocNoText.setObjectName(u"CustomText")
        self.ckdDocNoText.setReadOnly(True)
        self.ckdDocNoText.setText(u'自动编号')
        self.ckdDocNoText.setMinimumWidth(100)
        self.ckdDocNoText.setMaximumWidth(150)    
        #客户行布局
        self.ckdDocNoLine.addWidget(self.ckdDocNoLable)
        self.ckdDocNoLine.addWidget(self.ckdDocNoText)
        self.ckdDocNoLine.addSpacerItem(self.spacerCustom)
        return self.ckdDocNoLine
        
    def createCustomLine(self):
                #客户录入行组件
        self.CustomLine = QHBoxLayout()
        self.CustomLine.setObjectName(u"CustomLine")
        self.CustomLable = QLabel(self)
        self.CustomLable.setObjectName(u"CustomLable")
        self.CustomLable.setText(u'客户:')
        self.CustomLable.setMinimumWidth(70)
        self.CustomLable.setMargin(5)
        self.spacerCustom = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.CustomText = QLineEdit(self)
        self.CustomText.setObjectName(u"CustomText")
        self.CustomText.setMinimumWidth(100)
        self.CustomText.setMaximumWidth(150)    
        #客户行布局
        self.CustomLine.addWidget(self.CustomLable)
        self.CustomLine.addWidget(self.CustomText)
        self.CustomLine.addSpacerItem(self.spacerCustom)
        return self.CustomLine
    
    def createItemLine(self):
                #料品规格录入行组件
        self.ItemLine = QHBoxLayout()
        self.ItemLine.setObjectName(u"ItemLine")
        self.ItemLable = QLabel(self)
        self.ItemLable.setObjectName(u"ItemLable")
        self.ItemLable.setText(u'料器规格:')
        self.ItemLable.setMinimumWidth(70)
        self.ItemLable.setMargin(5)
        self.spacerItem = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ItemText = QLineEdit(self)
        self.ItemText.setObjectName(u"ItemText")
        self.ItemText.setMinimumWidth(100)
        self.ItemText.setMaximumWidth(150)
                
        #料品规格行布局
        self.ItemLine.addWidget(self.ItemLable)
        self.ItemLine.addWidget(self.ItemText)
        self.ItemLine.addSpacerItem(self.spacerItem)
        return self.ItemLine



    #重量录入行
    def createWeightLine(self): 
        #重量录入行组件创建      
        self.weightLine = QHBoxLayout()
        self.weightLine.setObjectName(u"weightLine")
        self.weightLable = QLabel(self)
        self.weightLable.setObjectName(u"weightLable")
        self.weightLable.setText(u'重量(T):')
        self.weightLable.setMinimumWidth(70)
        self.weightLable.setMargin(5)
        self.spacerWeight = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.weightText = QLineEdit(self)
        self.weightText.setObjectName(u"weightText")
        self.weightText.setMinimumWidth(100)
        self.weightText.setMaximumWidth(150)                
        #重量行布局
        self.weightLine.addWidget(self.weightLable)
        self.weightLine.addWidget(self.weightText)
        self.weightLine.addSpacerItem(self.spacerWeight)
        return self.weightLine
    
    #入库时间行
    def createOutDateLine(self): 
        #入库时间录入行组件创建      
        self.outDateLine = QHBoxLayout()
        self.outDateLine.setObjectName(u"outDateLine")
        self.outDateLable = QLabel(self)
        self.outDateLable.setObjectName(u"outDateLable")
        self.outDateLable.setText(u'入库日期:')
        self.outDateLable.setMinimumWidth(70)
        self.outDateLable.setMargin(5)
        self.spacerOutDate = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.today = datetime.date.today()
        self.outDateEdit = QDateEdit(QDate(self.today.year,self.today.month,self.today.day))
        self.outDateEdit.setCalendarPopup(True)
        self.outDateEdit.setObjectName(u"outDateEdit")
        self.outDateEdit.setMinimumWidth(100)
        self.outDateEdit.setMaximumWidth(150)             
        #重量行布局
        self.outDateLine.addWidget(self.outDateLable)
        self.outDateLine.addWidget(self.outDateEdit)
        self.outDateLine.addSpacerItem(self.spacerOutDate)
        return self.outDateLine
    
    #按钮区
    def createButtonLine(self): 
        #按钮行组件创建      
        self.buttonLine = QHBoxLayout()
        self.saveButton = QPushButton()
        self.saveButton.setObjectName(u'saveButton')
        self.saveButton.setText(u'保存')
        
        #按钮信号槽设置
        self.connect(self.saveButton, SIGNAL("clicked()"),self.testMess)
        
        #按钮行布局设置
        self.buttonLine.addStretch(1)
        self.buttonLine.addWidget(self.saveButton)
        self.buttonLine.addStretch(1)
        return self.buttonLine
    
    def testMess(self):
        QMessageBox.information(self,"Information",self.CustomText.text())        
        
    def refreshDate(self):
        pass
    
    def upDate(self):
        pass
    
    
        
# app = QApplication(sys.argv)
# ckd = UI_ckd()
# ckd.show()
# app.exec_()