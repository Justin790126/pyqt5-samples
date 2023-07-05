from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *

from AddMember.AddMemberView import AddMemberView
from AddMember.AddMemberModel import AddMemberModel

class AddMemberCtrller():
    def __init__(self):
        self.model = AddMemberModel()
        self.view = AddMemberView()
        self.view.submitBtn.clicked.connect(self.view.addMember)
        self.view.add2DB.connect(self.model.addMember)
        self.model.addDBresult.connect(self.memberUpdateUI)
        # self.view.submitBtn.clicked.connect(self.view.addProduct)
        # self.view.add2DB.connect(self.model.addProduct)
        # self.model.addDBresult.connect(self.view.showUpdateDBresult)
        # self.view.uploadBtn.clicked.connect(self.view.uploadImg)
    
    def memberUpdateUI(self, title_content):
        self.view.showUpdateDBresult(title_content)
        self.view.clearText()




