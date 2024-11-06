#Esta es una version mia del test. El otro archivo es 
#la version que hicimos en clase 

import os, sqlite3
import random as rd

#Base de datos
def get_connection():
    return sqlite3.connect("/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_combine/bancopreguntas.sqlite3")

# Cargar preguntas de la base de datos
def cargar_preguntas():
    connection = get_connection()
    cursor = connection.cursor()
    preguntas_l = []

    try:
        # Obtener todas las preguntas con sus opciones
        query_preguntas = "SELECT idPregunta, pregunta, respuesta FROM Pregunta;"
        cursor.execute(query_preguntas)
        preguntas_bd = cursor.fetchall()

        for pregunta in preguntas_bd:
            id_pregunta, texto_pregunta, respuesta = pregunta
            query_opciones = "SELECT letra, opcion FROM Opcion WHERE idPregunta = ?;"
            cursor.execute(query_opciones, (id_pregunta,))
            opciones = cursor.fetchall()
            opciones_dict = [opcion[1] for opcion in opciones]
            letras = [opcion[0] for opcion in opciones]
            
            # Agregar pregunta con opciones al listado
            preguntas_l.append({
                "pregunta": texto_pregunta,
                "respuesta": respuesta,
                "opciones_l": opciones_dict,
                "letras_l": letras
            })
    except Exception as e:
        print(f"Error al cargar preguntas: {e}")
    finally:
        cursor.close()
        connection.close()

    return preguntas_l

# Función de test
def test_preguntas(num_preguntas=None):
    preguntas_l = cargar_preguntas()  # Cargar preguntas desde la BD
    if not preguntas_l:
        print("No se encontraron preguntas en la base de datos.")
        return
    
    score = 0
    preguntas_seleccionadas = (
        rd.sample(preguntas_l, min(num_preguntas, len(preguntas_l))) if num_preguntas else preguntas_l
    )

    for idx, pregunta in enumerate(preguntas_seleccionadas):
        print(f"\nPregunta {idx + 1}: {pregunta['pregunta']}")
        for letra, opcion in zip(pregunta['letras_l'], pregunta['opciones_l']):
            print(f"{letra}: {opcion}")

        respuesta_usuario = input("Seleccione su respuesta (A, B, C, D): ").upper()
        while respuesta_usuario not in pregunta['letras_l']:
            print("Opción no válida. Por favor, elija A, B, C o D.")
            respuesta_usuario = input("Seleccione su respuesta (A, B, C, D): ").upper()

        if respuesta_usuario == pregunta['respuesta']:
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}.")

    print(f"\nSu puntuación es: {score}/{len(preguntas_seleccionadas)}")
    input("Presione Enter para ir al Menú...")
    menu()

# Definir el menú
def menu():
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
                    preguntas_l = cargar_preguntas()  # Cargar preguntas para contar
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
    menu()

if __name__ == "__main__":
    main()