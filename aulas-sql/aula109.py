"""
Python - dotenv

A biblioteca python-dotenv (ou só dotenv) serve basicamente
para guardar informações sensíveis ou de configuração em um
arquivo separado (.env), em vez de deixar essas informações
direto no código.
"""

import dotenv
import pymysql
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

# Exemplo de como o dotenv puxa as variáveis de dentro do arquivo .env
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

# As conexões são de uso único, após fechar não é possível
# reutilizá-las.
with connection:
    # Já os cursores podem ser reutilizados.
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)) '
        )
        # Atenção! O comando abaixo limpa a tabela informada!
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} (name, age) VALUES ("Leah", 18) '
        )
    connection.commit()
