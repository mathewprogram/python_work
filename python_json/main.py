#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, json, csv
from tabulate import tabulate

def menu():
    while True:
        print("\nMenú:")
        print("1. Leer lista datos.json")
        print("2. Cambiar formato trabajador.csv a trabajador.json")
        print("3. Leer archivo convertido a JSON.")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            read()        
        elif opcion == "2":
            os.system("clear")
            cambio_formato()
        elif opcion == "3":
            os.system("clear")
            read_json()
        elif opcion == "4":
            os.system("clear")
            print("Adios.")    
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def read():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_json/datos.json"
    headers = ["Nombre y Apellido", "Edad", "Curso"]
    with open(nra,"r", encoding="utf-8") as f:
        filas_l = json.load(f)
        #print(filas_l)
        #for fila_d in filas_l:
            #print(fila_d)
    
        tabla = []
        for fila in filas_l:
          tabla.append([fila.get("nombre"), fila.get("edad"), fila.get("curso")])
        print(tabulate(tabla, headers=headers, tablefmt="fancy_grid", stralign="center", numalign="center")) 

def cambio_formato():
    nra_csv = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_csv/trabajador.csv"
    nra_json = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_json/trabajador.json"
    try:
        with open(nra_csv, "r", encoding="utf-8") as f:
            filas = csv.reader(f, delimiter=";")
            filas_l = list(filas)

            # Usar la primera fila como encabezados
            trabajadores = []  # Lista para almacenar los trabajadores

            for fila in filas_l:  # Recorrer todas las filas
                trabajador_dict = {
                    "id": fila[0],        # "dato del archivo" para id
                    "nombre": fila[1],    # "dato del archivo" para nombre
                    "apellido": fila[2],   # "dato del archivo" para apellido
                    "tipo": fila[3],      # "dato del archivo" para tipo
                    "sueldo": fila[4]     # "dato del archivo" para sueldo
                }
                trabajadores.append(trabajador_dict)  # Añadir el diccionario a la lista
                print(trabajador_dict)
            # Guardar la lista de trabajadores como JSON
            with open(nra_json, "w", encoding="utf-8") as json_file:
                json.dump(trabajadores, json_file, ensure_ascii=False, indent=4)

            print(f"\nLos datos han sido convertidos y guardados en {nra_json}")

    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def read_json():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_json/trabajador.json"
    headers = ["Id", "Nombre", "Apellido", "Tipo", "Sueldo"]
    with open(nra,"r", encoding="utf-8") as f:
        filas_l = json.load(f)
        #print(filas_l)
        #for fila_d in filas_l:
            #print(fila_d)
    
        tabla = []
        for fila in filas_l:
          tabla.append([fila.get("id"), fila.get("nombre"), fila.get("apellido"), fila.get("tipo"), fila.get("sueldo")])
        print(tabulate(tabla, headers=headers, tablefmt="fancy_grid", stralign="center", numalign="center"))

def main():
    os.system("clear")
    menu()
if __name__ == "__main__":
   main()