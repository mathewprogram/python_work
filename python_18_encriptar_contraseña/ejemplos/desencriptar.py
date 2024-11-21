import sqlite3, bcrypt

def get_connection():
    nra = ("/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/"
           "python_18_encriptar_contraseña/ferreteria.sqlite3")
    connection = None
    try:
        connection = sqlite3.connect(nra)
    except sqlite3.Error as error:
        connection = None
    return connection

nombre_usuario = input("Nombre de usuario: ")
contrasena = input("Contraseña: ")

connection = get_connection()

cursor = connection.cursor()
sql = "SELECT contrasena FROM Usuario WHERE nombre_usuario = ?"
cursor.execute(sql, (nombre_usuario,))
contrasena_t = cursor.fetchone()
contrasena_hashed = contrasena_t[0]  # esto corresponde a la contraseña encriptada

contrasena_byte = contrasena.encode()
print(f"Contraseña ingresada: {contrasena}")
print(f"Contraseña encriptada: {contrasena_hashed.encode()}")

if bcrypt.checkpw(contrasena_byte, contrasena_hashed.encode()):
    print(f"Contraseña correcta.")
else:
    print("Contraseña incorrecta.")