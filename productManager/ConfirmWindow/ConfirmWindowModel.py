from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.db import *
########## import DB / utils here ##########

class ConfirmWindowModel(QObject):

    ########## #add custom signal here ##########
    queryPriceDone = pyqtSignal(int)
    queryProductSellDone = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()


    def query_db(self, queryArgs):
        pass


    def priceQuery(self, productId):
        priceQUery=("SELECT product_price FROM products WHERE product_id =?")
        price = cur.execute(priceQUery, (productId,)).fetchone()
        self.queryPriceDone.emit(price[0])

    def queryUpdateProductSelling(self, productInfo):

        productName = productInfo[0]
        productId = productInfo[1]
        memberName = productInfo[2]
        memberId = productInfo[3]
        quantity = int(productInfo[4])
        amount = int(productInfo[5])
        try:
            sellQuery=("INSERT INTO 'sellings' (selling_product_id,selling_member_id,selling_quantity,selling_amount) VALUES (?,?,?,?)")
            cur.execute(sellQuery, (productId, memberId, quantity, amount))

            qoutaQuery=("SELECT product_qouta FROM products WHERE product_id=?")
            self.qouta = cur.execute(qoutaQuery, (productId,)).fetchone()

            if (quantity == self.qouta[0]):
                updateQoutaQuery = ("UPDATE products set product_qouta=?, product_availability=? WHERE product_id=?")
                cur.execute(updateQoutaQuery, (0, "UnAvailable", productId))
                con.commit()
            else:
                newQouta = self.qouta[0] - quantity
                updateQoutaQuery = ("UPDATE products set product_qouta=? WHERE product_id=?")
                cur.execute(updateQoutaQuery, (newQouta, productId))
                con.commit()

            self.queryProductSellDone.emit(("Info", "Confirm product purchased!", "close"))
            
        except Exception as e:
            self.queryProductSellDone.emit(("Error", f"Error confirm: {e}"))
