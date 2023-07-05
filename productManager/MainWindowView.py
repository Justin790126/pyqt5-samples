import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import style
from utils.db import *

class MainWindowView(QMainWindow):

    displayProductsInit = pyqtSignal()
    displayMembersInit = pyqtSignal()
    showDisplayProductWindow = pyqtSignal(int)
    showDisplayMemberWindow = pyqtSignal(int)


    def __init__(self):

        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450, 150, 1350, 750)
        self.setFixedSize(self.size())
        self.UI()
        self.show()


    def UI(self):
        self.toolBar()
        self.tabWidget()
        self.widgets()
        self.layouts()

    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ################ Toolbar buttons################################

        ################### add product #####################
        self.addProduct = QAction(QIcon("icons/add.png"), "Add Product", self)
        self.tb.addAction(self.addProduct)
        self.tb.addSeparator()
        ########### add member #####################
        self.addMember = QAction(QIcon("icons/users.png"), "Add Member", self)
        self.tb.addAction(self.addMember)

        self.tb.addSeparator()
        ################# sell products #####################
        self.sellProduct = QAction(
            QIcon("icons/sell.png"), "Sell Product", self)
        self.tb.addAction(self.sellProduct)

        self.tb.addSeparator()

    def tabWidget(self):
        self.tabs = QTabWidget()
        self.tabs.blockSignals(True)

        self.setCentralWidget(self.tabs)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")

    def widgets(self):
        ################ Tab1 widgets #################
        ############### Main left layout widget #################
        self.productsTable = QTableWidget()
        self.productsTable.setColumnCount(6)
        self.productsTable.setColumnHidden(0, True)
        self.productsTable.setHorizontalHeaderItem(
            0, QTableWidgetItem("Product Id"))
        self.productsTable.setHorizontalHeaderItem(
            1, QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(
            2, QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(
            3, QTableWidgetItem("Price"))
        self.productsTable.setHorizontalHeaderItem(
            4, QTableWidgetItem("Qouta"))
        self.productsTable.setHorizontalHeaderItem(
            5, QTableWidgetItem("Availability"))
        self.productsTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.productsTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        ############### Right top layout widgets #################
        self.searchText = QLabel("Search")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Search For Products")
        self.searchButton = QPushButton("Search")

        self.searchButton.setStyleSheet(style.searchButtonStyle())
        ################ Right middle layout widgets #################
        self.allProducts = QRadioButton("All Products")
        self.availableProducts = QRadioButton("Available")
        self.notAvailableProducts = QRadioButton("Not Available")
        self.listButton = QPushButton("List")

        self.listButton.setStyleSheet(style.listButtonStyle())
        ################# Tab2 widgets  #################
        self.membersTable = QTableWidget()
        self.membersTable.setColumnCount(4)
        self.membersTable.setHorizontalHeaderItem(
            0, QTableWidgetItem("Member ID"))
        self.membersTable.setHorizontalHeaderItem(
            1, QTableWidgetItem("Member Name"))
        self.membersTable.setHorizontalHeaderItem(
            2, QTableWidgetItem("Member Surname"))
        self.membersTable.setHorizontalHeaderItem(3, QTableWidgetItem("Phone"))
        self.membersTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.membersTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.membersTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)

        self.memberSearchText = QLabel("Search Members")
        self.memberSearchEntry = QLineEdit()
        self.memberSearchButton = QPushButton("Search For Members")

        #################### tab3 widgets #################
        self.totalProductsLabel = QLabel()
        self.totalMemberLabel = QLabel()
        self.soldProductsLabel = QLabel()
        self.totalAmountLabel = QLabel()

    def layouts(self):
        ########## tab1 layout ##########
        self.mainLayout = QHBoxLayout()
        self.mainLeftLayout = QVBoxLayout()
        self.mainRightLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightMiddleLayout = QHBoxLayout()
        self.topGroupBox = QGroupBox("Search Box")
        self.topGroupBox.setStyleSheet(style.searchBoxStyle())
        self.middleGroupBox = QGroupBox("List Box")
        self.middleGroupBox.setStyleSheet(style.listBoxStyle())
        self.bottomGroupBox = QGroupBox("")
        ########### Add widgets ############
        ######### left main layout ###########
        self.mainLeftLayout.addWidget(self.productsTable)

        ########### right top layout #########
        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchButton)
        self.topGroupBox.setLayout(self.rightTopLayout)
        ############### right middle layout #########
        self.rightMiddleLayout.addWidget(self.allProducts)
        self.rightMiddleLayout.addWidget(self.availableProducts)
        self.rightMiddleLayout.addWidget(self.notAvailableProducts)
        self.rightMiddleLayout.addWidget(self.listButton)
        self.middleGroupBox.setLayout(self.rightMiddleLayout)

        self.mainRightLayout.addWidget(self.topGroupBox, 20)
        self.mainRightLayout.addWidget(self.middleGroupBox, 20)
        self.mainRightLayout.addWidget(self.bottomGroupBox, 60)

        self.mainLayout.addLayout(self.mainLeftLayout, 70)
        self.mainLayout.addLayout(self.mainRightLayout, 30)
        self.tab1.setLayout(self.mainLayout)

        ################### tab2 layout################
        self.memberMainLayout = QHBoxLayout()
        self.memberLeftLayout = QHBoxLayout()
        self.memberRightLayout = QHBoxLayout()
        self.memberRightGroupBox = QGroupBox("Search For Members")
        self.memberRightGroupBox.setContentsMargins(10, 10,  10, 520)

        self.memberRightLayout.addWidget(self.memberSearchText)
        self.memberRightLayout.addWidget(self.memberSearchEntry)
        self.memberRightLayout.addWidget(self.memberSearchButton)
        self.memberRightGroupBox.setLayout(self.memberRightLayout)

        self.memberLeftLayout.addWidget(self.membersTable)
        self.memberMainLayout.addLayout(self.memberLeftLayout, 70)
        self.memberMainLayout.addWidget(self.memberRightGroupBox, 30)
        self.tab2.setLayout(self.memberMainLayout)

        ##################### tab3 layout #################

        self.statisticsMainLayout = QVBoxLayout()
        self.statisticsLayout = QFormLayout()
        self.statisticsLayout.addRow(
            QLabel("Total Products: "), self.totalProductsLabel)
        self.statisticsLayout.addRow(
            QLabel("Total Member: "), self.totalMemberLabel)
        self.statisticsLayout.addRow(
            QLabel("Sold Products: "), self.soldProductsLabel)
        self.statisticsLayout.addRow(
            QLabel("Total Amount: "), self.totalAmountLabel)

        self.statisticsGroupBox = QGroupBox("Statistics")
        self.statisticsGroupBox.setFont(QFont("Arial", 20))
        self.statisticsGroupBox.setLayout(self.statisticsLayout)
        self.statisticsMainLayout.addWidget(self.statisticsGroupBox)
        self.tab3.setLayout(self.statisticsMainLayout)
        self.tabs.blockSignals(False)

    ############### ctrller-trigger-view-to-model #####


    def selectedProduct(self):
        global productId

        listProduct = []
        for i in range(0, 6):
            listProduct.append(self.productsTable.item(
                self.productsTable.currentRow(), i).text())

        productId = int(listProduct[0])
        self.showDisplayProductWindow.emit(productId)


    def selectedMember(self):
        global memberId
        listMember = []
        for i in range(0, 4):
            listMember.append(self.membersTable.item(
                self.membersTable.currentRow(), i).text())
        memberId = int(listMember[0])

        self.showDisplayMemberWindow.emit(memberId)


    ######################### Model emit event handler ############################

    def statisticPageChangeUI(self, event):
        self.totalProductsLabel.setText(str(event["countProducts"]))
        self.totalMemberLabel.setText(str(event["countMembers"]))
        self.soldProductsLabel.setText(str(event["soldProducts"]))
        self.totalAmountLabel.setText("{} $".format(event["totalAmount"]))

    def productsPageChangeUI(self, data):
        self.productsTable.setFont(QFont('Times', 12))
        for i in reversed(range(self.productsTable.rowCount())):
            self.productsTable.removeRow(i)

        query = data
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def membersPageChangeUI(self, event):
        self.productsTable.setFont(QFont('Times', 12))
        self.membersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in reversed(range(self.membersTable.rowCount())):
            self.membersTable.removeRow(i)

        query = event
        for row_data in query:
            row_number = self.membersTable.rowCount()
            self.membersTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.membersTable.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))

    def searchMembersPageChangeUI(self, event):
        print(event)
        results = event
        if results == []:
            QMessageBox.information(
                self, "Warning", "There is no such a member")

            self.displayMembersInit.emit()
        else:
            for i in reversed(range(self.membersTable.rowCount())):
                self.membersTable.removeRow(i)

            for row_data in results:
                row_number = self.membersTable.rowCount()
                self.membersTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.membersTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

    def searchProductPageChangeUI(self, event):
        results = event
        if results == []:
            QMessageBox.information(
                self, "Warning", "There is no such a product or manufacturer")

            self.displayProductsInit.emit()
            
        else:
            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in results:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))


    def productsAvailabiltyPageChangeUI(self, event):
        products = event
        if products == []:
            QMessageBox.information(
                self, "Warning", "There is no prodcut available")
        else:
            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))
