import os
from herencia_futbol import *

seleccion_futbol_lo = []

def menu():
    
    while True:
        print("\nMenú:")
        print("1. Crear base de datos.")
        print("2. Crear objetos y guadarlos en una lista.")
        print("3. Mostrar objetos.")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            os.system("clear")
            crear_base_datos()
            input("Presiona Enter para continuar...")
        if opcion == "2":
            os.system("clear")
            crear_lista_objetos()
            input("Presiona Enter para continuar...")
        elif opcion == "3":
            os.system("clear")
            mostrar_lista_objetos()
            input("Presiona Enter para continuar...")
        elif opcion == "4":
            os.system("clear")
            print("Adios.")    
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def crear_base_datos():
    pass

def crear_lista_objetos():
    delBosque = Entrenador(1, "Vicente", "Del Bosque", 60, "284EZ89")
    zidane = Futbolista(2, "Zinedine", "Zidane", 29, 5, "Medio Central")
    raulMartinez = Masajista(3, "Raúl", "Martinez", 41, "Licenciado en Fisioterapia", 18)
    seleccion_futbol_lo.append(delBosque)
    seleccion_futbol_lo.append(zidane)
    seleccion_futbol_lo.append(raulMartinez)

def mostrar_lista_objetos():
    for seleccion_o in seleccion_futbol_lo:
        print(seleccion_o.nombre, end=" es ")
        if isinstance(seleccion_o, Entrenador):
            print("Entrenador")
        elif isinstance(seleccion_o, Futbolista):
            print("Futbolista")
        elif isinstance(seleccion_o, Masajista):
            print("Masajista")

def main():
    menu()
          
if __name__ == "__main__":
   main()

