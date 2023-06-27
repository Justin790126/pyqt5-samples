import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu widget")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        ### mainmenu ###
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        helpMenu = menubar.addMenu("Help")

        ### submenu ###
        new = QAction("New Project", self)
        new.setShortcut("Ctrl+O")
       
        open = QAction("Open", self)
        exit = QAction("Exit", self)
        exit.setIcon(QIcon("icons/exit.png"))
        exit.triggered.connect(self.exitFunc)

        file.addAction(new)
        file.addAction(open)
        file.addAction(exit)

        ######### toolbar #########
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newTb = QAction(QIcon("icons/folder.png"), "New", self)
        tb.addAction(newTb)

        openTb = QAction(QIcon("icons/empty.png"), "Open", self)
        tb.addAction(openTb)

        saveTb = QAction(QIcon("icons/save.png"), "Save", self)
        tb.addAction(saveTb)

        exitTb = QAction(QIcon("icons/exit.png"), "Exit", self)
        exitTb.triggered.connect(self.exitFunc)
        tb.addAction(exitTb)

        tb.actionTriggered.connect(self.btnFunc)

        self.combo = QComboBox()
        self.combo.addItems(["spiderman", "superman", "batman"])

        tb.addWidget(self.combo)

        self.show()

    def btnFunc(self, btn):
        if btn.text() == "New":
            print("You clicked new button")
        elif btn.text() == "Open":
            print("You clicked open button")
        elif btn.text() == "Save":
            print("You clicked save button")
        else:
            pass

    def exitFunc(self):
        mbox = QMessageBox.information(self, "Warning", "Are you sure to exit?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit(0)



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()