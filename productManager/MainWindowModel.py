
import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal
from utils.db import con,cur,productId


class MainWindowModel(QObject):


    statisticDataChanged = pyqtSignal(dict)
    productsDataChanged = pyqtSignal(list)
    membersDataChanged = pyqtSignal(list)
    searchMembersGot = pyqtSignal(list)
    searchProductsGot = pyqtSignal(list)
    productsAvailabiltyGot = pyqtSignal(list)

    def __init__(self):
        super().__init__()


    def getStatistics(self):
        countProducts = cur.execute(
            "SELECT count(product_id) FROM products").fetchall()
        countProducts = countProducts[0][0]

        countMembers = cur.execute(
            "SELECT count(member_id) FROM members").fetchall()
        countMembers = countMembers[0][0]

        soldProducts = cur.execute(
            "SELECT SUM(selling_quantity) FROM sellings").fetchall()
        soldProducts = soldProducts[0][0]

        totalAmount = cur.execute(
            "SELECT SUM(selling_amount) FROM sellings").fetchall()
        totalAmount = totalAmount[0][0]

        self.statisticDataChanged.emit({
           "countProducts": countProducts,
           "countMembers": countMembers,
           "soldProducts": soldProducts,
           "totalAmount": totalAmount
        })


    def displayProducts(self):
 
        query = cur.execute(
            "SELECT product_id,product_name,product_manufacturer, product_price,product_qouta,product_availability FROM 'products'")

        self.productsDataChanged.emit(query.fetchall())

    def displayMembers(self):
        query = cur.execute("SELECT * FROM 'members'")
        self.membersDataChanged.emit(query.fetchall())

    def searchMembers(self, value):
        query = "SELECT * FROM members WHERE member_name LIKE ? or member_surname LIKE ? or member_phone LIKE ?"
        if (value == ""):
            self.searchMembersGot.emit([])
        else:
            results = cur.execute(
                query, (f"%{value}%", f"%{value}%", f"%{value}%")).fetchall()
            self.searchMembersGot.emit(results)

    def searchProduct(self, value):
        if (value == ""):
            self.searchProductsGot.emit([])
        else:
            query = "SELECT product_id, product_name, product_manufacturer, product_price, product_qouta, product_availability FROM products WHERE product_name LIKE ? or product_manufacturer LIKE ?"
            results = cur.execute(
                query, ('%' + value + '%', '%' + value + '%')).fetchall()
            self.searchProductsGot.emit(results)


    def listProductBy(self, availability):
        products = []
        if availability == True:
            query = ("SELECT product_id,product_name,product_manufacturer,product_price,product_qouta,"
                     "product_availability FROM products WHERE product_availability=?")
            products = cur.execute(query, ('Available',)).fetchall()
        else:
            query = ("SELECT product_id,product_name,product_manufacturer,product_price,product_qouta,"
                     "product_availability FROM products WHERE product_availability=?")
            products = cur.execute(query, ('UnAvailable',)).fetchall()
        
        self.productsAvailabiltyGot.emit(products)