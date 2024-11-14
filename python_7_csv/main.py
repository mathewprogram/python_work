#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, csv
from tabulate import tabulate

def menu():
    while True:
        print("\nMenú:")
        print("1. Mostrar tabla completa.")
        print("2. Buscar trabajadores por tipo (1-4).")
        print("3. Buscar trabajadores por nombre.")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            lista()
        elif opcion == "2":
            mostrar_trabajador_por_tipo()
        elif opcion == "3":
            mostrar_trabajador_por_nombre()
        elif opcion == "4":
            print("Adios.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def lista():
    
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_csv/trabajador.csv"
    headers = ["Id", "Nombre", "Apellido", "Tipo", "Sueldo"]
    #nra = "\\Users\\mihaitamatei\\Documents\\personal\\Projects\\python\\python_work_in_class\\python_csv\\trabajador.csv" - solo para Windows
    try:
        with open(nra, "r") as f:
            filas = csv.reader(f, delimiter=";")
            filas_l = list(filas)
            #print(list(filas_l))

            tabla = []
            for i, fila in enumerate(filas_l):
                tabla.append(fila)
            print(tabulate(tabla, headers=headers, tablefmt="fancy_grid")) 

    except FileNotFoundError:
        print("El archivo no existe")

def mostrar_trabajador_por_tipo():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_csv/trabajador.csv"
    headers = ["Id", "Nombre", "Apellido", "Tipo", "Sueldo"]
    try:
        tipo = input("Ingrese el tipo de trabajador que desea ver (1-4): ")
        
        with open(nra, "r") as f:
            filas = csv.reader(f, delimiter=";")
            filas_l = list(filas)
            
            # Filtrar los trabajadores por el tipo ingresado
            trabajadores_filtrados = [fila for fila in filas_l if fila[3] == tipo]
            
            if trabajadores_filtrados:
                print(tabulate(trabajadores_filtrados, headers=headers, tablefmt="fancy_grid"))
            else:
                print(f"No se encontraron trabajadores del tipo {tipo}.")

    except FileNotFoundError:
        print("El archivo no existe")
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar un número.")
        
def mostrar_trabajador_por_nombre():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_csv/trabajador.csv"
    headers = ["Id", "Nombre", "Apellido", "Tipo", "Sueldo"]
    try:
        nombre = input("Ingrese el nombre de trabajador que desea ver: ")
        
        with open(nra, "r") as f:
            filas = csv.reader(f, delimiter=";")
            filas_l = list(filas)
            
            # Filtrar los trabajadores por el tipo ingresado
            trabajadores_filtrados = [fila for fila in filas_l if fila[1] == nombre]
            
            if trabajadores_filtrados:
                print(tabulate(trabajadores_filtrados, headers=headers, tablefmt="fancy_grid"))
            else:
                print(f"No se encontraron trabajadores con el nombre: {nombre}.")

    except FileNotFoundError:
        print("El archivo no existe")
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar un número.")

def main():
    os.system("clear")
    menu()
if __name__ == "__main__":
   main()