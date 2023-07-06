from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *

class DisplayMemberModel(QObject):

    initDataPrepareDone = utilsSignal["initDataPrepareDone"]
    updateDBresult = utilsSignal["updateDBresult"]
    deleteDBresult = utilsSignal["deleteDBresult"]

    def __init__(self):
        super().__init__()


    def prepareDatas(self, memberId):
        query = "SELECT * FROM members WHERE member_id=?"
        member = cur.execute(query, (memberId,)).fetchone()
        self.initDataPrepareDone.emit(member)

    def askDB2delete(self, memberId):
        try:
            cur.execute("DELETE FROM members WHERE member_id=?", (memberId,))
            con.commit()
            self.deleteDBresult.emit(("Delete Successful", "Member has been deleted", "close"))


        except Exception as e:
            self.deleteDBresult.emit(("Delete Fail", f"Delete Error: {e}"))


    def askDB2update(self, queryArgs):
        try:
            query = "UPDATE members set member_name=?, member_surname=?,member_phone=? WHERE member_id=?"
            cur.execute(query, queryArgs)
            con.commit()

            self.updateDBresult.emit(("Update Success", "member has been updated"))

        except Exception as e:
            self.updateDBresult.emit(("Update Error", f"Error: {e}"))
