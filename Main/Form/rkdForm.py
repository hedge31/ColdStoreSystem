# encoding: utf-8
'''
Created on 2015年8月4日

@author: hedge31

入库单的界面
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Control import rkdOperate
class UI_rkd(QWidget):
    def __init__(self,parent = None):
        super(UI_rkd,self).__init__(parent)
        self.resize(200,200)
        self.setGeometry(QRect(20, 20, 246, 141))
        self.setMinimumSize(200, 200)
        self.RkdInput = QVBoxLayout(self)
        self.setContentsMargins(20, 5, 20, 20)
        self.RkdInput.setMargin(5)
        self.RkdInput.setObjectName(u"RkdInput")
        
       
        #表单标头
        self.formTitle = QLabel(self)
        self.formTitle.setText(u'入库单')
        self.formTitle.setFont(QFont(u'微软雅黑',20))
        self.formTitle.setMargin(5)
        self.RkdInput.addWidget(self.formTitle)
        
        #入库单主布局设置
        self.RkdInput.addLayout(self.createRKDDocNoLine())
        self.RkdInput.addLayout(self.createCustomLine())
        self.RkdInput.addLayout(self.createItemLine())
        self.RkdInput.addLayout(self.createWeightLine())
        self.RkdInput.addLayout(self.createInDateLine())
        self.RkdInput.addLayout(self.createStockLine())
        self.RkdInput.addStretch()
        
        #主界面添加布局
        self.setLayout(self.RkdInput)
        
        #添加Action
        self.createAction()
        #添加ToolBar
        self.createToolBar(parent)
    
    def createRKDDocNoLine(self):
        self.rkdDocNoLine = QHBoxLayout()
        self.rkdDocNoLine.setObjectName(u"rkdDocNOLine")
        self.rkdDocNoLable = QLabel(self)
        self.rkdDocNoLable.setObjectName(u"rkdDocNOLable")
        self.rkdDocNoLable.setText(u'入库单号:')
        self.rkdDocNoLable.setMinimumWidth(70)
        self.rkdDocNoLable.setMargin(5)
        self.spacerCustom = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.rkdDocNoText = QLineEdit(self)
        self.rkdDocNoText.setObjectName(u"CustomText")
        self.rkdDocNoText.setReadOnly(True)
        self.rkdDocNoText.setText(u'自动编号')
        self.rkdDocNoText.setMinimumWidth(100)
        self.rkdDocNoText.setMaximumWidth(150)    
        #客户行布局
        self.rkdDocNoLine.addWidget(self.rkdDocNoLable)
        self.rkdDocNoLine.addWidget(self.rkdDocNoText)
        self.rkdDocNoLine.addSpacerItem(self.spacerCustom)
        return self.rkdDocNoLine
        
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
        self.ItemLable.setText(u'料品规格:')
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
    def createInDateLine(self): 
        #入库时间录入行组件创建      
        self.inDateLine = QHBoxLayout()
        self.inDateLine.setObjectName(u"inDateLine")
        self.inDateLable = QLabel(self)
        self.inDateLable.setObjectName(u"inDateLable")
        self.inDateLable.setText(u'入库日期:')
        self.inDateLable.setMinimumWidth(70)
        self.inDateLable.setMargin(5)
        self.spacerInDate = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.inDateEdit = QDateEdit(QDate().currentDate())
        self.inDateEdit.setDate(QDate().currentDate())
        self.inDateEdit.setCalendarPopup(True)
        self.inDateEdit.setObjectName(u"inDateEdit")
        self.inDateEdit.setMinimumWidth(100)
        self.inDateEdit.setMaximumWidth(150)             
        #重量行布局
        self.inDateLine.addWidget(self.inDateLable)
        self.inDateLine.addWidget(self.inDateEdit)
        self.inDateLine.addSpacerItem(self.spacerInDate)
        return self.inDateLine
    
    def createStockLine(self):
        self.stockLine = QHBoxLayout()
        self.stockLine.setObjectName(u"stockLine")
        self.stockLable = QLabel(self)
        self.stockLable.setObjectName(u"stockLable")
        self.stockLable.setText(u'余量:')
        self.stockLable.setMinimumWidth(70)
        self.stockLable.setMargin(5)
        self.spacerStock = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.stockText = QLineEdit(self)
        self.stockText.setObjectName(u"stockText")
        self.stockText.setReadOnly(True)
        self.stockText.setMinimumWidth(100)
        self.stockText.setMaximumWidth(150)                
        #重量行布局
        self.stockLine.addWidget(self.stockLable)
        self.stockLine.addWidget(self.stockText)
        self.stockLine.addSpacerItem(self.spacerStock)
        return self.stockLine
    
    
    
    #入库单的ToolBar
    def createToolBar(self,parent):
        self.fileToolBar = parent.addToolBar("Form")
        self.fileToolBar.setMovable(False)
        self.fileToolBar.setFloatable(False)
        self.fileToolBar.addAction(self.newFormAction)
        self.fileToolBar.addAction(self.updateFormAction) 
        self.fileToolBar.addAction(self.deleteFormAction)
        self.fileToolBar.addAction(self.findFormAction)
        
    
    #添加动作
    def createAction(self):
        self.newFormAction = QAction(u'新增',self)
        self.connect(self.newFormAction, SIGNAL("triggered()"),self.clearForm)
        self.updateFormAction = QAction(u'保存',self)
        self.connect(self.updateFormAction, SIGNAL("triggered()"),self.updateForm)
        self.deleteFormAction = QAction(u'删除',self)
        self.connect(self.deleteFormAction, SIGNAL("triggered()"),self.deleteForm)
        self.findFormAction = QAction(u'查找',self)
        self.connect(self.findFormAction, SIGNAL("triggered()"),self.findForm)
             
    def updateForm(self):
        return rkdOperate.updateRkd(self)
            
    def deleteForm(self):
        return rkdOperate.deleteRkd(self)
    
    def clearForm(self):
        return rkdOperate.clearRkd(self)
    
    def findForm(self):
        self.findRkdDialog = QDialog(self)
        self.findRkdDialog.setWindowTitle(u'查找')
        self.findDialogLayout = QGridLayout(self.findRkdDialog)
        self.findDialogLayout.setContentsMargins(20, 5, 20, 5)
        self.findargv = [(u'docno',u'入库单号'),(u'custom',u'客户'),(u'Item',u'料品规格')]
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
            temp = QLineEdit(self)
            temp.setObjectName(u'find'+line[0])
            temp.setMinimumWidth(100)
            temp.setMaximumWidth(150)
            self.findDialogLayout.addWidget(self.findChild(QLineEdit,u'find'+line[0]),row,col)
            col +=1
        
        self.findButton = QPushButton(self)
        self.findButton.setText(u'查找')
        self.findDialogLayout.addWidget(self.findButton,row+1,3)
        
        
        self.findRkdDialog.setLayout(self.findDialogLayout)

        self.findRkdDialog.exec_()
# app = QApplication(sys.argv)
# rkd = UI_rkd()
# rkd.show()
# app.exec_()