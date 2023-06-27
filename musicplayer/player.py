import sys
import os
import random, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pygame import mixer
from mutagen.mp3 import MP3
import style

musicList = []
mixer.init()
muted = False
count = 0 # for mp3 progress bar
songLength = 0
index = 0



class Player(QWidget):
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
        self.addButton.clicked.connect(self.addSound)

        self.shuffleButton = QToolButton()
        self.shuffleButton.setIcon(QIcon("icons/shuffle.png"))
        self.shuffleButton.setIconSize(QSize(48,48))
        self.shuffleButton.setToolTip("Shuffle the list")
        self.shuffleButton.clicked.connect(self.shufflePlayList)

        self.previousButton = QToolButton()
        self.previousButton.setIcon(QIcon("icons/previous.png"))
        self.previousButton.setIconSize(QSize(48,48))
        self.previousButton.setToolTip("Play Previous")
        self.previousButton.clicked.connect(self.playPrevious)

        self.playButton = QToolButton()
        self.playButton.setIcon(QIcon("icons/play.png"))
        self.playButton.setIconSize(QSize(64,64))
        self.playButton.setToolTip("Play")
        self.playButton.clicked.connect(self.playSounds)
        

        self.nextButton = QToolButton()
        self.nextButton.setIcon(QIcon("icons/next.png"))
        self.nextButton.setIconSize(QSize(48,48))
        self.nextButton.setToolTip("Play Next")
        self.nextButton.clicked.connect(self.playNext)

        self.muteButton = QToolButton()
        self.muteButton.setIcon(QIcon("icons/mute.png"))
        self.muteButton.setIconSize(QSize(24,24))
        self.muteButton.setToolTip("Mute")
        self.muteButton.clicked.connect(self.muteSound)


        ########## volume slider #################

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setToolTip("Volume")
        self.volumeSlider.setTickInterval(1)
        self.volumeSlider.setValue(70)
        mixer.music.set_volume(0.7)
        self.volumeSlider.valueChanged.connect(self.setVolume)

        ########### play list ##########

        self.playList = QListWidget()
        self.playList.doubleClicked.connect(self.playSounds)
        self.playList.setStyleSheet(style.playListStyle())


        ######### timer ##########
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateProgress)

    def playSoundsByIndex(self, target_index):
        global musicList, songLength, count, index
        count = 0
        index = target_index

        try:
            mixer.music.load(str(musicList[index]))
            mixer.music.play()
            self.timer.start()

            sound = MP3(str(musicList[index]))
            songLength = round(sound.info.length)


            self.songLengthLabel.setText(time.strftime("/ %M:%S", time.gmtime(songLength)))

            self.progressBar.setValue(count)
            self.progressBar.setMaximum(songLength)


        except Exception as e:
            mbox = QMessageBox.information(self, "Error loading", f"Error : {e}")

    def playPrevious(self):
        global index
        items = self.playList.count()
        if index == 0:
            index = items

        index -= 1
        self.playSoundsByIndex(index)

        self.playList.setCurrentRow(index)

    def playNext(self):
        global index
        items = self.playList.count()
        index += 1
        if index >= items:
            index = 0

        self.playSoundsByIndex(index)
        self.playList.setCurrentRow(index)


    def playSounds(self):
        self.playSoundsByIndex(self.playList.currentRow())
        

    
    def updateProgress(self):
        global count
        global songLength
        count += 1


        self.progressBar.setValue(count)
        self.songTimerLabel.setText(time.strftime("%M:%S", time.gmtime(count)))
        if count == songLength:
            self.progressBar.setValue(songLength)

            self.timer.stop()

            

    def muteSound(self):
        global muted
        if muted == False:
            mixer.music.set_volume(0.0)
            muted = True
            self.muteButton.setIcon(QIcon("icons/unmuted.png"))
            self.muteButton.setToolTip("Unmute")
            self.volumeSlider.setValue(0)
        else:
            mixer.music.set_volume(0.7)
            muted = False
            self.muteButton.setIcon(QIcon("icons/mute.png"))
            self.muteButton.setToolTip("Mute")
            self.volumeSlider.setValue(70)


        

    def setVolume(self):
        self.volume = self.volumeSlider.value()
        mixer.music.set_volume(self.volume/100.0)

    
        
    def addSound(self):
        directory = QFileDialog.getOpenFileName(self, "Add Sound", "", "Sound Files (*.mp3 *.ogg *.wav)")
        filename = os.path.basename(directory[0])
        self.playList.addItem(filename)
        musicList.append(directory[0])

    def shufflePlayList(self):
        global musicList
        random.shuffle(musicList)
        self.playList.clear()
        for song in musicList:
            filename = os.path.basename(song)
            self.playList.addItem(filename)

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

def main():
    App = QApplication(sys.argv)
    window = Player()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()