from PyQt5.QtCore import QObject, pyqtSignal



class CommonSignals(QObject):

    initDisplay = pyqtSignal()

    def __init__(self):
        super().__init__()