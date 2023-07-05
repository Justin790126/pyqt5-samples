import sqlite3

con=sqlite3.connect("products.db")
cur=con.cursor()
productId = 0