import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QFont, Qt
import ventana_insert_usuario as viu
import ventana_insert_venta_admin as viv
import ventana_insert_producto_admin as vip

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú Principal")
        self.setFixedSize(400, 250)
        self.setStyleSheet("background-color: lightgray;")
        self.personalizarVentana()

    def personalizarVentana(self):
        # Crear el contenedor principal
        self.pnlPrincipal = QWidget()
        self.setCentralWidget(self.pnlPrincipal)

        # Configuración del layout
        layout = QVBoxLayout(self.pnlPrincipal)
        layout.setSpacing(11)  # Establecer el espacio en pixeles

        # Título para la ventana
        self.titulo = QLabel("Menú")  # Crear el título
        self.titulo.setFont(QFont("Courier New", 30, QFont.Bold))
        self.titulo.setStyleSheet("background-color: black; color: white; font-weight: bold") # Establecer la fuente
        self.titulo.setAlignment(Qt.AlignCenter)  # Centrar el texto
        layout.addWidget(self.titulo)

        # Botón para ventana de usuarios
        self.btnUsuarios = QPushButton("Gestionar Usuarios")
        self.btnUsuarios.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btnUsuarios.setStyleSheet("""
            QPushButton {
                color: black;
                border: 2px solid black;
                background-color: white;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: lightblue;
            }
        """)
        self.btnUsuarios.clicked.connect(self.abrirVentanaUsuarios)
        layout.addWidget(self.btnUsuarios)

        # Botón para ventana de ventas
        self.btnVentas = QPushButton("Gestionar Ventas")
        self.btnVentas.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btnVentas.setStyleSheet("""
            QPushButton {
                color: black;
                border: 2px solid black;
                background-color: white;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: lightblue;
            }
        """)
        self.btnVentas.clicked.connect(self.abrirVentanaVentas)
        layout.addWidget(self.btnVentas)

        # Botón para ventana de productos
        self.btnProductos = QPushButton("Gestionar Productos")
        self.btnProductos.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btnProductos.setStyleSheet("""
            QPushButton {
                color: black;
                border: 2px solid black;
                background-color: white;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: lightblue;
            }
        """)
        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        layout.addWidget(self.btnProductos)

    # Métodos para abrir las otras ventanas
    def abrirVentanaUsuarios(self):
        self.ventana_usuarios = viu.Ventana()
        self.ventana_usuarios.show()
        self.close()

    def abrirVentanaVentas(self):
        self.ventana_ventas = viv.Ventana()
        self.ventana_ventas.show()
        self.close()

    def abrirVentanaProductos(self):
        self.ventana_productos = vip.Ventana()
        self.ventana_productos.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_menu = Ventana()
    ventana_menu.show()
    sys.exit(app.exec())
