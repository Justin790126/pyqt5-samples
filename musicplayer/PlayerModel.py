

class PlayerModel:
    def __init__(self):
        self.musicList = []
        self.songLength = 0
        self.muted = False
        self.index = 0
        self.count = 0 # for mp3 progress bar