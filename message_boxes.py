import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using message boxes")
        self.setGeometry(250,150,1024,768)
        self.UI()
        
    
        
    def UI(self):

        button = QPushButton("Click me", self)
        button.setFont(font)
        button.move(200,150)
        button.clicked.connect(self.infomessageBox)
        
        self.show()

    def infomessageBox(self):
        mbox=QMessageBox.information(self, "Information",
                                     "You logged out!")

    def messageBox(self):
        mbox = QMessageBox.question(self,
                                    "Warning !!!", "Are you sure to exit?",
                                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                    QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()
        elif mbox==QMessageBox.No:
            print(f"You clicked No Button")




def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()