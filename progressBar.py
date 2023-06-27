import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon


count = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Progress bar")
        self.setGeometry(350, 150, 500, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.progressBar = QProgressBar()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.runProgressBar)

        btnStart = QPushButton("Start")
        btnStart.clicked.connect(self.timerStart)
        btnStop = QPushButton("Stop")
        btnStop.clicked.connect(self.timerStop)
        hbox.addWidget(btnStart)
        hbox.addWidget(btnStop)

        vbox.addWidget(self.progressBar)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.show()

    def runProgressBar(self):
        global count
        count += 1
        print(count)
        if count == 100:
            self.timer.stop()
        else:
            self.progressBar.setValue(count)


    def timerStart(self):
        self.timer.start();

    def timerStop(self):
        self.timer.stop();



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()