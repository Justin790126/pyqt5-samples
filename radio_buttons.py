import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using radio buttons")
        self.setGeometry(250,150,1024,768)
        self.UI()
        
    
        
    def UI(self):
        self.name=QLineEdit(self)
        self.name.move(150,50)
        self.name.setPlaceholderText("Enter your name")

        self.surname=QLineEdit(self)
        self.surname.move(150, 80)
        self.surname.setPlaceholderText("Enter your surname")
        

        self.male=QRadioButton("Male",self)
        self.male.move(150, 110)
        self.male.setChecked(True)
        

        self.female=QRadioButton("Female",self)
        self.female.move(220, 110)
        self.female.setChecked(True)

        button = QPushButton("Submit",self)
        button.move(200, 140)
        button.clicked.connect(self.getValue)
        
        self.show()

    def getValue(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            print(f"{name} {surname} is a male")
        else:
            print(f"{name} {surname} is a female")
    
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