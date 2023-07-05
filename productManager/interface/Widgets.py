from abc import ABC, abstractmethod
from PyQt5.QtWidgets import *
from utils.CommonMsgs import *

class UIinterface(QWidget):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.UI()
    

    @abstractmethod
    def UI(self):
        print(msg_interface_format.format(self.UI.__name__))
        
        self.widgets()
        self.layouts()
        

    @abstractmethod
    def widgets(self):
        print(msg_interface_format.format(self.widgets.__name__))
        pass

    @abstractmethod
    def layouts(self):
        print(msg_interface_format.format(self.layouts.__name__))
        pass

    @abstractmethod
    def prepareDatas(self):
        print(msg_interface_format.format(self.prepareDatas.__name__))
        pass