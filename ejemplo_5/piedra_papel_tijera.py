"""
Empate Jugador = pc(Aleatorio)

Ganas Jugador Pc
      Piedra Gana Tijera
      Papel Gana Piedra
      Tijera Gana Papel
pierdes
"""

import random, os

def jugar():
    opciones = ['Piedra', 'Papel', 'Tijera']
    puntuacion_jugador = 0
    puntuacion_pc = 0

    while puntuacion_jugador < 3 and puntuacion_pc < 3:
        pc = random.choice(opciones)

        print("\nOpciones:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")

        # Solicitar al jugador que elija
        eleccion_jugador = input("Selecciona una opción (1/2/3): ")
        
        # Convertir la elección del jugador a una opción de texto
        if eleccion_jugador == '1':
            jugador = 'Piedra'
        elif eleccion_jugador == '2':
            jugador = 'Papel'
        elif eleccion_jugador == '3':
            jugador = 'Tijera'
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
            continue

        print(f"\nJugador: {jugador}")
        print(f"PC: {pc}")

        # Determinar el resultado
        if jugador == pc:
            print("¡Empate!")
        elif (jugador == 'Piedra' and pc == 'Tijera') or \
             (jugador == 'Papel' and pc == 'Piedra') or \
             (jugador == 'Tijera' and pc == 'Papel'):
            print("¡Ganas!")
            puntuacion_jugador += 1
        else:
            print("¡Pierdes!")
            puntuacion_pc += 1

        print(f"Score - Jugador: {puntuacion_jugador}, PC: {puntuacion_pc}")

    # Mostrar quién ganó el mejor de tres
    if puntuacion_jugador == 3:
        print("\n¡Felicidades! Ganaste el mejor de tres.")
    else:
        print("\n¡La PC ganó el mejor de tres!")

def main():
    while True:
        jugar()
        volver_a_jugar = input("\n¿Quieres volver a jugar? (s/n): ").lower()
        if volver_a_jugar != 's':
            print("¡Gracias por jugar!")
            os.system("clear")
            break
        
            
if __name__ == "__main__":
    main()
