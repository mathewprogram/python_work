import sys, os, sqlite3, bcrypt
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLabel, QLineEdit, 
    QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QComboBox
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt

import ventana_menu as vm

# Funciones de la base de datos y encriptación
def encriptar_contrasena(contrasena):
    contrasena_byte = contrasena.encode()
    contrasena_hashed = bcrypt.hashpw(contrasena_byte, bcrypt.gensalt())
    return contrasena_hashed.decode()

def get_connection():
    ruta = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_18_encriptar_contraseña/ferreteria.sqlite3"
    connection = None
    try:
        connection = sqlite3.connect(ruta)
    except sqlite3.Error as error:
        QMessageBox.critical(None, "Error", f"Error al conectar con la base de datos: {error}")
    return connection

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.personalizarVentana()
        self.personalizarComponentes()

    def personalizarVentana(self):
        self.setWindowTitle("Administrar")
        self.setFixedSize(480, 330)
        self.setStyleSheet("background-color: lightgray;")
        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))
        self.pnlPrincipal = QWidget()
        self.setCentralWidget(self.pnlPrincipal)

    def personalizarComponentes(self):
        # Layout principal
        layout = QVBoxLayout(self.pnlPrincipal)

        # Título
        self.lblTitulo = QLabel("Insertar Usuario")
        self.lblTitulo.setFont(QFont("Courier New", 22, QFont.Bold))
        self.lblTitulo.setStyleSheet("background-color: black; color: white; font-weight: bold")
        self.lblTitulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lblTitulo)

        # Sub-layout para los campos de entrada
        form_layout = QVBoxLayout()
        
        # Campos de texto
        self.lblUsuario = QLabel("Usuario: ")
        self.lblUsuario.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblUsuario.setStyleSheet("color: black; font-weight: bold")
        self.txtUsuario = QLineEdit()
        self.txtUsuario.setFont(QFont("Courier New", 13, QFont.Bold))
        self.txtUsuario.setStyleSheet("border: 2px solid black; padding: 5px; color: black;")
        
        self.lblContrasena = QLabel("Contraseña: ")
        self.lblContrasena.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblContrasena.setStyleSheet("color: black; font-weight: bold")
        self.txtContrasena = QLineEdit()
        self.txtContrasena.setFont(QFont("Courier New", 13, QFont.Bold))
        self.txtContrasena.setStyleSheet("border: 2px solid black; padding: 5px; color: black;")
        self.txtContrasena.setEchoMode(QLineEdit.Password)

        # Botón para alternar visibilidad de la contraseña
        self.btnTogglePassword = QPushButton("🙈", self.pnlPrincipal)
        self.btnTogglePassword.setCheckable(True)
        self.btnTogglePassword.clicked.connect(self.toggle_password_visibility)

        # Layout horizontal para la contraseña y el botón de visibilidad
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.txtContrasena)  # Campo de contraseña
        password_layout.addWidget(self.btnTogglePassword)  # Botón de visibilidad

        # Agregar widgets al formulario
        form_layout.addWidget(self.lblUsuario)
        form_layout.addWidget(self.txtUsuario)
        form_layout.addWidget(self.lblContrasena)
        form_layout.addLayout(password_layout)  # Usar el nuevo layout para la contraseña

        # ComboBox para tipo de usuario
        self.cboTipoUsuario = QComboBox()
        self.cboTipoUsuario.setFont(QFont("Courier New", 18, QFont.Bold))
        self.cboTipoUsuario.setStyleSheet("color: black; font-weight: bold")
        self.cboTipoUsuario.addItems(["Seleccione", "Admin", "Cajero", "Almacen"])
        form_layout.addWidget(self.cboTipoUsuario)

        layout.addLayout(form_layout)

        # Sub-layout para los botones
        button_layout = QHBoxLayout()
        
        self.btnInsert = QPushButton("Insertar")
        self.btnInsert.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btnInsert.setStyleSheet("""
            QPushButton {
                border: 2px solid black;
                background-color: white;
                color: black;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: lightblue;  /* Cambiar el color cuando se hace hover */
            }
        """)
        self.btnInsert.clicked.connect(self.insertar_usuario)

        self.btnReiniciar = QPushButton("Reiniciar")
        self.btnReiniciar.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btnReiniciar.setStyleSheet("""
            QPushButton {
                border: 2px solid black;
                background-color: white;
                color: black;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: lightblue;  /* Cambiar el color cuando se hace hover */
            }
        """)
        self.btnReiniciar.clicked.connect(self.reiniciar)

        self.btnAtras = QPushButton("Atrás")
        self.btnAtras.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btnAtras.setStyleSheet("""
            QPushButton {
                border: 2px solid black;
                background-color: white;
                color: black;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: lightblue;  /* Cambiar el color cuando se hace hover */
            }
        """)
        self.btnAtras.clicked.connect(self.atras)

        self.btnSalir = QPushButton("Salir")
        self.btnSalir.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btnSalir.setStyleSheet("""
            QPushButton {
                border: 2px solid black;
                background-color: red;
                color: white;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)
        self.btnSalir.clicked.connect(self.salir)

        # Agregar botones al sub-layout
        button_layout.addWidget(self.btnInsert)
        button_layout.addWidget(self.btnReiniciar)
        button_layout.addWidget(self.btnAtras)
        button_layout.addWidget(self.btnSalir)

        layout.addLayout(button_layout)

    # Función para alternar la visibilidad de la contraseña
    def toggle_password_visibility(self):
        if self.btnTogglePassword.isChecked():
            self.txtContrasena.setEchoMode(QLineEdit.Normal)
            self.btnTogglePassword.setText("👁")  # Cambio de icono cuando la contraseña es visible
        else:
            self.txtContrasena.setEchoMode(QLineEdit.Password)
            self.btnTogglePassword.setText("🙈")  # Cambio de icono cuando la contraseña está oculta

    def insertar_usuario(self):
        nombre_usuario = self.txtUsuario.text().strip()
        contrasena = self.txtContrasena.text().strip()
        rol = self.cboTipoUsuario.currentText()

        if not nombre_usuario or not contrasena or rol == "Seleccione":
            QMessageBox.warning(self, "Advertencia", "Complete todos los campos antes de insertar.")
            return

        contrasena_encriptada = encriptar_contrasena(contrasena)
        connection = get_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                sql = """INSERT INTO Usuario (nombre_usuario, contrasena, rol) VALUES (?, ?, ?);"""
                cursor.execute(sql, (nombre_usuario, contrasena_encriptada, rol))
                connection.commit()
                QMessageBox.information(self, "Éxito", "Usuario insertado correctamente.")
            except sqlite3.IntegrityError:
                QMessageBox.critical(self, "Error", "El nombre de usuario ya existe.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Error al insertar: {e}")
            finally:
                connection.close()

    def reiniciar(self):
        self.txtUsuario.clear()
        self.txtContrasena.clear()
        self.cboTipoUsuario.setCurrentIndex(0)

    def salir(self):
        self.close()

    def atras(self):
        self.close()  # Cierra la ventana actual
        self.ventana = vm.Ventana()
        self.ventana.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
