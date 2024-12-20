import sys, os
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,
    QTableWidget, QAbstractItemView, QFormLayout, QLabel, QLineEdit,
    QComboBox,  )
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt

from ventana_principal import VentanaPrincipal
from insertar_usuario import VentanaRegistrarUsuarios


class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icono.png"))
        self.personalizar_ventana()
        self.personalizar_componentes()
        self.show()
        

    def personalizar_ventana(self):
        self.setWindowTitle("Iniciar sesión")
        self.setWindowIcon(QIcon("icono.png"))
        self.setFixedSize(200, 200)

    def personalizar_componentes(self):
        

        layout_formulario = QFormLayout()
        self.txt_nombre_usuario = QLineEdit()
        self.txt_nombre_usuario.setPlaceholderText("Usuario")
        self.txt_nombre_usuario.setAlignment(Qt.AlignCenter)
        self.txt_nombre_usuario.setFocus()
        self.txt_contrasena = QLineEdit()
        self.txt_contrasena.setPlaceholderText("Contraseña")
        self.txt_contrasena.setAlignment(Qt.AlignCenter)
        self.txt_contrasena.setEchoMode(QLineEdit.Password)

        
        

        layout_formulario.addWidget(self.txt_nombre_usuario)

        layout_formulario.addWidget(self.txt_contrasena)

        
        layout_principal = QVBoxLayout()

        layout_principal.addLayout(layout_formulario)

        self.btn_registrar = QPushButton("Registrar")
        self.btn_registrar.clicked.connect(self.abrir_ventana_registrar)
        self.btn_registrar.setFocusPolicy(Qt.StrongFocus)
        layout_principal.addWidget(self.btn_registrar)

        self.btn_login = QPushButton("Iniciar sesión")
        self.btn_login.clicked.connect(self.validar_credenciales)
        self.btn_login.setFocusPolicy(Qt.StrongFocus)
        layout_principal.addWidget(self.btn_login)

        
        self.setLayout(layout_principal)
        self.set_tab_order()

    def set_tab_order(self):
        self.setTabOrder(self.txt_nombre_usuario, self.txt_contrasena)
        self.setTabOrder(self.txt_contrasena, self.btn_login)
        self.setTabOrder(self.btn_registrar, self.btn_login)
        

    def get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Passw0rd!",
            database="ferreteria"
        )

    def validar_credenciales(self):
        connection = self.get_connection()
        if connection is not None:
            try:                
                nombre_usuario = self.txt_nombre_usuario.text()
                contrasena = self.txt_contrasena.text()
                cursor = connection.cursor()
                query = "SELECT contrasena, rol FROM Usuario WHERE nombre_usuario = %s"
                cursor.execute(query, (nombre_usuario,))  # Se pasa el nombre de usuario como parámetro y siendo uno solo no es necesario una tupla pero si fuera más de uno sí sería necesario (nombre_usuario,)
                resultado_t = cursor.fetchone()

                if resultado_t:
                    contrasena_hash, rol = resultado_t
                    if bcrypt.checkpw(contrasena.encode('utf-8'), contrasena_hash.encode('utf-8')):
                        self.abrir_ventana_principal(rol)
                    else:
                        QMessageBox.warning(self, "Error", "Contraseña incorrecta.")
                else:
                    QMessageBox.warning(self, "Error", "Usuario no valido.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al intentar iniciar sesión: {str(e)}")
        else:
            QMessageBox.critical(self, "Error", "No se pudo establecer la conexión.")
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Cuando se presiona Enter, se dispara la acción del botón
            self.validar_credenciales()

    def abrir_ventana_principal(self, rol):
        self.txt_nombre_usuario.clear()
        self.txt_contrasena.clear()
        self.hide()
        self.ventana_principal = VentanaPrincipal(rol,self)
        self.ventana_principal.show()
        #QMessageBox.information(self, "Éxito", "Iniciaste sesión correctamente." + rol)
        

    def abrir_ventana_registrar(self):
        self.hide()
        self.ventana_registrar = VentanaRegistrarUsuarios()
        self.ventana_registrar.show()
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec())