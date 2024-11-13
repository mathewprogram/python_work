import os, sqlite3
from herencia_futbol import *
from tabulate import tabulate

seleccionfutbol_lo = []

def menu():
    
    while True:
        os.system("clear")
        print("\nMenú:")
        print("1. Crear base de datos.")
        print("2. Ver contenido de la base de datos.")
        print("3. Crear objetos y guadarlos en una lista.")
        print("4. Mostrar objetos.")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            os.system("clear")
            crear_base_datos()
            input("Presiona Enter para continuar...")
        if opcion == "2":
            os.system("clear")
            ver_datos()
            input("Presiona Enter para continuar...")    
        if opcion == "3":
            os.system("clear")
            obtener_lista_seleccionfutbol_objeto()
            #crear_lista_objetos()
            input("Presiona Enter para continuar...")
        elif opcion == "4":
            os.system("clear")
            mostrar_lista_objetos()
            input("Presiona Enter para continuar...")
        elif opcion == "5":
            os.system("clear")
            print("Adios.")    
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def get_connection():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_objetos/db_footbol.sqlite3"
    connection = None
    try:
        connection = sqlite3.connect(nra)
    except sqlite3.Error as error:
        connection = None
    return connection

def crear_base_datos():  # sourcery skip: extract-method
    connection = get_connection()
    if connection != None:
        print("OK: CONEXION")
        try:
            cursor = connection.cursor()

            # Crear las tablas
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS SeleccionFutbol (
                id_seleccionfutbol TEXT    PRIMARY KEY,
                nombre             TEXT    NOT NULL,
                apellidos          TEXT    NOT NULL,
                edad               INTEGER NOT NULL
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Futbolista (
                id_futbolista      TEXT    PRIMARY KEY,
                dorsal             INTEGER NOT NULL,
                posicion        TEXT    NOT NULL,
                FOREIGN KEY (id_futbolista) REFERENCES SeleccionFutbol (id_seleccionfutbol)
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Masajista (
                id_masajista       TEXT    PRIMARY KEY,
                titulacion         TEXT    NOT NULL,
                anios_experiencia   INTEGER NOT NULL,
                FOREIGN KEY (id_masajista) REFERENCES SeleccionFutbol (id_seleccionfutbol)
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Entrenador (
                id_entrenador TEXT    PRIMARY KEY,
                id_federacion INTEGER NOT NULL,
                FOREIGN KEY (id_entrenador) REFERENCES SeleccionFutbol (id_seleccionfutbol)
            )
            ''')

                    # Insertar datos en la tabla SeleccionFutbol
            seleccion_futbol = [
                ('S001', 'Juan', 'Perez', 30),
                ('S002', 'Carlos', 'Lopez', 28),
                ('S003', 'Andres', 'Martinez', 32),
                ('S004', 'Luis', 'Garcia', 27),
                ('S005', 'Miguel', 'Rodriguez', 31),
                ('S006', 'Fernando', 'Fernandez', 29),
                ('S007', 'Pablo', 'Sanchez', 26),
                ('S008', 'Jorge', 'Ramirez', 33),
                ('S009', 'Roberto', 'Diaz', 25),
                ('S010', 'Raul', 'Cruz', 34),
                ('S011', 'Oscar', 'Jimenez', 28),
                ('S012', 'Mario', 'Vargas', 31),
                ('S013', 'Daniel', 'Herrera', 27),
                ('S014', 'Gabriel', 'Torres', 29),
                ('S015', 'Adrian', 'Castro', 30),
                ('S016', 'Francisco', 'Gomez', 26),
                ('S017', 'Ricardo', 'Ruiz', 32),
                ('S018', 'Victor', 'Mendoza', 28),
                ('S019', 'Diego', 'Ortiz', 33),
                ('S020', 'Ivan', 'Silva', 27),
                ('S021', 'Sergio', 'Morales', 25),
                ('S022', 'Edgar', 'Navarro', 31),
                ('S023', 'Martin', 'Rios', 29),
                ('S024', 'Enrique', 'Flores', 26),
                ('S025', 'Tomas', 'Gutierrez', 32),
                ('S026', 'Hugo', 'Peña', 30),
                ('S027', 'Alberto', 'Castillo', 27),
                ('S028', 'Alejandro', 'Aguilar', 31),
                ('S029', 'Javier', 'Mendez', 28),
                ('S030', 'Angel', 'Carrillo', 34),
                ('S031', 'Emilio', 'Salazar', 33),
                ('S032', 'Samuel', 'Vera', 29),
                ('S033', 'Benjamin', 'Soto', 26),
                ('S034', 'Cristian', 'Chavez', 30),
                ('S035', 'Lucas', 'Arias', 25),
                ('S036', 'Nicolas', 'Delgado', 27),
                ('S037', 'Marcelo', 'Fuentes', 32),
                ('S038', 'Antonio', 'Romero', 29),
                ('S039', 'Manuel', 'Ibanez', 28),
                ('S040', 'Sebastian', 'Mejia', 31)
            ]

            cursor.executemany("INSERT INTO SeleccionFutbol (id_seleccionfutbol, nombre, apellidos, edad) VALUES (?, ?, ?, ?)", seleccion_futbol)

            # Insertar datos en Futbolista
            futbolistas = [
                ('S001', 9, 'Delantero'), ('S002', 4, 'Defensa'), ('S003', 10, 'Delantero'),
                ('S004', 5, 'Medio'), ('S005', 3, 'Defensa'), ('S006', 8, 'Medio'),
                ('S007', 11, 'Portero'), ('S008', 6, 'Lateral'), ('S009', 7, 'Delantero'),
                ('S010', 2, 'Defensa')
            ]
            cursor.executemany("INSERT INTO Futbolista (id_futbolista, dorsal, posicion) VALUES (?, ?, ?)", futbolistas)

            # Insertar datos en Masajista
            masajistas = [
                ('S011', 'Fisioterapia', 5), ('S012', 'Rehabilitacion', 3), ('S013', 'Deporte', 7),
                ('S014', 'Masaje', 4), ('S015', 'Terapia Deportiva', 6), ('S016', 'Recuperación', 8),
                ('S017', 'Fisioterapia', 2), ('S018', 'Rehabilitacion', 5), ('S019', 'Kinesiología', 3),
                ('S020', 'Masoterapia', 6)
            ]
            cursor.executemany("INSERT INTO Masajista (id_masajista, titulacion, anios_experiencia) VALUES (?, ?, ?)", masajistas)

            # Insertar datos en Entrenador
            entrenadores = [
                ('S021', 1001), ('S022', 1002), ('S023', 1003), ('S024', 1004), ('S025', 1005),
                ('S026', 1006), ('S027', 1007), ('S028', 1008), ('S029', 1009), ('S030', 1010)
            ]
            cursor.executemany("INSERT INTO Entrenador (id_entrenador, id_federacion) VALUES (?, ?)", entrenadores)

            # Guardar y cerrar conexión
            connection.commit()
            connection.close()
            print("OK: CREAR BASE DATOS")
        except Exception as e:
            print("ERROR: CREAR BASE DATOS")
    else:
        print("ERROR: CONEXION")

def ver_datos():
    connection = get_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()

            # Consultar y mostrar los registros de la tabla SeleccionFutbol
            print("Datos de la tabla SeleccionFutbol:")
            cursor.execute("SELECT * FROM SeleccionFutbol")
            seleccion_futbol = cursor.fetchall()
            print(tabulate(seleccion_futbol, headers=['ID Selección', 'Nombre', 'Apellidos', 'Edad'], tablefmt='fancy_grid'))

            # Consultar y mostrar los registros de la tabla Futbolista
            print("\nDatos de la tabla Futbolista:")
            cursor.execute("SELECT * FROM Futbolista")
            futbolista = cursor.fetchall()
            print(tabulate(futbolista, headers=['ID Futbolista', 'Dorsal', 'Posición', 'ID Selección'], tablefmt='fancy_grid'))

            # Consultar y mostrar los registros de la tabla Masajista
            print("\nDatos de la tabla Masajista:")
            cursor.execute("SELECT * FROM Masajista")
            masajista = cursor.fetchall()
            print(tabulate(masajista, headers=['ID Masajista', 'Titulación', 'Años de Experiencia', 'ID Selección'], tablefmt='fancy_grid'))

            # Consultar y mostrar los registros de la tabla Entrenador
            print("\nDatos de la tabla Entrenador:")
            cursor.execute("SELECT * FROM Entrenador")
            entrenador = cursor.fetchall()
            print(tabulate(entrenador, headers=['ID Entrenador', 'ID Federación', 'ID Selección'], tablefmt='fancy_grid'))

            # Cerrar la conexión
            connection.close()
        except Exception as e:
            print(f"Error al consultar los datos: {e}")
    else:
        print("Error en la conexión.")


def crear_lista_objetos():
    delBosque = Entrenador(1, "Vicente", "Del Bosque", 60, "284EZ89")  # noqa: F405
    zidane = Futbolista(2, "Zinedine", "Zidane", 29, 5, "Medio Central")  # noqa: F405
    raulMartinez = Masajista(3, "Raúl", "Martinez", 41, "Licenciado en Fisioterapia", 18)  # noqa: F405
    seleccionfutbol_lo.append(delBosque)
    seleccionfutbol_lo.append(zidane)
    seleccionfutbol_lo.append(raulMartinez)


def mostrar_lista_objetos():
    seleccionfutbol_lo = obtener_lista_seleccionfutbol_objeto()
    print(f"Lista obtenida: {seleccionfutbol_lo}")
    for seleccion_o in seleccionfutbol_lo:
        print(seleccion_o.nombre, end=" es ")
        if isinstance(seleccion_o, Entrenador):  # noqa: F405
            print("Entrenador")
        elif isinstance(seleccion_o, Futbolista):  # noqa: F405
            print("Futbolista")
        elif isinstance(seleccion_o, Masajista):  # noqa: F405
            print("Masajista")

def obtener_lista_seleccionfutbol_objeto():
    connection = get_connection()
    if connection is not None:
        cursor = connection.cursor()
        seleccionfutbol_lo = []
        try:
            # Consulta principal para SeleccionFutbol
            query_seleccionfutbol = "SELECT * FROM SeleccionFutbol"
            cursor.execute(query_seleccionfutbol)
            seleccionfutbol_lt = cursor.fetchall()
            
            for seleccionfutbol_t in seleccionfutbol_lt:
                if len(seleccionfutbol_t) == 4:
                    id_seleccionfutbol, nombre, apellidos, edad = seleccionfutbol_t
                else:
                    print(f"Registro inesperado en SeleccionFutbol: {seleccionfutbol_t}")
                    continue

                # Consultar en Futbolista
                cursor.execute("SELECT * FROM Futbolista WHERE id_futbolista = ?", (id_seleccionfutbol,))
                futbolista_lt = cursor.fetchone()
                if futbolista_lt and len(futbolista_lt) == 4:
                    id_futbolista, dorsal, posicion, id_seleccionfutbol_fut = futbolista_lt
                    futbolista_o = Futbolista(id_futbolista, nombre, apellidos, edad, dorsal, posicion)
                    seleccionfutbol_lo.append(futbolista_o)

                # Consultar en Masajista
                cursor.execute("SELECT * FROM Masajista WHERE id_masajista = ?", (id_seleccionfutbol,))
                masajista_lt = cursor.fetchone()
                if masajista_lt and len(masajista_lt) == 4:
                    id_masajista, titulacion, anios_experiencia, id_seleccionfutbol_mas = masajista_lt
                    masajista_o = Masajista(id_masajista, nombre, apellidos, edad, titulacion, anios_experiencia)
                    seleccionfutbol_lo.append(masajista_o)

                # Consultar en Entrenador
                cursor.execute("SELECT * FROM Entrenador WHERE id_entrenador = ?", (id_seleccionfutbol,))
                entrenador_lt = cursor.fetchone()
                if entrenador_lt and len(entrenador_lt) == 3:
                    id_entrenador, id_federacion, id_seleccionfutbol_ent = entrenador_lt
                    entrenador_o = Entrenador(id_entrenador, nombre, apellidos, edad, id_federacion)
                    seleccionfutbol_lo.append(entrenador_o)

            # Cerrar la conexión
            connection.close()
            return seleccionfutbol_lo

        except Exception as e:
            print(f"Error al consultar los datos: {e}")

def main():
    menu()
    
if __name__ == "__main__":
    main()

