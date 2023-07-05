import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
import addproduct, addmember, sellings, style
from PIL import Image
from interface.Widgets import UIinterface
from MainWindowView import MainWindowView
from MainWindowModel import MainWindowModel

from DisplayProduct.DisplayProductCtrller import DisplayProductCtrller


con=sqlite3.connect("products.db")
cur=con.cursor()

class MainCtrller():
    def __init__(self):
        ################# view controllers #################
        self.mainWindowView = MainWindowView()
        self.mainWindowView.addProduct.triggered.connect(self.funcAddProduct)
        self.mainWindowView.addMember.triggered.connect(self.funcAddMember)
        self.mainWindowView.sellProduct.triggered.connect(self.funcSellProduct)
        self.mainWindowView.tabs.currentChanged.connect(self.tabChanged)
        self.mainWindowView.productsTable.doubleClicked.connect(self.selectedProduct)
        self.mainWindowView.searchButton.clicked.connect(self.searchProduct)
        self.mainWindowView.listButton.clicked.connect(self.listProducts)
        self.mainWindowView.membersTable.doubleClicked.connect(self.selectedMember)
        self.mainWindowView.memberSearchButton.clicked.connect(self.searchMembers)
        

        ################# model controllers #################
        self.mainWindowModel = MainWindowModel()
        self.mainWindowModel.searchProductsGot.connect(
            self.mainWindowView.searchProductPageChangeUI)
        self.mainWindowModel.searchMembersGot.connect(
            self.mainWindowView.searchMembersPageChangeUI)
        self.mainWindowModel.statisticDataChanged.connect(
            self.mainWindowView.statisticPageChangeUI)
        self.mainWindowModel.productsDataChanged.connect(
            self.mainWindowView.productsPageChangeUI)
        self.mainWindowModel.membersDataChanged.connect(
            self.mainWindowView.membersPageChangeUI)
        self.mainWindowModel.productsAvailabiltyGot.connect(
            self.mainWindowView.productsAvailabiltyPageChangeUI)
        self.tabChanged()


        ################ interchange controller & view event #################################
        self.mainWindowView.displayProductsInit.connect(self.mainWindowModel.displayProducts)
        self.mainWindowView.displayMembersInit.connect(self.mainWindowModel.displayMembers)
        self.mainWindowView.showDisplayProductWindow.connect(self.showDisplayProductCtrller)

    

        
    def funcAddProduct(self):
        self.newProduct = addproduct.AddProduct()

    def funcAddMember(self):
        self.newMember = addmember.AddMember()

    def funcSellProduct(self):
        self.sell = sellings.SellProducts()

    
    def tabChanged(self):
        self.mainWindowModel.getStatistics()
        self.mainWindowModel.displayProducts()
        self.mainWindowModel.displayMembers()

    def selectedProduct(self):
        self.mainWindowView.selectedProduct()

    def searchProduct(self):
        value = self.mainWindowView.searchEntry.text()
        self.mainWindowModel.searchProduct(value)


    def searchMembers(self):
        value = self.mainWindowView.memberSearchEntry.text()
        self.mainWindowModel.searchMembers(value)



    def listProducts(self):
        if self.mainWindowView.allProducts.isChecked() == True:
            self.mainWindowModel.displayProducts()
            return

        if self.mainWindowView.notAvailableProducts.isChecked() == True:
            self.mainWindowModel.listProductBy(False)
        elif self.mainWindowView.availableProducts.isChecked() == True:
            self.mainWindowModel.listProductBy(True)


    def selectedMember(self):
        global memberId
        listMember = []
        for i in range(0, 4):
            listMember.append(self.mainWindowView.membersTable.item(
                self.mainWindowView.membersTable.currentRow(), i).text())
        memberId = int(listMember[0])

        self.displayMember = DisplayMember()

    def showDisplayProductCtrller(self, event):
        self.displayProductCtrller = DisplayProductCtrller(event)


class DisplayMember(UIinterface):
    def __init__(self):
       super().__init__()
       self.setWindowTitle("Member Details")
       self.setWindowIcon(QIcon("icons/icon.ico"))
       self.setGeometry(450, 150, 350, 600)
       self.setFixedSize(self.size())
       self.show()

    def widgets(self):
        ################################
        self.memberImg = QLabel()
        self.img = QPixmap("icons/members.png")
        self.memberImg.setPixmap(self.img)
        self.memberImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Display Member")
        self.titleText.setAlignment(Qt.AlignCenter)
        ################################
        
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.memberName)
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setText(self.memberSurName)
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setText(self.memberPhone)
        self.deleteBtn = QPushButton("Delete")
        self.deleteBtn.clicked.connect(self.deleteMember)
        self.updateBtn = QPushButton("Update")
        self.updateBtn.clicked.connect(self.updateMember)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.topFrame.setStyleSheet(style.memberTopFrame())
        self.bottomFrame = QFrame()
        self.bottomFrame.setStyleSheet(style.memberBottomFrame())

        ################################

        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.memberImg)

        self.topFrame.setLayout(self.topLayout)

        ################################

        self.bottomLayout.addRow(QLabel("Name: "), self.nameEntry)
        self.bottomLayout.addRow(QLabel("SurName: "), self.surnameEntry)
        self.bottomLayout.addRow(QLabel("Phone: "), self.phoneEntry)
        self.bottomLayout.addRow(QLabel(""), self.updateBtn)
        self.bottomLayout.addRow(QLabel(""), self.deleteBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        ################################

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)
        
    def prepareDatas(self):
        global memberId
        query = "SELECT * FROM members WHERE member_id=?"
        member = cur.execute(query, (memberId,)).fetchone()

        self.memberName = member[1]
        self.memberSurName = member[2]
        self.memberPhone = member[3]

    def deleteMember(self):
        global memberId

        mbox = QMessageBox.question(self, "Warning", "Are you sure you want to delete?", QMessageBox.Yes|QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cur.execute("DELETE FROM members WHERE member_id=?", (memberId,))
                con.commit()
                QMessageBox.information(self, "Delete Successful", "Member has been deleted")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Delete Fail", f"Delete Error: {e}")

    def updateMember(self):
        global memberId
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        if name and surname and phone != "":
            try:
                query = "UPDATE members set member_name=?, member_surname=?,member_phone=? WHERE member_id=?"
                cur.execute(query, (name, surname, phone, memberId))
                con.commit()
                QMessageBox.information(self, "Update Success", "member has been updated")
            except Exception as e:
                QMessageBox.information(self, "Update Error", f"Error: {e}")
        else:
            QMessageBox.information(self, "Files Error", f"Fields empty")




def main():
    App = QApplication(sys.argv)
    window = MainCtrller()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()