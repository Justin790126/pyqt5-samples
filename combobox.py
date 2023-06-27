import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using combobox")
        self.setGeometry(250,150,1024,768)
        self.UI()
        
    
        
    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        self.combo.addItem("Python")
        self.combo.addItems(["C", "C#", "PHP"])
        list1=["Batman", "Superman", "Spiderman"]

        for name in list1:
            self.combo.addItem(name)

        for number in range(18, 101):
            self.combo.addItem(str(number))
                             
        button = QPushButton("Save", self)
        button.move(150, 130)
        button.clicked.connect(self.getValue)
        
        self.show()

    def getValue(self):
        value = self.combo.currentText()
        print(value)
    
    def submit(self):
        if (self.remember.isChecked()):
            print(f"Name : {self.name.text()}, \nsurname : {self.surname.text()}, \nremember me checked")
        else:
            print(f"Name : {self.name.text()}, \nsurname : {self.surname.text()}, \nremember me NOT checked")

    def removeImg(self):
        self.image.close()
    
    def showImg(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()