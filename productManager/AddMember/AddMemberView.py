from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *
from interface.Widgets import UIinterface



class AddMemberView(UIinterface):

    add2DB = utilsSignal["add2DB"]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.addMemberImg = QLabel()
        self.img = QPixmap(("icons/addmember.png"))
        self.addMemberImg.setPixmap(self.img)
        self.addMemberImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Add Member")
        self.titleText.setAlignment(Qt.AlignCenter)

        ################################################################
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter name of member")

        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter surname of member")

        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter phone number")

        self.submitBtn = QPushButton("Submit")

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        self.topFrame = QFrame()
        self.bottomFrame = QFrame()
        ################# add widgets to layout #################


        #### top frame ####
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.addMemberImg)
        self.topFrame.setLayout(self.topLayout)
        #### bottom frame ####
        self.bottomLayout.addRow(QLabel("Name: "), self.nameEntry)
        self.bottomLayout.addRow(QLabel("SurName: "), self.surnameEntry)
        self.bottomLayout.addRow(QLabel("Phone: "), self.phoneEntry)
        self.bottomLayout.addRow(QLabel(""), self.submitBtn)
        self.bottomFrame.setLayout(self.bottomLayout)
        #### add frames to mainLayout ####
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)

    def clearText(self):
        self.nameEntry.setText("")
        self.surnameEntry.setText("")
        self.phoneEntry.setText("")

    def addMember(self):
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()

        if name and surname and phone != "":
            self.add2DB.emit((name, surname, phone))
            
        else:
            QMessageBox.information(self, "Add Member Failure", "Files can not be empty")
   
    def closeEvent(self, event):
        pass
