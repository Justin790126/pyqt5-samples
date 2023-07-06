import os,sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#import style
#from PIL import Image
#from interface.Widgets import UIinterface
#from utils.db import *
from Sellings.SellingsModel import SellingsModel
from Sellings.SellingsView import SellingsView

from ConfirmWindow.ConfirmWindowCtrller import ConfirmWindowCtrller


class SellingsCtrller():

    ########## #add custom signal here ##########
    customSignal = pyqtSignal(tuple)

    def __init__(self):
        self.model = SellingsModel()
        self.view = SellingsView()

        
        self.model.queryProductsDone.connect(self.view.updateProductsUI)
        self.model.prepareProductsUIquery()

        self.model.queryMembersDone.connect(self.view.updateMembersUI)
        self.model.prepareMembersUIquery()

        self.model.queryQoutaDone.connect(self.view.updateQoutCombo)
        self.view.productCombo.currentIndexChanged.connect(self.changeComboValue)
        self.view.submitBtn.clicked.connect(self.sellProduct)

        

    def changeComboValue(self):
        product_id = self.view.productCombo.currentData()
        self.model.queryQouta(product_id)

    def sellProduct(self):
        
        self.confirm = ConfirmWindowCtrller(self.view.getSellProduct())
        # self.confirm.close()
        

    

