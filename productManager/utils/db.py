import sqlite3
from PyQt5.QtCore import *

con=sqlite3.connect("products.db")
cur=con.cursor()
productId = 0
memberId = 0

utilsSignal = {
    "initDataPrepareDone": pyqtSignal(tuple),
    "updateUI2DB": pyqtSignal(tuple),
    "delete2DB": pyqtSignal(int),
    "add2DB": pyqtSignal(tuple),
    "updateDBresult": pyqtSignal(tuple),
    "deleteDBresult": pyqtSignal(tuple),
    "addDBresult": pyqtSignal(tuple)
}
