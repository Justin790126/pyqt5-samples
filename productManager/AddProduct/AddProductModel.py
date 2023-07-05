from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *

class AddProductModel(QObject):

    initDataPrepareDone = utilsSignal["initDataPrepareDone"]
    updateDBresult = utilsSignal["updateDBresult"]
    deleteDBresult = utilsSignal["deleteDBresult"]
    addDBresult = utilsSignal["addDBresult"]

    def __init__(self):
        super().__init__()


    def addProduct(self, queryArgs):
        try:
            query = "INSERT INTO 'products' (product_name,product_manufacturer,product_price,product_qouta,product_img) VALUES(?,?,?,?,?)"
            con.execute(query, queryArgs)
            con.commit()
            self.addDBresult.emit(("Add Product Successfully", "Add Product Successfully"))

            
        except Exception as e:
            self.addDBresult.emit(("Add Product Error", f"Error: {e}"))