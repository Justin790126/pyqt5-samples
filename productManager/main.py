import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
import addmember, sellings
import style


from MainWindowView import MainWindowView
from MainWindowModel import MainWindowModel

from DisplayProduct.DisplayProductCtrller import DisplayProductCtrller
from DisplayMember.DisplayMemberCtrller import DisplayMemberCtrller
from AddProduct.AddProductCtrller import AddProductCtrller


class MainCtrller():
    def __init__(self):
        ################# view controllers #################
        self.mainWindowView = MainWindowView()
        self.mainWindowView.addProduct.triggered.connect(self.funcAddProduct)
        self.mainWindowView.addMember.triggered.connect(self.funcAddMember)
        self.mainWindowView.sellProduct.triggered.connect(self.funcSellProduct)
        self.mainWindowView.tabs.currentChanged.connect(self.tabChanged)
        self.mainWindowView.productsTable.doubleClicked.connect(self.mainWindowView.selectedProduct)
        self.mainWindowView.searchButton.clicked.connect(self.searchProduct)
        self.mainWindowView.listButton.clicked.connect(self.listProducts)
        self.mainWindowView.membersTable.doubleClicked.connect(self.mainWindowView.selectedMember)
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
        self.mainWindowView.showDisplayMemberWindow.connect(self.showDisplayMemberCtrller)

        
    def funcAddProduct(self):
        self.newProduct = AddProductCtrller()
        

    def funcAddMember(self):
        self.newMember = addmember.AddMember()

    def funcSellProduct(self):
        self.sell = sellings.SellProducts()

    
    def tabChanged(self):
        self.mainWindowModel.getStatistics()
        self.mainWindowModel.displayProducts()
        self.mainWindowModel.displayMembers()


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


    def showDisplayProductCtrller(self, event):
        self.displayProductCtrller = DisplayProductCtrller(event)

    def showDisplayMemberCtrller(self, event):
        self.displayMemberCtrller = DisplayMemberCtrller(event)



def main():
    App = QApplication(sys.argv)
    window = MainCtrller()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()