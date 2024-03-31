import sqlite3

db = sqlite3.connect('testdb.db')
cursor = db.cursor()

cursor.execute('''create table table1(col1 text, col2 text, col3 integer)''')
cursor.close()

