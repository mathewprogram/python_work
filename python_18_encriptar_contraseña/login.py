import sys, os, sqlite3, bcrypt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt
import ventana_insert_venta as viv
import ventana_insert_producto as vip
import ventana_menu as vm

def get_connection():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_18_encriptar_contraseña/ferreteria.sqlite3"
    connection = None
    try:
        connection = sqlite3.connect(nra)
    except sqlite3.Error as error:
        connection = None
    return connection

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.personalizarVentana()
        self.personalizarComponentes()

    def verificar_contrasena(self, contrasena_ingresada, contrasena_almacenada):
        # Comparar la contraseña ingresada con el hash almacenado
        return bcrypt.checkpw(contrasena_ingresada.encode(), contrasena_almacenada.encode())

    def personalizarVentana(self):
        self.setWindowTitle("Log In")
        self.setStyleSheet("background-color: lightgray;")
        self.setFixedSize(480, 330)

        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta)
        self.setWindowIcon(QIcon(ruta_absoluta))

        self.pnlPrincipal = QWidget()
        self.setCentralWidget(self.pnlPrincipal)
    
    def personalizarComponentes(self):
        self.lblLogin = QLabel("Usuario", self.pnlPrincipal)
        self.lblLogin.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblLogin.setStyleSheet("background-color: black; color:white;")
        self.lblLogin.setAlignment(Qt.AlignCenter)
        self.lblLogin.setGeometry(180, 80, 120, 20)

        self.txtLogin = QLineEdit(self.pnlPrincipal)
        self.txtLogin.setGeometry(180, 110, 120, 20)
        self.txtLogin.setFont(QFont("Courier New", 18))
        self.txtLogin.setAlignment(Qt.AlignCenter)
        self.txtLogin.setStyleSheet("color: black;")
        self.txtLogin.setPlaceholderText("Usuario")

        self.lblPassword = QLabel("Contraseña", self.pnlPrincipal)
        self.lblPassword.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblPassword.setStyleSheet("background-color: black; color:white;")
        self.lblPassword.setAlignment(Qt.AlignCenter)
        self.lblPassword.setGeometry(180, 140, 120, 20)

        self.txtPassword = QLineEdit(self.pnlPrincipal)
        self.txtPassword.setGeometry(180, 170, 120, 20)
        self.txtPassword.setFont(QFont("Courier New", 18))
        self.txtPassword.setAlignment(Qt.AlignCenter)
        self.txtPassword.setStyleSheet("color: black;")  
        self.txtPassword.setMaxLength(9)
        self.txtPassword.setEchoMode(QLineEdit.Password) 
        self.txtPassword.setPlaceholderText("Contraseña")


        self.btoAceptar = QPushButton("Aceptar", self.pnlPrincipal)
        self.btoAceptar.setGeometry(180, 220, 120, 20)
        self.btoAceptar.setFont(QFont("Courier New", 18, QFont.Bold))
        self.btoAceptar.setStyleSheet("color: black;")
        self.btoAceptar.clicked.connect(self.btnAceptarClick)

    def btnAceptarClick(self):
        login = self.txtLogin.text()
        password = self.txtPassword.text()
        
        connection = get_connection()
        if connection is not None:
            cursor = connection.cursor()
            sql = "SELECT nombre_usuario, contrasena, rol FROM Usuario WHERE nombre_usuario = ?"
            cursor.execute(sql, (login,))
            result = cursor.fetchone()

            if result:
                nombre_usuario, contrasena_db, rol = result
                # Verificar la contraseña usando bcrypt
                if self.verificar_contrasena(password, contrasena_db):
                    # Verificar el rol y redirigir según el acceso
                    if rol == 'Admin':
                        QMessageBox.information(self, 'Login correcto', f'Welcome, admin {nombre_usuario}!')
                        self.close()
                        self.abrirVentana('Admin')
                    elif rol == 'Cajero':
                        QMessageBox.information(self, f'Login correcto', f'Welcome, cajero {nombre_usuario}!')
                        self.close()
                        self.abrirVentana('Cajero')
                    elif rol == 'Almacen':
                        QMessageBox.information(self, 'Login correcto', f'Welcome, almacen {nombre_usuario}!')
                        self.close()
                        self.abrirVentana('Almacen')
                else:
                    QMessageBox.warning(self, 'Incorrect login', 'Incorrect password')
            else:
                QMessageBox.warning(self, 'Incorrect login', 'User not found')

            connection.close()  # Cerrar la conexión a la base de datos

        else:
            QMessageBox.critical(self, "Error", "Connection failed.")


    def abrirVentana(self, rol):
        if rol == 'Admin':
            self.ventana_menu = vm.Ventana()
            self.ventana_menu.show()
            self.close()
        elif rol == 'Cajero':
            self.ventana_venta = viv.Ventana()
            self.ventana_venta.show()
        elif rol == 'Almacen':
            self.ventana_almacen = vip.Ventana()
            self.ventana_almacen.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
