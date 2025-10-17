import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cuidado ao fazer delete sem where!
cursor.execute(f'DELETE FROM {TABLE_NAME}')
# Zera a sequência de Id's
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Cuidado com sql injection!
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (name, weight) '
#     'VALUES ("Luana", 57), '
#     '("Geovanna", 63.5)'
# )
# Método menos perigoso de se inserir valores
sql = f'INSERT INTO {TABLE_NAME} (name, weight) ' 'VALUES (?, ?)'
# cursor.execute(sql, ['Geovanna', 63.2])
cursor.executemany(sql, [['Geovanna', 63.2], ['Leah', 10.3], ['Aurora', 9.4]])
connection.commit()

cursor.close()
connection.close()
