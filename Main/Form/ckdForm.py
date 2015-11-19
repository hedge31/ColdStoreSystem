# encoding: utf-8
'''
Created on 2015年8月5日

@author: hedge31
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Control import rkdOperate
from Main.Form.ckdFindForm import ckdFindForm
class UI_ckd(QWidget):
    def __init__(self,parent = None):
        super(UI_ckd,self).__init__(parent)
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
        findForm = rkdFindForm(self)
        findForm.exec_() 



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