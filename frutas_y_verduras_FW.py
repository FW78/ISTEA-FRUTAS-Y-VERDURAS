"""
FRUTAS Y VERDURAS 

AUTOR: WAIBSCHNAIDER FABIAN
EMAIL: F.WAIBSCHNAIDER@HOTMAIL.COM

1) Hacer un menú con las necesidades de una persona durante 5/7 dias. Desde la tabla 1 saco las calorías, vitaminas y minerales
2) Presupuesto

"""

import sqlite3

def conectar_db(nombre):
    global connection
    connection = sqlite3.connect(f"{nombre}.db")
    return connection.cursor()

def consultar_tablas():
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(query)
    for linea in cursor:
        print(linea)
    cursor.close
    connection.close


nombre_db = "frutas_y_verduras_FW"
cursor = conectar_db(nombre_db)
consultar_tablas()
query = "SELECT * FROM 'frutas_y_verduras'"
cursor.execute(query)
for linea in cursor:
    print(linea)
    cursor.close
