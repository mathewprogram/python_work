#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, sqlite3

def ejemplo1():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_sqlite/test.sqlite3"
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None

    if conexion is not None:
       print("OK: CONEXION")
    else:
       print("ERROR: CONEXION")

def obtener_conexion():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_sqlite/test.sqlite3"
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None
    return conexion

def insert1():
    conexion = obtener_conexion()
    clientes_lt = [
        ("Juan Goycochea", 25, 50000, 3),
        ("María Paredes", 30, 75000, 5)
    ]
    if conexion is not None:
       cursor = conexion.cursor()
       try:
           for cliente_t in clientes_lt:
               query = "INSERT INTO Cliente (nombre, edad, ingresos, historial_compras) \
                        VALUES (?, ?, ?, ?)"
               cursor.execute(query, cliente_t)
           conexion.commit() # Guarda los cambios
           print("OK: INSERT")
       except Exception as e:
            print("ERROR: INSERT ", e)
    else:
      print("ERROR: CONEXION")

def insert2():
    conexion = obtener_conexion()
    '''
    nombre = input("Ingresar nombre? ")
    edad = int(input("Ingresar edad? "))
    ingresos = int(input("Ingresar ingresos? "))
    historial_compras = int(input("Ingresar historial de compras? "))
    cliente_t = (nombre, edad, ingresos, historial_compras)
    '''
    
    cliente_t = (input("Ingresar nombre? "), 
                 int(input("Ingresar edad? ")), 
                 float(input("Ingresar ingresos? ")), 
                 int(input("Ingresar historial de compras? ")))
    if conexion is not None:
       cursor = conexion.cursor()
       try:
           query = "INSERT INTO Cliente (nombre, edad, ingresos, historial_compras) \
                   VALUES (?, ?, ?, ?)"
           cursor.execute(query, cliente_t)
           conexion.commit() # Guarda los cambios
           print("OK: INSERT")
       except Exception as e:
            print("ERROR: INSERT ", e)
    else:
      print("ERROR: CONEXION")

def select1():
    conexion = obtener_conexion()
    if conexion is not None:
       cursor = conexion.cursor()
       try:
            query = "SELECT * FROM Cliente"
            cursor.execute(query)
            resultados_lt = cursor.fetchall()
            print(resultados_lt)
       except Exception as e:
            print("ERROR: SELECT ", e)
    else:
       print("ERROR: CONEXION")

def update1():
    conexion = obtener_conexion()
    if conexion is not None:
       cursor = conexion.cursor()
       try:
          query = "UPDATE Cliente SET nombre = ?, edad = ?, ingresos = ?, historial_compras = ?  WHERE id_cliente = ?"
          cursor.execute(query,('Delly Lescano',56,45000,8,1))
          conexion.commit() # Guardar cambios

          if cursor.rowcount > 0:
             print("OK: UPDATE")
          else:
             print("NO EXISTE CLIENTE CON ESE ID")

       except Exception as e:
           print("ERROR: UPDATE: ", e)
    else:
       print("ERROR: CONEXION")

def delete1():
    conexion = obtener_conexion()
    if conexion != None:
       id_cliente_eliminar = int(input("Ingresar id cliente eliminar?"))
       #print("OK: CONEXION")
       try:
          query = "DELETE FROM Cliente WHERE id_cliente = ?"
          cursor = conexion.cursor()
          cursor.execute(query,(id_cliente_eliminar,))
          conexion.commit() # Guardar cambios
          if cursor.rowcount > 0:
             print("OK: CLIENTE ELIMINADO")
          else:
             print("CLIENTE NO EXISTE")    
       except Exception as e:
           print("ERROR: DELETE")
    else:
      print("ERROR: CONEXION")


def main():
    os.system("clear")
    #ejemplo1()
    delete1()
    select1()
          
if __name__ == "__main__":
   main()