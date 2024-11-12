import os, sqlite3

trabajadores_ld = [
    {
        'id_trabajador': 'T1',
        'nombre': 'Juan',
        'apellido': 'Peña',
        'tipo_trabajador': "Conserje",
        'horas_trabajadas': 130,
        'incentivos': 0
    },
    {
        'id_trabajador': 'T2',
        'nombre': 'Pedro',
        'apellido': 'Perez',
        'tipo_trabajador': "Secretaria",
        'horas_trabajadas': 160,
        'incentivos': 200
    },
    {
        'id_trabajador': 'T3',
        'nombre': 'Maria',
        'apellido': 'Gutierrez',
        'tipo_trabajador': "Directivo",  
        'base': 1800,
        'dietas': 500,
        'metas': 600
    },
    {
        'id_trabajador': 'T4',
        'nombre': 'Luis',
        'apellido': 'Lopez',
        'tipo_trabajador': "Secretaria",  
        'horas_trabajadas': 200,
        'incentivos': 400,
    },
    {
        'id_trabajador': 'T5',
        'nombre': 'Mihai',
        'apellido': 'Matei',
        'tipo_trabajador': "Directivo",  
        'base': 6800,
        'dietas': 1000,
        'metas': 25000
    }
]



def get_connection():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_objetos/db_trabajador.sqlite3"
    connection = None
    try:
        connection = sqlite3.connect(nra)
    except sqlite3.Error as error:
        connection = None
    return connection


def creat_tables():
    connection = get_connection()
    if connection != None:
        cursor = connection.cursor()
        try:
            query_trabajador = """
                CREATE TABLE IF NOT EXISTS Trabajador (
                    id_trabajador TEXT NOT NULL PRIMARY KEY,
                    nombre        TEXT NOT NULL,
                    apellido      TEXT NOT NULL);
                            """         
            query_directivo = """
            CREATE TABLE IF NOT EXISTS Directivo (
                id_directivo TEXT     NOT NULL PRIMARY KEY,
                metas        INTEGER  NOT NULL,
                dietas       INTEGER  NOT NULL,
                base         INTEGER  NOT NULL,
                            FOREIGN KEY (id_directivo) REFERENCES Trabajador (id_trabajador));
                            """
            query_secretaria = """
            CREATE TABLE IF NOT EXISTS Secretaria (
                id_secretaria    TEXT    NOT NULL PRIMARY KEY,
                horas_trabajadas INTEGER NOT NULL,
                incentivos       INTEGER NOT NULL,
                                FOREIGN KEY (id_secretaria) REFERENCES Trabajador (id_trabajador));
                            """
            query_conserje = """
            CREATE TABLE IF NOT EXISTS Conserje (
                id_conserje       TEXT    NOT NULL PRIMARY KEY,
                horas_trabajadas  INTEGER NOT NULL,
                                FOREIGN KEY (id_conserje) REFERENCES Trabajador (id_trabajador));
                            """
            cursor.execute(query_trabajador)
            cursor.execute(query_directivo)
            cursor.execute(query_secretaria)
            cursor.execute(query_conserje)
            connection.commit()
            print("Tables created.")    
        except Exception as e:
            print("Error: {}".format(e))    
    else:
        print("Connection Error.")
    cursor.close()


def insert_data():
    connection = get_connection()
    if connection != None:
        cursor = connection.cursor()
        try:
            query_trabajador = "INSERT INTO Trabajador (id_trabajador, nombre, apellido) VALUES (?, ?, ?);"
            query_directivo = "INSERT INTO Directivo (id_directivo, metas, dietas, base) VALUES (?, ?, ?, ?);"
            query_secretaria = "INSERT INTO Secretaria (id_secretaria, horas_trabajadas, incentivos) VALUES (?, ?, ?);"
            query_conserje = "INSERT INTO Conserje (id_conserje, horas_trabajadas) VALUES (?, ?);"
            for trabajador in trabajadores_ld:
                id_trabajador = trabajador['id_trabajador']
                nombre = trabajador['nombre']
                apellido = trabajador['apellido']
                tipo_trabajador = trabajador['tipo_trabajador']
                cursor.execute(query_trabajador, (id_trabajador, nombre, apellido))
                if tipo_trabajador == "Directivo":
                    cursor.execute(query_directivo, (id_trabajador, trabajador['metas'], trabajador['dietas'], trabajador['base']))
                elif tipo_trabajador == "Secretaria":
                    cursor.execute(query_secretaria, (id_trabajador, trabajador['horas_trabajadas'], trabajador['incentivos']))
                elif tipo_trabajador == "Conserje":
                    cursor.execute(query_conserje, (id_trabajador, trabajador['horas_trabajadas']))
            connection.commit()
            print("Data inserted.")
        except Exception as e:
            print("Error: {}".format(e))    
    else:
        print("Connection Error.")
    cursor.close()


def main():
    os.system("clear")
    creat_tables()
    insert_data()

if __name__ == "__main__":
    main()
