from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *
########## import DB / utils here ##########

class SellingsModel(QObject):

    ########## #add custom signal here ##########
    queryProductsDone = pyqtSignal(list)
    queryMembersDone = pyqtSignal(list)
    queryQoutaDone = pyqtSignal(int)

    def __init__(self):
        super().__init__()


    def prepareProductsUIquery(self):
        query1 = ("SELECT * FROM products WHERE product_availability=?")
        products = cur.execute(query1, ('Available',)).fetchall()
        self.queryProductsDone.emit(products)
        
    def prepareMembersUIquery(self):
        query2= ("SELECT member_id,member_name FROM members")
        members = cur.execute(query2).fetchall()
        self.queryMembersDone.emit(members)

    def queryQouta(self, product_id):
        query = ("SELECT product_qouta FROM products WHERE product_id=?")
        qouta = cur.execute(query, (product_id,)).fetchone()
        self.queryQoutaDone.emit(qouta[0])
        

