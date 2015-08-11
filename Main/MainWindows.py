# encoding: utf-8
'''
Created on 2015年8月4日

@author: hedge31
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Form import rkdForm,ckdForm
from Control import meteData

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.setWindowTitle(self.tr('冷库出库系统'))
        self.resize(600,400)
        self.createAction()
        self.createMenu()
        
    def createAction(self):
        #入库单动作连接
        self.rkd = QAction(u'入库单',self)
        self.connect(self.rkd, SIGNAL("triggered()"),self.loadrkdForm)
        #退出动作连接
        self.close = QAction(u'退出',self)
        self.connect(self.close, SIGNAL("triggered()"),SLOT(u'close()'))
        
        
        #出库单动作
        self.ckd = QAction(u'出库单',self)
        self.connect(self.ckd, SIGNAL("triggered()"),self.loadckdForm)
        
        #数据库初始化
        self.initDataBase = QAction(u'初始化数据库',self)
        self.connect(self.initDataBase, SIGNAL("triggered()"),meteData.meteData)
            
    def createMenu(self):
        startMenu = self.menuBar().addMenu(u'开始')
        startMenu.addAction(self.rkd)
        startMenu.addAction(self.ckd)
        startMenu.addAction(self.close)
        settingMenu = self.menuBar().addMenu(u'设置')
        settingMenu.addAction(self.initDataBase)
        
    def loadrkdForm(self):
        rkdWidget = rkdForm.UI_rkd(self)
        rkdWidget.resize(self.size())
        self.setCentralWidget(rkdWidget)  
        
    
    def loadckdForm(self):
        ckdWidget = ckdForm.UI_ckd(self)
        ckdWidget.resize(self.size())
        self.setCentralWidget(ckdWidget)
        self.setContentsMargins(20, 20, 20, 20)
        
        
    def testMess(self):
        QMessageBox.information(self,"Information",u"连接成功！")  
        
        
if __name__ == '__main__':
    app=QApplication(sys.argv)  
    main=MainWindow()  
    main.show()
    app.exec_()  