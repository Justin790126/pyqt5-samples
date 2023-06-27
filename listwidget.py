import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Times", 14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using List widgets")
        self.setGeometry(250,150,550,350)
        self.UI()
        
    
        
    def UI(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100, 50)

        self.listWidget = QListWidget(self)
        self.listWidget.move(100, 80)

        list1=["Batman", "Superman", "Spiderman"]
        self.listWidget.addItems(list1)
        self.listWidget.addItem("yoyoman")

        # for number in range(1, 6):
        #     self.listWidget.addItem(str(number))
        btnAdd = QPushButton("Add",self)
        btnAdd.move(360, 80)
        btnAdd.clicked.connect(self.funcAdd)

        btnDelete = QPushButton("Delete",self)
        btnDelete.move(360,110)
        btnDelete.clicked.connect(self.funcDelete)

        btnGet = QPushButton("Get",self)
        btnGet.move(360, 140)
        btnGet.clicked.connect(self.funcGet)

        btnDeleteAll = QPushButton("Delete All", self)
        btnDeleteAll.move(360,170)
        btnDeleteAll.clicked.connect(self.funcDeleteAll)

        self.show()

    def funcDeleteAll(self):
        self.listWidget.clear()

    def funcGet(self):
        val = self.listWidget.currentItem().text()
        print(val)

    def funcDelete(self):
        id = self.listWidget.currentRow()
        print(id)
        self.listWidget.takeItem(id)

    def funcAdd(self):
        self.listWidget.addItem(self.addRecord.text())
        self.addRecord.setText("")


    def getValue(self):
        text = self.editor.toPlainText()
        print(text)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()