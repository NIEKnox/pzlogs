import sqlite3

con = sqlite3.connect("database.db")
c = con.cursor()

c.execute("CREATE TABLE lines(datetime, text)")

