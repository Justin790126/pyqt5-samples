import os,random,time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from pygame import mixer
from mutagen.mp3 import MP3

from PlayerView import PlayerView
from PlayerModel import PlayerModel

mixer.init()

_self = None

class PlayerCtrller:
    def __init__(self):
        self.playerView = PlayerView()
        self.playerModel = PlayerModel()

        global _self
        _self = self.playerView
        
        _self.addButton.clicked.connect(self.addSound)
        _self.shuffleButton.clicked.connect(self.shufflePlayList)
        _self.previousButton.clicked.connect(self.playPrevious)
        _self.playButton.clicked.connect(self.playSounds)
        _self.nextButton.clicked.connect(self.playNext)
        _self.muteButton.clicked.connect(self.muteSound)
        _self.volumeSlider.valueChanged.connect(self.setVolume)
        _self.playList.doubleClicked.connect(self.playSounds)
        _self.timer.timeout.connect(self.updateProgress)

    def addSound(self):
        _self = self.playerView
        directory = QFileDialog.getOpenFileName(_self, "Add Sound", "", "Sound Files (*.mp3 *.ogg *.wav)")
        filename = os.path.basename(directory[0])
        _self.playList.addItem(filename)
        self.playerModel.musicList.append(directory[0])

    def shufflePlayList(self):
        global _self
        random.shuffle(self.playerModel.musicList)
        _self.playList.clear()
        for song in self.playerModel.musicList:
            filename = os.path.basename(song)
            _self.playList.addItem(filename)

    def playSoundsByIndex(self, target_index):
        global  _self
        self.playerModel.count = 0
        self.playerModel.index = target_index

        try:
            mixer.music.load(str(self.playerModel.musicList[self.playerModel.index]))
            mixer.music.play()
            _self.timer.start()

            sound = MP3(str(self.playerModel.musicList[self.playerModel.index]))
            self.playerModel.songLength = round(sound.info.length)


            _self.songLengthLabel.setText(time.strftime("/ %M:%S", time.gmtime(self.playerModel.songLength)))

            _self.progressBar.setValue(self.playerModel.count)
            _self.progressBar.setMaximum(self.playerModel.songLength)


        except Exception as e:
            mbox = QMessageBox.information(self, "Error loading", f"Error : {e}")

    def playPrevious(self):
        global  _self
        items = _self.playList.count()
        if self.playerModel.index == 0:
            self.playerModel.index = items

        self.playerModel.index -= 1
        self.playSoundsByIndex(self.playerModel.index)

        _self.playList.setCurrentRow(self.playerModel.index)

    def playSounds(self):
        global _self
        self.playSoundsByIndex(_self.playList.currentRow())
        
    def playNext(self):
        global  _self
        items = _self.playList.count()
        self.playerModel.index += 1
        if self.playerModel.index >= items:
            self.playerModel.index = 0

        self.playSoundsByIndex(self.playerModel.index)
        _self.playList.setCurrentRow(self.playerModel.index)

    def muteSound(self):
        global _self
        if  self.playerModel.muted == False:
            mixer.music.set_volume(0.0)
            self.playerModel.muted = True
            _self.muteButton.setIcon(QIcon("icons/unmuted.png"))
            _self.muteButton.setToolTip("Unmute")
            _self.volumeSlider.setValue(0)
        else:
            mixer.music.set_volume(0.7)
            self.playerModel.muted = False
            _self.muteButton.setIcon(QIcon("icons/mute.png"))
            _self.muteButton.setToolTip("Mute")
            _self.volumeSlider.setValue(70)

    def setVolume(self):
        global _self
        self.volume = _self.volumeSlider.value()
        mixer.music.set_volume(self.volume/100.0)

    def updateProgress(self):
        global _self
        self.playerModel.count += 1


        _self.progressBar.setValue(self.playerModel.count)
        _self.songTimerLabel.setText(time.strftime("%M:%S", time.gmtime(self.playerModel.count)))
        if self.playerModel.count == self.playerModel.songLength:
            _self.progressBar.setValue(self.playerModel.songLength)

            _self.timer.stop()