import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
import addproduct, addmember, sellings, style
from PIL import Image
from interface.Widgets import UIinterface

from utils.db import *
class DisplayProductView(QWidget):

    updateUI2DB = utilsSignal["updateUI2DB"]
    delete2DB = utilsSignal["delete2DB"]

    def __init__(self, productId):
        super().__init__()
        self.productId = productId
        
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450,150,350,600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()


    def UI(self):
        # self.prepareDatas()
        self.widgets()
        self.layouts()


    def widgets(self):
        self.product_Img = QLabel()
        self.product_Img.setAlignment(Qt.AlignCenter)

        self.titleText = QLabel("Update Product")
        self.titleText.setAlignment(Qt.AlignCenter)

        ################################

        self.nameEntry = QLineEdit()
        self.manufacturerEntry = QLineEdit()
       
        self.priceEntry = QLineEdit()
        self.qoutaEntry = QLineEdit()
       
        self.availabilityCombo = QComboBox()
        self.availabilityCombo.addItems(["Available", "UnAvailable"])
        self.uploadBtn = QPushButton("Upload")
        self.deleteBtn = QPushButton("Delete")
        self.updateBtn = QPushButton("Update")
        
    def setInitDatas(self, event):
        product = event
        self.productName = product[1]
        self.productManufacturer = product[2]
        self.productPrice = product[3]
        self.productQouta = product[4]
        self.productImg = product[5]
        self.productStatus = product[6]

        self.img = QPixmap("img/{}".format(self.productImg))
        self.product_Img.setPixmap(self.img)
        self.nameEntry.setText(self.productName)
        self.manufacturerEntry.setText(self.productManufacturer)
        self.priceEntry.setText(str(self.productPrice))
        self.qoutaEntry.setText(str(self.productQouta))


    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.topFrame.setStyleSheet(style.productTopFrame())
        self.bottomFrame = QFrame()
        self.bottomFrame.setStyleSheet(style.productBottomFrame())

        ################################

        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.product_Img)
        self.topFrame.setLayout(self.topLayout)

        ################################

        self.bottomLayout.addRow(QLabel("Name: "), self.nameEntry)
        self.bottomLayout.addRow(QLabel("Manufacturer: "), self.manufacturerEntry)
        self.bottomLayout.addRow(QLabel("Price: "), self.priceEntry)
        self.bottomLayout.addRow(QLabel("Qouta: "), self.qoutaEntry)
        self.bottomLayout.addRow(QLabel("Status: "), self.availabilityCombo)
        self.bottomLayout.addRow(QLabel("Image: "), self.uploadBtn)
        self.bottomLayout.addRow(QLabel(""), self.deleteBtn)
        self.bottomLayout.addRow(QLabel(""), self.updateBtn)



        self.bottomFrame.setLayout(self.bottomLayout)

        ################################

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        ################################
        self.setLayout(self.mainLayout)
    
    def uploadImg(self):
        size=(256,256)
        self.filename,ok = QFileDialog.getOpenFileName(self, "Upload Image", '', 'Image files (*.jpg *.png)')

        if ok:
            self.productImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img_upload/{}".format(self.productImg))


    def getUpdateProductArgs(self):
        productId=self.productId
        name = self.nameEntry.text()
        manufacturer = self.manufacturerEntry.text()
        price = int(self.priceEntry.text())
        qouta = int(self.qoutaEntry.text())
        status = self.availabilityCombo.currentText()
        defaultImg = self.productImg

        return (name,manufacturer,price,qouta,defaultImg,status,productId)

    def updateProduct(self):
        productId=self.productId
        name = self.nameEntry.text()
        manufacturer = self.manufacturerEntry.text()
        price = int(self.priceEntry.text())
        qouta = int(self.qoutaEntry.text())
        status = self.availabilityCombo.currentText()
        defaultImg = self.productImg
        

        if name and manufacturer and price and qouta != "":
            queryArgs = (name,manufacturer,price,qouta,defaultImg,status,productId)
            self.updateUI2DB.emit(queryArgs)
        else:
            self.showUpdateDBresult(("Info", "Files should not be empty"))

    def showUpdateDBresult(self, title_content):
        QMessageBox.information(self, title_content[0], title_content[1])
        if "close" in title_content:
            self.close()

    def deleteProduct(self):
        productId=self.productId

        mbox = QMessageBox.question(self, "Warning", "Are you sure you want to delete?", QMessageBox.Yes|QMessageBox.No)
        if mbox == QMessageBox.Yes:
            self.delete2DB.emit(productId)
