
import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal
from utils.db import con,cur,productId

con = sqlite3.connect("products.db")
cur = con.cursor()

class DisplayProductModel(QObject):

    initDataPrepareDone = pyqtSignal(tuple)
    updateDBresult = pyqtSignal(tuple)
    deleteDBresult = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()


    def prepareDatas(self, productId):
        query = "SELECT * FROM products WHERE product_id=?"
        product = cur.execute(query, (productId,)).fetchone()
        self.initDataPrepareDone.emit(product)

    def updateData2DB(self, queryArgs):
        try:
            query = "UPDATE products set product_name=?, product_manufacturer=?, product_price=?, product_qouta=?, product_img=?, product_availability=? WHERE product_id=?"
            cur.execute(query,queryArgs)
            con.commit()
            self.updateDBresult.emit(("Info", "Product has been updated"))

        except Exception as e:
            self.updateDBresult.emit(("Error", f"Error {e}"))

    def deleteBy(self, productId):
        try:
            cur.execute("DELETE FROM products WHERE product_id=?", (productId,))
            con.commit()
            self.deleteDBresult.emit(("Info", "Product has been deleted"))

        except Exception as e:
            self.deleteDBresult.emit(("Info", f"Delete error {e}"))




