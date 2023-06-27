import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)

computerScore = 0
playerScore = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors game")
        self.setGeometry(250,150,550,500)
        self.rndComputer=randint(1,3)
        self.rndPlayer = randint(1,3)
        self.UI()
        
    
        
    def UI(self):
        #######################Scores#####################
        self.scoreComputerText = QLabel("Computer Score:    ", self)
        self.scoreComputerText.move(30,20)
        self.scoreComputerText.setFont(textFont)
        self.scorePlayerText = QLabel("Your Score:    ", self)
        self.scorePlayerText.move(330, 20)
        self.scorePlayerText.setFont(textFont)
        
        ############## images ##############
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap("images/rock.png"))
        self.imageComputer.move(50, 100)
        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("images/rock.png"))
        self.imagePlayer.move(330, 100)

        self.imageGame = QLabel(self)
        self.imageGame.setPixmap(QPixmap("images/game.png"))
        self.imageGame.move(230, 160)

        ############ buttons #############
        btnStart = QPushButton("Start", self)
        btnStart.setFont(buttonFont)
        btnStart.move(180,250)
        btnStart.clicked.connect(self.start)
        btnStop = QPushButton("Stop", self)
        btnStop.setFont(buttonFont)
        btnStop.move(270,250)
        btnStop.clicked.connect(self.stop)

        ######### timer #########
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playGame)

        self.show()
    
    def start(self):
        self.timer.start()

    def playGame(self):
        self.rndComputer=randint(1,3)
        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap("images/rock.png"))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap("images/paper.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("images/scissors.png"))

        self.rndPlayer = randint(1,3)
        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("images/rock.png"))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("images/paper.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("images/scissors.png"))


        

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndComputer == self.rndPlayer:
            mbox = QMessageBox.information(self, "Information", "Draw Game")
            

        elif (self.rndComputer == 1 and self.rndPlayer == 2) or (self.rndComputer == 2 and self.rndPlayer == 3) or (self.rndComputer == 3 and self.rndPlayer == 1):
            
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1

        elif (self.rndComputer ==1 and self.rndPlayer == 3) or (self.rndComputer == 2 and self.rndPlayer == 1) or (self.rndComputer == 3 and self.rndPlayer == 2):
            
            mbox = QMessageBox.information(self, "Information", "Computer Win")
            computerScore += 1

      
        self.scorePlayerText.setText("Your Score: {}".format(playerScore))
        self.scoreComputerText.setText("Computer Score: {}".format(computerScore))

        if computerScore == 3 or playerScore == 3:
            mbox = QMessageBox.information(self, "Information", "Game over")
            sys.exit()





def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
