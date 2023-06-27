import typing
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
import sys, os
import sqlite3
from PIL import Image
from PyQt5.QtWidgets import QWidget

con = sqlite3.connect('employees.db')
cur = con.cursor()
defaultImg= "person.png"
person_id=None

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My EMployees")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getEmployees()
        self.displayFirstRecord()
    
    def mainDesign(self):
        self.setStyleSheet("font-size: 14pt; font-weight: Arial Bold")
        self.employeeList = QListWidget()
        self.employeeList.itemClicked.connect(self.singleClick)
        self.btnNew = QPushButton("New")
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate = QPushButton("Update")
        self.btnUpdate.clicked.connect(self.updateEmployee)
        self.btnDelete = QPushButton("Delete")
        self.btnDelete.clicked.connect(self.deleteEmployee)

    def deleteEmployee(self):
        if self.employeeList.selectedItems():
            person = self.employeeList.currentItem().text()
            id = person.split('-')[0]
            mbox = QMessageBox.question(self, "Warning", "Are you sure you want to delete this person?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM employees WHERE id=?"
                    cur.execute(query, (id,))
                    con.commit()
                    mbox = QMessageBox.information(self, "Info", "Person had deleted")
                    self.close()
                    self.main=Main()
                except Exception as e:
                    mbox = QMessageBox.information(self, "Error", f"Delete Fail: {e}")
        else:
            QMessageBox.information(self, "Warning", "Please select a person to delete")          

    def addEmployee(self):
        self.newEmployee = AddEmployee()
        self.close()

    def getEmployees(self):
        query="SELECT id,name,surname FROM employees"
        employees = cur.execute(query).fetchall()
        for employee in employees:
            self.employeeList.addItem(
                f"{str(employee[0])}-{str(employee[1])} {str(employee[2])}")
            

    def showPersonOnLeftUI(self, employee):
        img=QLabel()
        img.setPixmap(QPixmap(f"images/{employee[5]}"))
        name = QLabel(employee[1])
        surname = QLabel(employee[2])
        phone = QLabel(employee[3])
        email = QLabel(employee[4])
        address = QLabel(employee[6])

        for i in reversed(range(self.leftLayout.count())):
            widget = self.leftLayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow("", img)
        self.leftLayout.addRow("Name: ", name)
        self.leftLayout.addRow("Surname: ", surname)
        self.leftLayout.addRow("Phone: ", phone)
        self.leftLayout.addRow("Email: ", email)
        self.leftLayout.addRow("Address: ", address)
            
    def singleClick(self):
        employee = self.employeeList.currentItem().text()
        id = employee.split('-')[0]
        query = "SELECT * FROM employees WHERE id=?"
        person = cur.execute(query, (id,)).fetchone() # single item tuple=(1,)
        self.showPersonOnLeftUI(person)

    def displayFirstRecord(self):
        query = "SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee = cur.execute(query).fetchone()

        self.showPersonOnLeftUI(employee)




    def layouts(self):
        ####### layout ####### 
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        ####### adding child layout to main layout #######
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 40)
        self.mainLayout.addLayout(self.rightMainLayout, 60)
        ####### adding widgets to layout #######
        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)

        ####### set main window layout #######
        self.setLayout(self.mainLayout)

    
    def updateEmployee(self):
        global person_id
        if self.employeeList.selectedItems():
            person = self.employeeList.currentItem().text()
            person_id = person.split('-')[0]
            self.updateWindow = UpdateEmployee()
            self.close()

            
        else:
            QMessageBox.information(self, "Warning", "Please select a person to update")


class UpdateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Employee")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):
        self.getPerson()
        self.mainDesign() # ui widget
        self.layouts() # layouts

    def closeEvent(self, evt):
        self.main=Main()

    def getPerson(self):
        global person_id
        
        query = "SELECT * FROM employees WHERE id=?"
        employee=cur.execute(query, (person_id,)).fetchone()
        self.name = employee[1]
        self.surname = employee[2]
        self.phone = employee[3]
        self.email = employee[4]
        self.image = employee[5]
        self.address = employee[6]
        

    def mainDesign(self):
        self.setStyleSheet("background-color: white;font-size:14; font-family:times;color:black;")

        ############## top layout widget #############
        self.title = QLabel("Update Person")
        self.title.setStyleSheet('font-size: 24pt;font-family: Arial Bold;')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap(f"images/{self.image}"))
        ############## bottom layout widget #############
        self.namelbl = QLabel("Name: ")
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.name)
        self.surnamelbl = QLabel("Surname: ")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setText(self.surname)

        self.phonelbl = QLabel("Phone: ")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setText(self.phone)

        self.emaillbl = QLabel("Email: ")
        self.emailEntry = QLineEdit()
        self.emailEntry.setText(self.email)

        self.imglbl = QLabel("Picture: ")
        self.imgButton = QPushButton("Browse")
        self.imgButton.setStyleSheet("background-color: orange;font-size: 10pt;")
        self.imgButton.clicked.connect(self.uploadImage)


        self.addresslbl = QLabel("Address")
        self.addressEditor = QTextEdit()
        self.addressEditor.setText(self.address)

        self.addButton = QPushButton("Update")
        self.addButton.setStyleSheet("background-color: orange;font-size: 10pt;")
        self.addButton.clicked.connect(self.updateEmployee)


    def uploadImage(self):
        global defaultImg
        size = (128,128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files(*.jpg *.png)')
        if ok:
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("images/{}".format(defaultImg))

    def updateEmployee(self):
        global defaultImg
        global person_id
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText()
        if (name and surname and phone != ""):
            try:
                query = 'UPDATE employees SET name=?, surname=?, phone=?, email=?, img=?, address=? WHERE id=?'
                cur.execute(query, (name, surname, phone, email, img, address, person_id))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been updated")
                self.close()
               
            except Exception as e:
                QMessageBox.information(self, "Warning", "Person has NOT been updated {}".format(e))



    def layouts(self):
        ############### create main layouts ###############
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        ########### add child layour to main layout #############
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)



        ########### add widget to layout #############
        #### top layout #############
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110, 20, 10, 30) # left, top, right, bottom
        ##### bottom layout #############
        self.bottomLayout.addRow(self.namelbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnamelbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phonelbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emaillbl, self.emailEntry)
        self.bottomLayout.addRow(self.imglbl, self.imgButton)
        self.bottomLayout.addRow(self.addresslbl, self.addressEditor)
        self.bottomLayout.addRow("", self.addButton)



        ########### set main layout for window #############
        self.setLayout(self.mainLayout)

class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employees")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign() # ui widget
        self.layouts() # layouts

    def closeEvent(self, evt):
        self.main=Main()
        

    def mainDesign(self):
        self.setStyleSheet("background-color: white;font-size:14; font-family:times;color:black;")

        ############## top layout widget #############
        self.title = QLabel("Add Person")
        self.title.setStyleSheet('font-size: 24pt;font-family: Arial Bold;')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap("icons/person.png"))
        ############## bottom layout widget #############
        self.namelbl = QLabel("Name: ")
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter Employee Name")

        self.surnamelbl = QLabel("Surname: ")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter Employee Surname")

        self.phonelbl = QLabel("Phone: ")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter Employee Phone Number")

        self.emaillbl = QLabel("Email: ")
        self.emailEntry = QLineEdit()
        self.emailEntry.setPlaceholderText("Enter Employee Email")

        self.imglbl = QLabel("Picture: ")
        self.imgButton = QPushButton("Browse")
        self.imgButton.setStyleSheet("background-color: orange;font-size: 10pt;")
        self.imgButton.clicked.connect(self.uploadImage)

        self.addresslbl = QLabel("Address")
        self.addressEditor = QTextEdit()

        self.addButton = QPushButton("Add")
        self.addButton.setStyleSheet("background-color: orange;font-size: 10pt;")
        self.addButton.clicked.connect(self.addEmployee)

    def uploadImage(self):
        global defaultImg
        size = (128,128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files(*.jpg *.png)')
        if ok:
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("images/{}".format(defaultImg))

    def addEmployee(self):
        global defaultImg
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText()
        if (name and surname and phone != ""):
            try:
                query = 'INSERT INTO employees (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)'
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been added")
                self.close()
               
            except Exception as e:
                QMessageBox.information(self, "Warning", "Person has NOT been added {}".format(e))



    def layouts(self):
        ############### create main layouts ###############
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        ########### add child layour to main layout #############
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)



        ########### add widget to layout #############
        #### top layout #############
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110, 20, 10, 30) # left, top, right, bottom
        ##### bottom layout #############
        self.bottomLayout.addRow(self.namelbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnamelbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phonelbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emaillbl, self.emailEntry)
        self.bottomLayout.addRow(self.imglbl, self.imgButton)
        self.bottomLayout.addRow(self.addresslbl, self.addressEditor)
        self.bottomLayout.addRow("", self.addButton)



        ########### set main layout for window #############
        self.setLayout(self.mainLayout)

    


def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()