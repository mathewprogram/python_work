import sys, os
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,
    QTableWidget, QAbstractItemView, QFormLayout, QLabel, QLineEdit,
    QComboBox)
from PySide6.QtGui import QIcon


class VentanaGestionUsuarios(QWidget):
    def __init__(self):
        super().__init__()
        self.personalizar_ventana()
        self.personalizar_componentes()
        self.cargar_datos()


    def personalizar_ventana(self):
        self.setWindowTitle("Gestión de usuarios")                          # Título de la ventana
        self.setFixedSize(600, 400)                                         # Tamaño de la ventana
        #self.setStyleSheet("background-color: lightgray; color: black;")   # Color de fondo

        # Cambiar el icono de la ventana con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta) # Imprime la ruta absoluta
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizar_componentes(self):
        layout = QVBoxLayout()

        # Tabla de usuarios
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Usuario", "Contraseña", "Rol"])
        #self.tabla.setStyleSheet("color: black; background-color: white;")
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.tabla)

        # Campos para CRUD
        self.txt_nombre_usuario = QLineEdit()
        self.txt_nombre_usuario.setPlaceholderText("Usuario")

        self.txt_contrasena = QLineEdit()
        self.txt_contrasena.setPlaceholderText("Contraseña")

        self.cbo_rol = QComboBox()
        self.cbo_rol.addItem("Seleccionar rol")
        self.cbo_rol.addItem("Administrador")
        self.cbo_rol.addItem("Cajero")
        self.cbo_rol.addItem("Almacén")

        self.btn_insertar = QPushButton("Insertar usuario")
        self.btn_insertar.clicked.connect(self.insertar_usuario)
        self.btn_actualizar = QPushButton("Actualizar usuario")
        self.btn_actualizar.clicked.connect(self.actualizar_usuario)
        self.btn_eliminar = QPushButton("Eliminar usuario")
        self.btn_eliminar.clicked.connect(self.eliminar_usuario)
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)

        insert_layout = QHBoxLayout()
        insert_layout.addWidget(self.txt_nombre_usuario)
        insert_layout.addWidget(self.txt_contrasena)
        insert_layout.addWidget(self.cbo_rol)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.btn_insertar)
        botones_layout.addWidget(self.btn_actualizar)
        botones_layout.addWidget(self.btn_eliminar)
        botones_layout.addWidget(self.btn_salir)        


        layout.addLayout(insert_layout)
        layout.addLayout(botones_layout)

        # Establecer el layout en la ventana principal
        self.setLayout(layout)

    def get_connection(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Passw0rd!",
            database="ferreteria"
        )
        return conexion

    def cargar_datos(self):
        connection = self.get_connection()

        if connection is not None:
            #QMessageBox.information(self, "Conexión exitosa", "Conexión a la base de datos exitosa")    
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Usuario")
                registros = cursor.fetchall()
                self.tabla.setRowCount(len(registros))
                for i, registro in enumerate(registros):
                    self.tabla.setItem(i, 0, QTableWidgetItem(registro[1]))
                    self.tabla.setItem(i, 1, QTableWidgetItem(registro[2]))
                    self.tabla.setItem(i, 2, QTableWidgetItem(registro[3]))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar datos: {e}")
        else:
            QMessageBox.critical(self, "Error", "Error al conectarse a la base de datos")           

    def insertar_usuario(self):
        connection = self.get_connection()

        if connection is not None:
            #QMessageBox.information(self, "Conexión exitosa", "Conexión a la base de datos exitosa")    
            try:
                cursor = connection.cursor()
                # Cambiar '?' por '%s' para MySQL
                query = "INSERT INTO Usuario (nombre_usuario, contrasena, rol) VALUES (%s, %s, %s);"
                registro_t = (
                    self.txt_nombre_usuario.text(),
                    self.encriptar_contrasena(self.txt_contrasena.text()),
                    self.cbo_rol.currentText()
                )
                cursor.execute(query, registro_t)
                connection.commit()
                self.cargar_datos()
                self.txt_nombre_usuario.clear()
                self.txt_contrasena.clear()
                self.cbo_rol.setCurrentIndex(0)
                #QMessageBox.information(self, "Éxito", "Usuario insertado con éxito")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al insertar usuario: {e}")
            finally:
                connection.close()  # Siempre cerrar la conexión
        else:
            QMessageBox.critical(self, "Error", "Error al conectarse a la base de datos")

    def encriptar_contrasena(self, contrasena):
        # Convertir la contraseña en bytes
        contrasena_byte = contrasena.encode()
        # Encriptar la contraseña
        contrasena_hashed = bcrypt.hashpw(contrasena_byte, bcrypt.gensalt())
        return contrasena_hashed.decode()
    
    def actualizar_usuario(self):
        connection = self.get_connection()

        if connection is not None:
            #QMessageBox.information(self, "Conexión exitosa", "Conexión a la base de datos exitosa")    
            try:
                cursor = connection.cursor()
                # Cambiar '?' por '%s' para MySQL
                query = "UPDATE Usuario SET contrasena = %s, rol = %s WHERE nombre_usuario = %s;"
                registro_t = (
                    self.encriptar_contrasena(self.txt_contrasena.text()),
                    self.cbo_rol.currentText(),
                    self.txt_nombre_usuario.text()
                )
                cursor.execute(query, registro_t)
                connection.commit()
                self.cargar_datos()
                self.txt_nombre_usuario.clear()
                self.txt_contrasena.clear()
                self.cbo_rol.setCurrentIndex(0)
                #QMessageBox.information(self, "Éxito", "Usuario actualizado con éxito")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al actualizar usuario: {e}")
            finally:
                connection.close()  # Siempre cerrar la conexión
        else:
            QMessageBox.critical(self, "Error", "Error al conectarse a la base de datos")

    def eliminar_usuario(self):
        connection = self.get_connection()

        if connection is not None:
            #QMessageBox.information(self, "Conexión exitosa", "Conexión a la base de datos exitosa")    
            try:
                cursor = connection.cursor()
                # Cambiar '?' por '%s' para MySQL
                query = "DELETE FROM Usuario WHERE nombre_usuario = %s;"
                cursor.execute(query, (self.tabla.item(self.tabla.currentRow(), 0).text(),))
                connection.commit()
                self.cargar_datos()
                self.txt_nombre_usuario.clear()
                self.txt_contrasena.clear()
                self.cbo_rol.setCurrentIndex(0)
                #QMessageBox.information(self, "Éxito", "Usuario eliminado con éxito")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar usuario: {e}")
            finally:
                connection.close()


if __name__ == "__main__":
    app = QApplication()
    ventana = VentanaGestionUsuarios()
    ventana.show()
    sys.exit(app.exec_())
