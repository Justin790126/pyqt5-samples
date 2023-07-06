import os,sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *
import style
#import style
#from PIL import Image
from interface.Widgets import UIinterface
########## import utils here ##########

class ConfirmWindowView(UIinterface):

    ########## #add custom signal here ##########
    reqUpdateProductSelling2DB = pyqtSignal(tuple)

    def __init__(self, ppmmq):
        super().__init__()
        self.productInfo = ppmmq
        self.setWindowTitle("Window Title here")
        #self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()


    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.titleText = QLabel("Sell Product")
        self.titleText.setAlignment(Qt.AlignCenter)
        self.titleImg = QLabel()
        self.img = QPixmap("icons/shop.png")
        self.titleImg.setPixmap(self.img)
        self.titleImg.setAlignment(Qt.AlignCenter)
        ################################
        productName = self.productInfo[0]
        productId = self.productInfo[1]
        memberName = self.productInfo[2]
        memberId = self.productInfo[3]
        quantity = int(self.productInfo[4])

  
        self.productName = QLabel()
        self.productName.setText(productName)
        self.memberName = QLabel()
        self.memberName.setText(memberName)
        self.amountName = QLabel()
        
        self.confirmBtn = QPushButton("Confirm")
        
        
    def updateUIofPrice(self, price):
        quantity = int(self.productInfo[4])
        self.amount = quantity * price
        self.amountName.setText(f"{price} x {quantity} = {self.amount}")
        

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.topFrame.setStyleSheet(style.sellProductTopFrame())
        self.bottomFrame = QFrame()
        self.bottomFrame.setStyleSheet(style.sellProductBottomFrame())
        ################################
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.titleImg)
        self.topFrame.setLayout(self.topLayout)
        ################################
        self.bottomLayout.addRow(QLabel("Product: "), self.productName)
        self.bottomLayout.addRow(QLabel("Member: "), self.memberName)
        self.bottomLayout.addRow(QLabel("Amount: "), self.amountName)
        self.bottomLayout.addRow(QLabel(""), self.confirmBtn)
        self.bottomFrame.setLayout(self.bottomLayout)


        ################################
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)

    def confirm(self):
        self.reqUpdateProductSelling2DB.emit(self.productInfo+(self.amount,))
        
        

    def closeEvent(self, event):
        pass


