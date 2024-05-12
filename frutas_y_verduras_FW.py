"""
FRUTAS Y VERDURAS 

AUTOR: WAIBSCHNAIDER FABIAN
EMAIL: F.WAIBSCHNAIDER@HOTMAIL.COM

1) Hacer un menú con las necesidades de una persona durante 5/7 dias. Desde la tabla 1 saco las calorías, vitaminas y minerales
2) Presupuesto

"""

import sqlite3
import json

def conectar_db(nombre):
    global connection
    connection = sqlite3.connect(f"{nombre}.db")
    return connection.cursor()

def consultar_tablas():
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(query)
    for linea in cursor:
        print(linea)
    # cursor.close
    # connection.close

def definir_menu():
    while True:
        print("\n")
        print("*"*50)
        print(f"Bienvenido. Gracias por usar la app MENU A MEDIDA\n")
        print("*"*50)
        opcion_gen = ("f", "m")
        genero = ""
        while genero not in opcion_gen: 
            genero = input("Ingrese F por femenino o M por masculino.\n\n").lower()
        dias = ""
        while not dias.isdecimal():
            dias = input("Ingrese la cantidad de dias\n\n")

        # Abro el archivo Json
        with open('nutrientes.json', 'r') as archivo:
            nutrientes_diarios = json.load(archivo)
            menu_diario = {}
            for nutri, cant in nutrientes_diarios.items():
                menu_diario[nutri] = cant[genero]
        print(menu_diario)
        print(dias)
        break
        

nombre_db = "frutas_y_verduras_FW"
cursor = conectar_db(nombre_db)
definir_menu()




# consultar_tablas()
# query = "SELECT * FROM 'frutas_y_verduras'"
# cursor.execute(query)
# for linea in cursor:
#     print(linea)
cursor.close