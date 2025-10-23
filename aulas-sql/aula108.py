import sqlite3

from aula107 import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = "3"')

# row = cursor.fetchone()
# _id, name, weight = row
# print(_id, name, weight)

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
connection.close()
