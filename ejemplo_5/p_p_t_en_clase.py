import os
import random
import regex as re

# Variables globales para la puntuación
puntuacion_jugador = 0
puntuacion_maquina = 0

def menu():
    while True:
        print("\nMenú:")
        print("1. Jugar con un número personalizado de jugadas")
        print("2. Jugar al mejor de tres")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            jugadas_personalizadas()
        elif opcion == "2":
            mejor_de_tres()
        elif opcion == "3":
            print("Gracias por jugar.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def jugadas_personalizadas():
    global puntuacion_jugador, puntuacion_maquina
    puntuacion_jugador = 0
    puntuacion_maquina = 0
    empate = 0 

    numero_jugadas = int(input("¿Cuántas jugadas quieres hacer?: "))

    for i in range(numero_jugadas):
        maquina = random.choice(["piedra", "papel", "tijera"])
        usuario = entrada_usuario("Ingresa piedra, papel o tijera: ")
        resultado = obtener_resultado(usuario, maquina)
        
        print(f"Máquina eligió: {maquina}")
        print(f"Resultado: {resultado}\n")
        
        if resultado == "Empate":
            empate += 1
        elif resultado == "Ganas":
            puntuacion_jugador += 1
        else:
            puntuacion_maquina += 1
        
        print(f"Empate: {empate}, Ganaste: {puntuacion_jugador}, Perdiste: {puntuacion_maquina}")

    # Resultado final
    print("\n--- Resultado final ---")
    print(f"Empates: {empate}, Ganaste: {puntuacion_jugador}, Perdiste: {puntuacion_maquina}")

def mejor_de_tres():
    global puntuacion_jugador, puntuacion_maquina
    puntuacion_jugador = 0
    puntuacion_maquina = 0
    empate = 0 

    for i in range(3):
        maquina = random.choice(["piedra", "papel", "tijera"])
        usuario = entrada_usuario("Ingresa piedra, papel o tijera: ")
        resultado = obtener_resultado(usuario, maquina)
        
        print(f"Máquina eligió: {maquina}")
        print(f"Resultado: {resultado}\n")
        
        if resultado == "Empate":
            empate += 1
        elif resultado == "Ganas":
            puntuacion_jugador += 1
        else:
            puntuacion_maquina += 1
        
        print(f"Empate: {empate}, Ganaste: {puntuacion_jugador}, Perdiste: {puntuacion_maquina}")

    # Resultado final para mejor de tres
    if puntuacion_jugador > puntuacion_maquina:
        print("\n¡Ganaste el mejor de tres!")
    elif puntuacion_maquina > puntuacion_jugador:
        print("\nPerdiste el mejor de tres.")
    else:
        print("\n¡Es un empate!")

def entrada_usuario(mensaje):
    patron = ["piedra", "papel", "tijera"]
    while True:
        cadena = input(mensaje).lower()
        if cadena in patron:
            return cadena
        else:
            print("Entrada no válida. Por favor, ingresa piedra, papel o tijera.")

def obtener_resultado(usuario, maquina):
    if usuario == maquina:
        return "Empate"
    elif (usuario == "piedra" and maquina == "tijera") or \
         (usuario == "papel" and maquina == "piedra") or \
         (usuario == "tijera" and maquina == "papel"):
        return "Ganas"
    else:
        return "Pierdes"

def main():
    os.system("clear")
    menu()

if __name__ == "__main__":
    main()
