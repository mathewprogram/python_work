#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, sqlite3
from tabulate import tabulate

def obtener_conexion():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_sqlite/hospital.sqlite3"
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None
    return conexion

def select1():
    conexion = obtener_conexion()
    if conexion is not None:
       cursor = conexion.cursor()
       try:
            query = "SELECT * FROM Consulta"
            cursor.execute(query)
            resultados_lt = cursor.fetchall()
            print(resultados_lt)
       except Exception as e:
            print("ERROR: SELECT ", e)
    else:
       print("ERROR: CONEXION")

def ejemplo1():
    conexion = obtener_conexion()
    if conexion is not None:
       cursor = conexion.cursor()
       try:
            cursor.execute("SELECT nombreMedico, COUNT(*) AS Consultas FROM Consulta GROUP BY nombreMedico ORDER BY nombreMedico") 
            resultados_lt = cursor.fetchall()
            if resultados_lt:
                cabeceras = ['Nombre Medico','Numero consultas']
                print(tabulate(resultados_lt, headers=cabeceras, tablefmt='fancy_grid'))
                
            else:
                print("ERROR: TABLA VACIA")    
       except Exception as e:
        print("ERROR QUERY", e)
    else:
        print("ERROR CONEXION")


def main():
    os.system("clear")
    ejemplo1()
    #select1()
          
if __name__ == "__main__":
   main()