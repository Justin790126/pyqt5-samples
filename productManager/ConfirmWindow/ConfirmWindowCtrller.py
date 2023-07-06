import os,sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#import style
#from PIL import Image
#from interface.Widgets import UIinterface
#from utils.db import *
from ConfirmWindow.ConfirmWindowModel import ConfirmWindowModel
from ConfirmWindow.ConfirmWindowView import ConfirmWindowView

class ConfirmWindowCtrller():

    ########## #add custom signal here ##########
    customSignal = pyqtSignal(tuple)

    def __init__(self, productInfo):
        self.model = ConfirmWindowModel()
        self.view = ConfirmWindowView(productInfo)

        # productName = productInfo[0]
        productId = productInfo[1]
        print(productId, type(productId))
        # memberName = productInfo[2]
        # memberId = productInfo[3]
        # quantity = int(productInfo[4])

        self.model.queryPriceDone.connect(self.view.updateUIofPrice)
        self.model.priceQuery(productId)

        self.model.queryProductSellDone.connect(self.view.showUpdateDBresult)
        self.view.confirmBtn.clicked.connect(self.view.confirm)
        self.view.reqUpdateProductSelling2DB.connect(self.model.queryUpdateProductSelling)

    
    


