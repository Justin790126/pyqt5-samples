import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File dialog")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()

        fileButton = QPushButton("Open File")
        fileButton.clicked.connect(self.openFile)

        fontButton = QPushButton("Change Font")
        fontButton.clicked.connect(self.changeFont)

        colorButton = QPushButton("Change Color")
        colorButton.clicked.connect(self.changeColor)

        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(fileButton)
        hbox.addWidget(fontButton)
        hbox.addWidget(colorButton)
        hbox.addStretch()

        self.setLayout(vbox)

        self.show()

    def changeColor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)

    def changeFont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)

    def openFile(self):
        url = QFileDialog.getOpenFileName(self, "Open a file", "", "All Files(*);;*.txt")
        print(url)
        fileurl =url[0]
        file = open(fileurl, 'r')
        content = file.read()
        self.editor.setText(str(content))




def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()