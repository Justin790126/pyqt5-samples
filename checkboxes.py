import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using labels")
        self.setGeometry(50,50,1024,768)
        self.UI()
        
    
        
    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter your surname")

        self.name.move(150,50)
        self.surname.move(150,80)

        self.remember=QCheckBox("Remember me", self)
        self.remember.move(150,110)

        button=QPushButton("Submit", self)
        button.move(200,140)
        button.clicked.connect(self.submit)
        

        self.show()
    
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