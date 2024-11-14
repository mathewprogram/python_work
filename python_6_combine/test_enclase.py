import os, sqlite3
import random as rd
from tabulate import tabulate

def get_connection():
    return sqlite3.connect("/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_combine/bancopreguntas.sqlite3")

# Base de datos
preguntas_l = []

def construir_preguntas():
    connection = get_connection()
    if connection is not None:
        cursor = connection.cursor()
        try: 
            query_pregunta = "SELECT * FROM Pregunta;"
            cursor.execute(query_pregunta)
            registro_lt = cursor.fetchall()
            for respuesta_t in registro_lt:
                pregunta_d = {}
                id_pregunta, pregunta, respuesta = respuesta_t    
                query_opcion = "SELECT * FROM Opcion WHERE id_pregunta = ?;"
                cursor.execute(query_opcion, (id_pregunta,))
                opcion_t = cursor.fetchall()
                pregunta_d["pregunta"] = pregunta
                pregunta_d["opciones_l"] = [opcion[1] for opcion in opcion_t]  # Extraer el texto de la opción
                pregunta_d["respuesta"] = respuesta
                preguntas_l.append(pregunta_d)                                
        except Exception as e:  
            print("Error al construir preguntas: {}".format(e))
    else:
        print("No se pudo establecer la conexión con la base de datos.")

# Función para ejecutar el test
def test_preguntas(num_preguntas=None):
    if not preguntas_l:
        print("No hay preguntas disponibles.")
        return

    # Seleccionar preguntas al azar
    preguntas_a_usar = rd.sample(preguntas_l, num_preguntas or len(preguntas_l))
    correctas = 0

    for i, pregunta_d in enumerate(preguntas_a_usar, start=1):
        print(f"\nPregunta {i}: {pregunta_d['pregunta']}")
        opciones = pregunta_d["opciones_l"]
        for j, opcion in enumerate(opciones, start=1):
            print(f"{j}. {opcion}")

        try:
            respuesta_usuario = int(input("Seleccione una opción: ")) - 1
            if opciones[respuesta_usuario] == pregunta_d["respuesta"]:
                print("¡Correcto!")
                correctas += 1
            else:
                print(f"Incorrecto. La respuesta correcta es: {pregunta_d['respuesta']}")
        except (ValueError, IndexError):
            print("Respuesta inválida. Por favor, ingrese un número válido.")

    print(f"\nHas respondido correctamente a {correctas} de {len(preguntas_a_usar)} preguntas.")

# Definir el menú
def menu():
    if not preguntas_l:
        print("No se encontraron preguntas en la base de datos.")
        return

    while True:
        os.system("clear")
        print("Menu")
        print("1. Empezar el test.")
        print("2. Elegir un número de preguntas.")
        print("3. Salir.")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            test_preguntas()
        elif opcion == "2":
            while True:
                try:
                    num_preguntas = int(input(f"Ingrese el número de preguntas (1-{len(preguntas_l)}): "))
                    if 1 <= num_preguntas <= len(preguntas_l):
                        test_preguntas(num_preguntas)
                        break
                    else:
                        print(f"Por favor, ingrese un número entre 1 y {len(preguntas_l)}.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            os.system("clear")
            exit()
            break

# Función principal
def main():
    os.system("clear")
    construir_preguntas()  # Llenar preguntas_l con datos de la base de datos
    menu()

if __name__ == "__main__":
    main()
