#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, mysql.connector
from tabulate import tabulate

def get_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="Passw0rd!",
            database="test0001"
        )
    except:
        connection = None
        
    if connection != None:
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM Cliente;"
            cursor.execute(query)
            resultados_lt = cursor.fetchall()
            #print(resultados_lt)
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()
    return connection

#CRUD - Create, Read, Update, Delete

def create():  #automatico
    connection = get_connection()
    if connection != None:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO Cliente (nombre, edad, ingresos, historial_compras) VALUES (%s, %s, %s, %s);"
            values = ("Mihai", 30, 30000, 10)
            cursor.execute(query, values)
            connection.commit()
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()

def create_insert():  #en base al input del usuario
    connection = get_connection()
    if connection != None:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO Cliente (nombre, edad, ingresos, historial_compras) \
                    VALUES (%s, %s, %s, %s);"
            values = (input("Ingrese el nombre: "), 
                      int(input("Ingrese la edad: ")), 
                      int(input("Ingrese los ingresos: ")), 
                      int(input("Ingrese el historial de compras: ")))
            cursor.execute(query, values)
            connection.commit()
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()

def create_insert_archivo():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_mysql/clientes.csv"
    if os.path.exists(nra):
        with open(nra, "r", encoding="utf-8") as f:  # Usa encoding para evitar problemas de codificación
            query = f.read()

        connection = get_connection()  # Implementa esta función para obtener la conexión
        if connection is not None:
            cursor = connection.cursor()
            try:
                # Divide las instrucciones por punto y coma para ejecutar cada una
                for command in query.split(';'):
                    command = command.strip()
                    if command:  # Asegúrate de que el comando no esté vacío
                        cursor.execute(command)

                connection.commit()
                print("Datos insertados correctamente.")
            except Exception as e:
                print("Error: {}".format(e))
            finally:
                cursor.close()
                connection.close()  # Cerrar la conexión aquí también
    else:
        print("El archivo {} no existe.".format(nra))


def read():  #esta funcion imprime la informacion que contiene la tabla en bruto
    connection = get_connection()
    if connection != None: # !=  - This is a general comparison operator for inequality, equivalent to <> in SQL.
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM Cliente;"
            cursor.execute(query)
            resultados_lt = cursor.fetchall()
            print(resultados_lt)
            print()
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()

def read_table():  #esta funcion imprime la informacion que contiene la tabla bonito
    connection = get_connection()
    if connection is not None: #is not - this operator is specifically used to check if a value is NULL or NOT NULL.
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM Cliente;"
            cursor.execute(query)
            resultados_lt = cursor.fetchall()
            
            if resultados_lt:
                cabeceras = ["Id", "Nombre", "Edad", "Ingresos", "Compras"]
                print(tabulate(resultados_lt, headers=cabeceras, tablefmt="fancy_grid", stralign="left", numalign="center"))
            else:
                print("No se encontraron datos en la tabla Cliente.")
                
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            cursor.close()
            connection.close()
    else:
        print("No se pudo establecer la conexión con la base de datos.")
        


def update():  #automatico
    connection = get_connection()
    if connection != None:
        cursor = connection.cursor()
        try:
            query = "UPDATE Cliente SET nombre = 'Mihai Matei' WHERE nombre = 'Mihai';"
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()

def update_id():  #en base al input del usuario
    connection = get_connection()
    if connection != None:
        cursor = connection.cursor()
        try:
            # Solicitud al usuario el ID del cliente primero
            id_cliente = input("Ingrese el id para actualizar: ")
            # Definir la consulta y los valores
            query = "UPDATE Cliente SET nombre = %s, edad = %s, ingresos = %s, historial_compras = %s WHERE id_cliente = %s;"
            values = (input("Ingrese el nuevo nombre: "),
                      int(input("Ingrese la nueva edad: ")),          
                      int(input("Ingrese la nueva cantidad de ingresos: ")),
                      int(input("Ingrese cantidad de compras: ")),
                      id_cliente)  # Asegúrate de que el id_cliente sea el último
            # Ejecutar la consulta
            cursor.execute(query, values)
            connection.commit()
            print("Registro actualizado exitosamente.")
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()
    else:
        print("No se pudo establecer la conexión con la base de datos.")
        
def delete():  #automatico
    connection = get_connection()
    if connection != None:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM Cliente WHERE nombre = 'Mihai';"
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()

def delete_id():  #en base al input del usuario
    connection = get_connection()
    if connection != None:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM Cliente WHERE id_cliente = %s;"
            values = (input("Ingrese el id para eliminar: "),)
            cursor.execute(query, values)
            connection.commit()
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()

def search():  #manual
    connection = get_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM Cliente WHERE id_cliente = %s;"
            id_cliente = input("Ingrese el id para buscar: ")
            values = (id_cliente,)
            
            cursor.execute(query, values)
            resultados_lt = cursor.fetchone()
            if resultados_lt:
                cabeceras = ["Id", "Nombre", "Edad", "Ingresos", "Compras"]
                print(tabulate([resultados_lt], headers=cabeceras, tablefmt="fancy_grid", stralign="left", numalign="center"))
            else:
                print("No se encontraron datos en la tabla Cliente.")
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()

def main():
    os.system("clear")
    connection = get_connection()
    if connection != None:
        search()
        #print("Connection established.")
        #create_insert()
        #delete_id()
        #update_id()
        #create_insert_archivo()
        #read()£
        #read_table()
    else:
        print("Connection failed.")
          
if __name__ == "__main__":
   main()