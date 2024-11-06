import os
import random as rd

#Base de datos
letras_l = ["A", "B", "C", "D"]
preguntas_l = [
     {
        "pregunta": "La función principal del sistema operativo es:",
        "opciones_l": [
            "Facilitar el uso de la computadora al usuario.",
            "Hacer la programación más fácil para los programadores.",
            "Administrar recursos.",
            "Todas las anteriores"],
        "respuesta": letras_l[3]
    },    
    {
        "pregunta": "Las partes de un sistema operativo son:",
        "opciones_l": [
            "Núcleo, drivers y programas.",
            "Núcleo, consola de comandos y aplicaciones.",
            "Núcleo, intérprete de comandos y sistema de archivos. ",
            "Sistema de archivos, compiladores / intérpretes y administrador de recursos."
        ],
        "respuesta": letras_l[2]
    },
    {
        "pregunta": "Para poder programar un algoritmo:",
        "opciones_l": [
            "Debe tener un número infinito de pasos.",
            "Debe tener al menos una salida.",
            "Cada paso debe ser escrito lo más corto posible. ",
            "Ninguna de las anteriores."
        ],
        "respuesta": letras_l[2]
    },
    {
        "pregunta": "El ensamblador y el código máquina son:",
        "opciones_l": [
            "Lenguajes de programación de bajo nivel. ",
            "Lenguajes de programación de alto nivel.",
            "Parte del sistema operativo.",
            "Entornos de programación."
        ],
        "respuesta": letras_l[0]
    },
    {
        "pregunta": "El compilador de Python permite ejecutar un archivo con extensión .py:",
        "opciones_l": [
            "Siempre que se ejecute como superusuario.",
            "Verdadero. ",
            "Falso. Python no tiene compilador.",
            "Falso. Los archivos .py no pueden ser ejecutados."
        ],
        "respuesta": letras_l[1]
    },
    {
        "pregunta": "La parte de la computadora responsable de realizar cálculos aritméticos y lógicos se llama:",
        "opciones_l": [
            "RAM",
            "CPU ",
            "ROM",
            "Registros"
        ],
        "respuesta": letras_l[1]
    },
    {
        "pregunta": "¿Qué tipo de salidas de energía tiene el bus GPIO?",
        "opciones_l": [
            "De 3.3V y 5V ",
            "No tiene salidas de energía",
            "SPI e I2C",
            "PoE (Power over Ethernet)"
        ],
        "respuesta": letras_l[0]
    },
    {
        "pregunta": "La memoria ROM...",
        "opciones_l": [
            "Es volátil",
            "Tiene gran capacidad",
            "Almacena las instrucciones de arranque del procesador ",
            "Almacena el sistema operativo del procesador"
        ],
        "respuesta": letras_l[2]
    },
    {
        "pregunta": "El siguiente comando de la consola $ mv blink.py blink2.py",
        "opciones_l": [
            "Renombra el archivo blink.py como blink2.py ",
            "Es incorrecto.",
            "Renombra el archivo blink2.py como blink.py",
            "Mueve el archivo blink.py a home."
        ],
        "respuesta": letras_l[0]
    },
    {
        "pregunta": "¿Cuál de las siguientes reglas no es correcta?",
        "opciones_l": [
            "Un símbolo de decisión puede ser alcanzado por varias líneas.",
            "Varias líneas pueden llegar a un símbolo de proceso.",
            "Todos los símbolos deben estar conectados.",
            "Todas las líneas que queramos pueden salir de un símbolo de decisión. "
        ],
        "respuesta": letras_l[3]
    }
]

def seleccionar_preguntas(num_preguntas):
    """Selecciona un número específico de preguntas aleatoriamente."""
    if num_preguntas > len(preguntas_l):
        num_preguntas = len(preguntas_l)  # Limita a la cantidad total de preguntas
    return rd.sample(preguntas_l, num_preguntas)
# Definir la función de test antes de usarla
def test_preguntas(num_preguntas=None):
    score = 0
    # Determinar las preguntas a utilizar
    preguntas_seleccionadas = (
        rd.sample(preguntas_l, min(num_preguntas, len(preguntas_l))) if num_preguntas else preguntas_l
    )

    # Iterar sobre cada pregunta seleccionada
    for idx, pregunta in enumerate(preguntas_seleccionadas):
        print(f"\nPregunta {idx + 1}: {pregunta['pregunta']}")
        for letra, opcion in zip(letras_l, pregunta['opciones_l']):
            print(f"{letra}: {opcion}")

        # Validar la respuesta del usuario
        respuesta_usuario = input("Seleccione su respuesta (A, B, C, D): ").upper()
        while respuesta_usuario not in letras_l:
            print("Opción no válida. Por favor, elija A, B, C o D.")
            respuesta_usuario = input("Seleccione su respuesta (A, B, C, D): ").upper()

        # Comparar respuesta con la correcta
        if respuesta_usuario == pregunta['respuesta']:
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}.")

    # Mostrar el puntaje final
    while True:
        print(f"\nSu puntuación es: {score}/{len(preguntas_seleccionadas)}")
        input("Presione Enter para ir al Menu...")
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
            while True:  # Bucle para validar la entrada
                try:
                    num_preguntas = int(input(f"Ingrese el número de preguntas (1-{len(preguntas_l)}): "))
                    if 1 <= num_preguntas <= len(preguntas_l):
                        test_preguntas(num_preguntas)
                        break  # Salir del bucle si la entrada es válida
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

#Funcion para hacer un test de preguntas
"""
def test_preguntas():
    preguntas = input("¿Desea realizar un test de preguntas? (si/no): ")
    if preguntas.lower() == "si":
        score = 0
        total_preguntas = len(preguntas_l)

        # Solicitar la cantidad de preguntas que desea
        while True:
            try:
                num_preguntas = int(input("¿Cuántas preguntas desea (máximo {})? ".format(total_preguntas)))
                if 1 <= num_preguntas <= total_preguntas:
                    break
                else:
                    print(f"Por favor ingrese un número entre 1 y {total_preguntas}.")
            except ValueError:
                print("Entrada no válida. Debe ser un número.")

        rd.shuffle(preguntas_l)  # Mezclar las preguntas

        for idx in range(num_preguntas):
            pregunta = preguntas_l[idx]
            print(f"\nPregunta {idx + 1}: {pregunta['pregunta']}")
            for letra, opcion in zip(letras_l, pregunta['opciones_l']):
                print(f"{letra}: {opcion}")

            respuesta_usuario = input("Seleccione su respuesta (A, B, C, D): ").lower().upper()
            while respuesta_usuario not in letras_l:
                print("Opción no válida. Por favor, elija A, B, C o D.")
                respuesta_usuario = input("Seleccione su respuesta (A, B, C, D): ").lower().upper()

            if respuesta_usuario == pregunta['respuesta']:
                print("¡Correcto!")
                score += 1
            else:
                print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}.")

        print(f"\nSu puntuación es: {score}/{num_preguntas}")
    elif preguntas.lower().upper() == "no":
        print("Gracias por usar este programa")
        exit()
    else:
        print("Entrada no válida. Por favor ingrese 'si' o 'no'.")

# Ejecutar la función del test
test_preguntas()
"""