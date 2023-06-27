import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
from PIL import Image
import style

con=sqlite3.connect("products.db")
cur=con.cursor()

defaultImg = "store.png"

class SellProducts(QWidget):
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
        self.productCombo.currentIndexChanged.connect(self.changeComboValue)
        self.memberCombo = QComboBox()
        self.quantityCombo = QComboBox()
        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.sellProduct)

        ################################
        query1 = ("SELECT * FROM products WHERE product_availability=?")
        products = cur.execute(query1, ('Available',)).fetchall()
        
        query2= ("SELECT member_id,member_name FROM members")
        members = cur.execute(query2).fetchall()

        quantity = products[0][4]

        for product in products:
            self.productCombo.addItem(product[1], product[0])

        for member in members:
            self.memberCombo.addItem(member[1], member[0])

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

    def changeComboValue(self):
        self.quantityCombo.clear()
        product_id = self.productCombo.currentData()
        query = ("SELECT product_qouta FROM products WHERE product_id=?")
        qouta = cur.execute(query, (product_id,)).fetchone()
        
        for i in range(1, qouta[0]+1):
            self.quantityCombo.addItem(str(i))

    def sellProduct(self):
        global productName, productId, memberName, memberId, quantity
        productName = self.productCombo.currentText()
        productId = self.productCombo.currentData()
        memberName = self.memberCombo.currentText()
        memberId = self.memberCombo.currentData()
        quantity = int(self.quantityCombo.currentText())

        self.confirm = ConfirmWindow()
        self.close()


class ConfirmWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sell Prodcut")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450, 150, 350, 600)
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
        global productName, productId, memberName, memberId, quantity
        priceQUery=("SELECT product_price FROM products WHERE product_id =?")
        price = cur.execute(priceQUery, (productId,)).fetchone()
        self.amount = quantity * price[0]
        self.productName = QLabel()
        self.productName.setText(productName)
        self.memberName = QLabel()
        self.memberName.setText(memberName)
        self.amountName = QLabel()
        self.amountName.setText(f"{price[0]} x {quantity} = {self.amount}")
        self.confirmBtn = QPushButton("Confirm")
        self.confirmBtn.clicked.connect(self.confirm)
        

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
        global productName, productId, memberName, memberId, quantity
        try:
            sellQuery=("INSERT INTO 'sellings' (selling_product_id,selling_member_id,selling_quantity,selling_amount) VALUES (?,?,?,?)")
            cur.execute(sellQuery, (productId, memberId, quantity, self.amount))

            qoutaQuery=("SELECT product_qouta FROM products WHERE product_id=?")
            self.qouta = cur.execute(qoutaQuery, (productId,)).fetchone()

            if (quantity == self.qouta[0]):
                updateQoutaQuery = ("UPDATE products set product_qouta=?, product_availability=? WHERE product_id=?")
                cur.execute(updateQoutaQuery, (0, "UnAvailable", productId))
                con.commit()
            else:
                newQouta = self.qouta[0] - quantity
                updateQoutaQuery = ("UPDATE products set product_qouta=? WHERE product_id=?")
                cur.execute(updateQoutaQuery, (newQouta, productId))
                con.commit()

            
            QMessageBox.information(self,"Info", "Confirm product purchased!")
        except Exception as e:
            QMessageBox.information(self,"Error", f"Error confirm: {e}")

        
        