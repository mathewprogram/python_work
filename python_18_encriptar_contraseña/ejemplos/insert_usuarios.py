import sys, sqlite3, bcrypt
from PySide6.QtWidgets import (
    QFormLayout, QApplication, QMainWindow, 
    QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QCheckBox, QRadioButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QHBoxLayout, QVBoxLayout
    )
from PySide6.QtGui import QIcon, QFont, Qt

# Funciones
def cambiar_rol():
    pass

def insert():
    connection = get_connection()
    QMessageBox.information(None, "Data", "Connection established.")
    if connection is not None:
        try:
            cursor = connection.cursor()
            nombre_usuario = txtNombreUsuario.text()
            contrasena = txtContrasena.text()
            rol = cboRol.currentText()
            sql = """INSERT INTO Usuario (nombre_usuario, contrasena, rol) 
                        VALUES (?, ?, ?);"""
            #contrasena = encriptar_contrasena(contrasena)
            cursor.execute(sql, (nombre_usuario, encriptar_contrasena(contrasena), rol))
            connection.commit()
            QMessageBox.information(None, "Data", "Data inserted.")
        except sqlite3.Error as error:
            QMessageBox.critical(None, "Error", "Query failed.")
    else:
        QMessageBox.critical(None, "Error", "Connection failed.")


def encriptar_contrasena(contrasena):
    # Convertir la contraseña en bytes
    contrasena_byte = contrasena.encode()
    # Encriptar la contraseña
    contrasena_hashed = bcrypt.hashpw(contrasena_byte, bcrypt.gensalt())
    return contrasena_hashed.decode()

def get_connection():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_18_encriptar_contraseña/ferreteria.sqlite3"
    connection = None
    try:
        connection = sqlite3.connect(nra)
    except sqlite3.Error as error:
        connection = None
    return connection

def crear_tabla():
    connection = get_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            # Ejecutar cada sentencia SQL por separado
            cursor.execute("""
            CREATE TABLE Usuario (
                id_usuario  INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_usuario      TEXT NOT NULL UNIQUE,
                contrasena          TEXT NOT NULL,
                rol                 TEXT NOT NULL CHECK (rol IN ('Admin', 'Cajero', 'Almacen'))
            );
            """)
            cursor.execute("""
            CREATE TABLE Venta (
                id_venta    INTEGER PRIMARY KEY AUTOINCREMENT,
                producto    TEXT NOT NULL,
                fecha_venta TEXT NOT NULL,
                total       REAL NOT NULL
            );
            """)
            cursor.execute("""
            CREATE TABLE Producto (
                id_producto  INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_producto     TEXT NOT NULL,
                precio              REAL NOT NULL,
                stock               INTEGER NOT NULL
            );
            """)
            connection.commit()
            QMessageBox.information(None, "Data", "Tablas creadas correctamente")
        except sqlite3.Error as error:
            QMessageBox.critical(None, "Error", f"Error al crear las tablas: {error}")
        finally:
            connection.close()
    else:
        QMessageBox.critical(None, "Error", "Error de conexión a la base de datos")

# Llamar a la función para crear las tablas



# 0. CONSTRUIR UNA APLICACION
app = QApplication(sys.argv) #<------------

# 1. CREAR LA VENTANA PRINCIPAL
ventana_principal = QMainWindow()

# 2. CREAR UN PANEL Principal
panel_principal = QWidget()

# 3. CREAR UN ADMINISTRADOR Principal DEL PANEL
layout_principal = QFormLayout()

# 4. CREAR COMPONENTES Y GESTIONARLOS CON EL ADMINISTRADOR
lblNombreUsuario = QLabel("Nombre:")
lblNombreUsuario.setFixedWidth(72)  # cambiar el tamaño de la etiqueta
txtNombreUsuario = QLineEdit()

lblContrasena = QLabel("Contraseña:")
txtContrasena = QLineEdit()
txtContrasena.setEchoMode(QLineEdit.Password)

btnTogglePassword = QPushButton("🙈")
btnTogglePassword.setCheckable(True)  # Hacer que el botón sea conmutador (toggle)
btnTogglePassword.setFixedSize(30, 30)

# Función para alternar la visibilidad
def toggle_password_visibility():
    if btnTogglePassword.isChecked():
        txtContrasena.setEchoMode(QLineEdit.Normal)  # Mostrar texto
        btnTogglePassword.setText("👁")  # Cambiar ícono
    else:
        txtContrasena.setEchoMode(QLineEdit.Password)  # Ocultar texto
        btnTogglePassword.setText("🙈")  # Cambiar ícono de vuelta

# Conectar la señal del botón a la función
btnTogglePassword.clicked.connect(toggle_password_visibility)

# Crear un contenedor horizontal para la contraseña y el botón
password_layout = QHBoxLayout()
password_layout.addWidget(txtContrasena)
password_layout.addWidget(btnTogglePassword)

cboRol = QComboBox()
cboRol.setFont(QFont("Courier New", 14, QFont.Bold))
cboRol.addItem("Seleccione rol")
cboRol.addItem("Admin")
cboRol.addItem("Cajero")
cboRol.addItem("Almacén")
cboRol.currentIndexChanged.connect(cambiar_rol)
btnCrearTabla = QPushButton("Crear tabla")
btnCrearTabla.clicked.connect(crear_tabla)

btnInsert = QPushButton("Insert")
btnInsert.clicked.connect(insert)

btnExit = QPushButton("Exit")
btnExit.clicked.connect(sys.exit)

# Crear un layout horizontal para los botones
button_layout = QHBoxLayout()
button_layout.addWidget(btnCrearTabla)
button_layout.addWidget(btnInsert)
button_layout.addWidget(btnExit)

# Agregando etiquetas y campos de entrada
layout_principal.addRow(lblNombreUsuario, txtNombreUsuario)
layout_principal.addRow(lblContrasena, password_layout)  # Usar el layout horizontal
layout_principal.addRow(" ", cboRol)
layout_principal.addRow(button_layout)



# 5. ASIGNAR EL ADMINISTRADOR AL PANEL
panel_principal.setLayout(layout_principal)

# 6. PONER EL PANEL A LA VENTANA PRINCIPAL
ventana_principal.setCentralWidget(panel_principal)

# 7. MOSTRAR VENTANA PRINCIPAL
ventana_principal.show()

# 8. EJECUTAR APLICACION
sys.exit(app.exec())        #<------------