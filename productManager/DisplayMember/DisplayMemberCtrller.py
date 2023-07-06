from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *

from DisplayMember.DisplayMemberView import DisplayMemberView
from DisplayMember.DisplayMemberModel import DisplayMemberModel

class DisplayMemberCtrller():
    def __init__(self, memberId):
        self.memberId = memberId
        print(self.memberId)

        self.view = DisplayMemberView(self.memberId)


        ################################################
        self.model = DisplayMemberModel()
        self.model.initDataPrepareDone.connect(self.view.setInitDatas)
        self.model.prepareDatas(self.memberId)

        self.view.delete2DB.connect(self.askDB2delete)
        self.model.deleteDBresult.connect(self.view.showUpdateDBresult)

        self.view.updateUI2DB.connect(self.askDB2update)
        self.model.updateDBresult.connect(self.view.showUpdateDBresult)

    def askDB2delete(self, memberId):
        self.model.askDB2delete(memberId)

    def askDB2update(self, queryArgs):
        self.model.askDB2update(queryArgs)


