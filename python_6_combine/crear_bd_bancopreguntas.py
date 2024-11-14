#!/usr/bin/env python
# -*- coding: utf8 -*-
import sqlite3, os

letras_l = ["A", "B", "C", "D"]
preguntas_ld = [
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


def menu():
    pass


def get_connection():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_combine/bancopreguntas.sqlite3"
    connection = None
    try:
       connection = sqlite3.connect(nra)
    except sqlite3.Error as error:
       connection = None
    return connection

def create_tables_bancopreguntas():
    connection = get_connection();
    if connection != None:
        print("Connection established.")
        cursor = connection.cursor()
        try:
            query_pregunta = """CREATE TABLE IF NOT EXISTS Pregunta (
                        idPregunta    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        pregunta      TEXT NOT NULL,
                        respuesta     CHAR(1) NOT NULL);
                            """
            cursor.execute(query_pregunta)
            print("Table 'Preguntas' created.")
            query_opcion =  """CREATE TABLE IF NOT EXISTS Opcion (
                                idOpcion      INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
                                idPregunta    INTEGER     NOT NULL,
                                opcion        TEXT    NOT NULL,
                                letra         CHAR(1) NOT NULL,
                                FOREIGN KEY (idPregunta)
                                REFERENCES Pregunta (idPregunta));
                            """
            cursor.execute(query_opcion)
            print("Table 'Opcion' created.")
            connection.commit()  # Guarda los cambios
        except Exception as e:
            print("Error: {}".format(e))
        cursor.close()
    else:   
        print("Error de conexión.")

def insert_preguntas():
    connection = get_connection();
    if connection != None:
        cursor = connection.cursor()
        try:
            query_preguntas = "INSERT INTO Pregunta (pregunta, respuesta) VALUES (?, ?);"
            query_opciones = "INSERT INTO Opcion (idPregunta, opcion, letra) VALUES (?, ?, ?);"
            for pregunta_d in preguntas_ld:
                pregunta = pregunta_d["pregunta"]
                respuesta = pregunta_d["respuesta"]
                cursor.execute(query_preguntas, (pregunta, respuesta))
                #Grabar pregunta y respuesta(Tabla Pregunta)
                id_pregunta = cursor.lastrowid
                opciones_l = pregunta_d["opciones_l"]
                for letra, opcion in zip(letras_l, opciones_l):
                    #Grabar id_pregunta, opcion, letra
                    cursor.execute(query_opciones, (id_pregunta, opcion, letra)) 
            connection.commit()
            print("Preguntas insertadas.")
        except Exception as e:  
            print("Error: {}".format(e))
        cursor.close()


def main():
    os.system("clear")
    create_tables_bancopreguntas()
    insert_preguntas()
    menu()
          
if __name__ == "__main__":
   main()

