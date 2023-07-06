from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *
import style
from interface.Widgets import UIinterface

class DisplayMemberView(UIinterface):

    updateUI2DB = utilsSignal["updateUI2DB"]
    delete2DB = utilsSignal["delete2DB"]

    def __init__(self, memberId):
       super().__init__()
       self.setWindowTitle("Member Details")
       self.setWindowIcon(QIcon("icons/icon.ico"))
       self.setGeometry(450, 150, 350, 600)
       self.setFixedSize(self.size())

       self.memberId = memberId
       self.UI()
       self.show()


    def UI(self):
        self.widgets()
        self.layouts()

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
        
        self.surnameEntry = QLineEdit()
        
        self.phoneEntry = QLineEdit()
        
        self.deleteBtn = QPushButton("Delete")
        self.deleteBtn.clicked.connect(self.deleteMember)
        self.updateBtn = QPushButton("Update")
        self.updateBtn.clicked.connect(self.updateMember)

    def setInitDatas(self, member):
        self.memberName = member[1]
        self.nameEntry.setText(self.memberName)
        self.memberSurName = member[2]
        self.surnameEntry.setText(self.memberSurName)
        self.memberPhone = member[3]
        self.phoneEntry.setText(self.memberPhone)
    

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

    def deleteMember(self):
        memberId = self.memberId

        mbox = QMessageBox.question(self, "Warning", "Are you sure you want to delete?", QMessageBox.Yes|QMessageBox.No)
        if mbox == QMessageBox.Yes:
            self.delete2DB.emit(memberId)

    def updateMember(self):
        memberId = self.memberId
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        if name and surname and phone != "":
            self.updateUI2DB.emit((name, surname, phone, memberId))
       
        else:
            QMessageBox.information(self, "Files Error", f"Fields empty")

