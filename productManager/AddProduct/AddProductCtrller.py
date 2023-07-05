from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *

from AddProduct.AddProductView import AddProductView
from AddProduct.AddProductModel import AddProductModel

class AddProductCtrller():
    def __init__(self):
        self.model = AddProductModel()
        self.view = AddProductView()
        self.view.submitBtn.clicked.connect(self.view.addProduct)
        self.view.add2DB.connect(self.model.addProduct)
        self.model.addDBresult.connect(self.view.showUpdateDBresult)
        self.view.uploadBtn.clicked.connect(self.view.uploadImg)



