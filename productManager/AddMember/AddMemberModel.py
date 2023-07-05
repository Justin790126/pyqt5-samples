from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *

class AddMemberModel(QObject):

    initDataPrepareDone = utilsSignal["initDataPrepareDone"]
    updateDBresult = utilsSignal["updateDBresult"]
    deleteDBresult = utilsSignal["deleteDBresult"]
    addDBresult = utilsSignal["addDBresult"]

    def __init__(self):
        super().__init__()


    def addMember(self, queryArgs):
        try:
            query = "INSERT INTO 'members' (member_name, member_surname, member_phone) VALUES(?,?,?)"
            con.execute(query, queryArgs)
            con.commit()
            self.addDBresult.emit(("Add Member Success", "Add Member Success"))

            
        except Exception as e:
            self.addDBresult.emit(("Add Member Failure", f"Add Member Failure with {e}"))