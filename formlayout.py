import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FormLayout")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        
        formLayout = QFormLayout()
        #formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)

        name_txt = QLabel("Name: ")
        name_input = QLineEdit()
        name_input.setPlaceholderText("Enter your name")

        pass_txt = QLabel("Passwords: ")
        pass_input = QLineEdit()
        pass_input.setPlaceholderText("Enter your password")
        pass_input.setEchoMode(QLineEdit.Password)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())

        # formLayout.addRow(name_txt, name_input)
        formLayout.addRow(name_txt, hbox1)
        formLayout.addRow(pass_txt, pass_input)
        formLayout.addRow(QLabel("Country: "), QComboBox())
        formLayout.addRow(hbox)
        # formLayout.addRow(QPushButton("Enter"), QPushButton("Exit"))

        self.setLayout(formLayout)


        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()