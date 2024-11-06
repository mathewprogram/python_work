#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, sqlite3
from tabulate import tabulate

def menu():
    print("1. Eliminar tablas.")
    print("2. Crear tablas.")
    print("3. Insertar registros tablas.")
    print("4. Eliminar tabla por nombre.")
    print("5. Mostrar tabla por nombre.")
    print("6. Exit.")

    opcion = input("Seleccione una acción: ")
    if opcion == "1":
        os.system("clear")
        eliminar_tablas()
        input("Presiona Enter para continuar...")
        menu()
    elif opcion == "2":
        os.system("clear")
        create_tables()
        input("Presiona Enter para continuar...")
        menu()
    elif opcion == "3":
        os.system("clear")
        insertar()
        input("Presiona Enter para continuar...")
        menu()
    elif opcion == "4":
        os.system("clear")
        eliminar_tabla()
        input("Presiona Enter para continuar...")
        menu()
    elif opcion == "5":
        os.system("clear")
        mostrar_tabla()
        input("Presiona Enter para continuar...")
        menu()
    elif opcion == "6":
        os.system("clear")
        print("Goodbye.")
        exit();
    else:
        os.system("clear")
        print("Opcion no valida. Por favor elija una de las anteriores.")
        input("Presiona Enter para continuar...")
        menu();


def get_connection():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_sqlite/hospital.sqlite3"
    connection = None
    try:
       connection = sqlite3.connect(nra)
    except sqlite3.Error as error:
       connection = None
    return connection

def eliminar_tablas():
    connection = get_connection();
    if connection != None:
        cursor = connection.cursor()
        try:
            query = "SELECT DISTINCT strftime('%Y', fecha) FROM Consulta;"
            cursor.execute(query)
            resultados_lt = cursor.fetchall()
            for result_t in resultados_lt:
                year = result_t[0]
                query_year="""DROP TABLE Consulta""" + year;
                cursor.execute(query_year)
                print("Table droped,", year)
        except Exception as e:
            print("Error: {}".format(e))    
    else:
        print("Connection Error.")

def eliminar_tabla():
    connection = get_connection();
    if connection != None:
        cursor = connection.cursor()
        table_year = input("Ingrese el año de la tabla que desea eliminar: ")
        try:
            query = f"DROP TABLE Consulta{table_year};"
            cursor.execute(query)
            connection.commit()  # Guarda los cambios
            print(f"Tabla '{table_year}' eliminada.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()  # Cerrar el cursor después de ejecutar
            connection.close()  # Cerrar la conexión
    else:
        print("Error de conexión.")

def create_tables():
    connection = get_connection();
    if connection != None:
        cursor = connection.cursor()
        try:
            query = "SELECT DISTINCT strftime('%Y', fecha) FROM Consulta;"
            cursor.execute(query)
            resultados_lt = cursor.fetchall()
            for result_t in resultados_lt:
                year = result_t[0]
                query_year="""CREATE TABLE Consulta""" + year + """ (
                            numeroConsulta TEXT(10) NOT NULL,
                            fecha          TEXT     NOT NULL,
                            nombreMedico   TEXT(50) NOT NULL,
                            deinpr         TEXT(20) NOT NULL,
                            procedencia    TEXT(20) NOT NULL,
                            PRIMARY KEY (numeroConsulta));
                           """;
                cursor.execute(query_year)
                print("Table created.", year)
        except Exception as e:
            print("Error: {}".format(e))    
    else:
        print("Connection Error.")

def insertar():
    connection = get_connection();
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "SELECT DISTINCT strftime('%Y', fecha) FROM Consulta;"
            cursor.execute(query)
            years = cursor.fetchall()

            # Iterate over each year and execute the inner query
            for year_tuple in years:
                year = year_tuple[0]
                query_insert = """SELECT numeroConsulta, fecha, nombreMedico, deinpr, procedencia
                                  FROM Consulta
                                  WHERE strftime('%Y', fecha) = ?;"""  # Use parameterized query
                cursor.execute(query_insert, (year,))
                resultados_lt = cursor.fetchall()

                # Determine the target table based on the year
                target_table = f'Consulta{year}'
                for result in resultados_lt:
                    # Prepare the insert query for the corresponding table
                    insert_query = f"""INSERT INTO {target_table} (numeroConsulta, fecha, nombreMedico, deinpr, procedencia)
                                       VALUES (?, ?, ?, ?, ?);"""
                    cursor.execute(insert_query, result)

                # Commit the changes after each year
                connection.commit()
                print(f"Inserted results for year {year} into {target_table}")
        except Exception as e:
            print("Error: {}".format(e))

    

def mostrar_tabla():
    connection = get_connection();
    if connection is not None:
        cursor = connection.cursor()
        try:
            table_display = input("Ingrese el nombre de la tabla que desea mostrar: ")    
            query = f"SELECT * FROM {table_display};"
            cursor.execute(query)
            
            results = cursor.fetchall()
            headers = ["Nr Consulta", "Fecha", "Médico", "Operación", "Procedencia"]

            print(f"Tabla 'Consulta{table_display}':")
            print(tabulate(results, headers=headers, tablefmt='fancy_grid'))
        except Exception:
            print(f"Tabla 'Consulta{table_display}' no existe.")
        finally:
            cursor.close()  # Cerrar el cursor después de ejecutar
            connection.close()  # Cerrar la conexión
            
def main():
    os.system("clear")
    menu()
          
if __name__ == "__main__":
   main()
