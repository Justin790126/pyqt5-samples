import sys
import os
import random, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pygame import mixer
from mutagen.mp3 import MP3
import style



class PlayerView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(450, 150, 480, 700)
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
        

    def widgets(self):
        ############## progress bar #############
        self.progressBar = QProgressBar()
        self.progressBar.setTextVisible(False)
        self.progressBar.setStyleSheet(style.progressBarStyle())

        ############ lables for duration #############

        self.songTimerLabel = QLabel("0:00")
        self.songLengthLabel = QLabel("/ 0:00")

        ########## add buttons #########
        self.addButton = QToolButton()
        self.addButton.setIcon(QIcon("icons/add.png"))
        self.addButton.setIconSize(QSize(48,48))
        self.addButton.setToolTip("Add a song")

        self.shuffleButton = QToolButton()
        self.shuffleButton.setIcon(QIcon("icons/shuffle.png"))
        self.shuffleButton.setIconSize(QSize(48,48))
        self.shuffleButton.setToolTip("Shuffle the list")

        self.previousButton = QToolButton()
        self.previousButton.setIcon(QIcon("icons/previous.png"))
        self.previousButton.setIconSize(QSize(48,48))
        self.previousButton.setToolTip("Play Previous")

        self.playButton = QToolButton()
        self.playButton.setIcon(QIcon("icons/play.png"))
        self.playButton.setIconSize(QSize(64,64))
        self.playButton.setToolTip("Play")
        

        self.nextButton = QToolButton()
        self.nextButton.setIcon(QIcon("icons/next.png"))
        self.nextButton.setIconSize(QSize(48,48))
        self.nextButton.setToolTip("Play Next")
        self.muteButton = QToolButton()
        self.muteButton.setIcon(QIcon("icons/mute.png"))
        self.muteButton.setIconSize(QSize(24,24))
        self.muteButton.setToolTip("Mute")


        ########## volume slider #################

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setToolTip("Volume")
        self.volumeSlider.setTickInterval(1)
        self.volumeSlider.setValue(70)
        mixer.music.set_volume(0.7)
        ########### play list ##########

        self.playList = QListWidget()
        self.playList.setStyleSheet(style.playListStyle())


        ######### timer ##########
        self.timer = QTimer()
        self.timer.setInterval(1000)

    
    def layouts(self):

        ########### Create layouts #########
        self.mainLayout = QVBoxLayout()

        self.topMainLayout = QVBoxLayout()
        self.topGroupBox = QGroupBox("Music Player")
        self.topGroupBox.setStyleSheet(style.groupBoxStyle())
        self.topLayout = QHBoxLayout()
        self.middleLayout = QHBoxLayout()


        self.bottomLayout = QVBoxLayout()

        ########## Add widgets ##########
        self.topLayout.addWidget(self.progressBar)
        self.topLayout.addWidget(self.songTimerLabel)
        self.topLayout.addWidget(self.songLengthLabel)

        ############# middle widgets #########
        self.middleLayout.addStretch()
        self.middleLayout.addWidget(self.addButton)
        self.middleLayout.addWidget(self.shuffleButton)
        self.middleLayout.addWidget(self.playButton)
        self.middleLayout.addWidget(self.previousButton)
        self.middleLayout.addWidget(self.nextButton)
        self.middleLayout.addWidget(self.volumeSlider)
        self.middleLayout.addWidget(self.muteButton)
        self.middleLayout.addStretch()



        ############ Bottom layout widget #################
        self.bottomLayout.addWidget(self.playList)
        self.topMainLayout.addLayout(self.topLayout)
        self.topMainLayout.addLayout(self.middleLayout)
        self.topGroupBox.setLayout(self.topMainLayout)
        self.mainLayout.addWidget(self.topGroupBox, 25)
        self.mainLayout.addLayout(self.bottomLayout, 75)
        self.setLayout(self.mainLayout)

        ###### top layout #########

