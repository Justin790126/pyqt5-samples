import os,sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import style
from utils.db import *
#from PIL import Image
#from interface.Widgets import UIinterface
########## import utils here ##########


class SellingsView(QWidget):
    ########## #add custom signal here ##########
    customSignal = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sell Products")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450, 150, 350, 600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.sellProductImg = QLabel()
        self.img =QPixmap("icons/shop.png")
        self.sellProductImg.setPixmap(self.img)
        self.sellProductImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Sell Products")
        self.titleText.setAlignment(Qt.AlignCenter)

        ################################

        self.productCombo = QComboBox()
        
        self.memberCombo = QComboBox()
        self.quantityCombo = QComboBox()
        self.submitBtn = QPushButton("Submit")
        
        ################################


    def updateMembersUI(self, members):
        for member in members:
            self.memberCombo.addItem(member[1], member[0])


    def updateProductsUI(self, products):
        for product in products:
            self.productCombo.addItem(product[1], product[0])

        quantity = products[0][4]
        for i in range(1,quantity+1):
            self.quantityCombo.addItem(str(i))

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
        self.topLayout.addWidget(self.sellProductImg)
        self.topFrame.setLayout(self.topLayout)

        ################################

        self.bottomLayout.addRow(QLabel("Products: "), self.productCombo)
        self.bottomLayout.addRow(QLabel("Memebers: "), self.memberCombo)
        self.bottomLayout.addRow(QLabel("Quantity: "), self.quantityCombo)
        self.bottomLayout.addRow(QLabel(""), self.submitBtn)

        self.bottomFrame.setLayout(self.bottomLayout)

        ################################
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)


        
    def updateQoutCombo(self, qouta):
        self.quantityCombo.clear()
        for i in range(1, qouta+1):
            self.quantityCombo.addItem(str(i))

    def getSellProduct(self):
        productName = self.productCombo.currentText()
        productId = self.productCombo.currentData()
        memberName = self.memberCombo.currentText()
        memberId = self.memberCombo.currentData()
        quantity = int(self.quantityCombo.currentText())

        return (productName, productId, memberName, memberId, quantity)

        # self.confirm = ConfirmWindow()
        # self.close()

    