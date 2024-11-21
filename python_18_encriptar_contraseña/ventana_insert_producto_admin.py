import sys, os, sqlite3
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLabel, QLineEdit, 
    QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt

import ventana_menu as vm

# Funciones de la base de datos
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
        self.setWindowTitle("Admin - Almacén")
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
        self.lblTitulo = QLabel("Insertar Producto")
        self.lblTitulo.setFont(QFont("Courier New", 22, QFont.Bold))
        self.lblTitulo.setStyleSheet("background-color: black; color: white; font-weight: bold")
        self.lblTitulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lblTitulo)

        # Sub-layout para los campos de entrada
        form_layout = QVBoxLayout()
        
        # Campos de texto
        self.lblNombreProducto = QLabel("Nombre del Producto: ")
        self.lblNombreProducto.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblNombreProducto.setStyleSheet("color: black; font-weight: bold")
        self.txtNombreProducto = QLineEdit()
        self.txtNombreProducto.setFont(QFont("Courier New", 13, QFont.Bold))
        self.txtNombreProducto.setStyleSheet("border: 2px solid black; padding: 5px; color: black;")
        
        self.lblPrecio = QLabel("Precio: ")
        self.lblPrecio.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblPrecio.setStyleSheet("color: black; font-weight: bold")
        self.txtPrecio = QLineEdit()
        self.txtPrecio.setFont(QFont("Courier New", 13, QFont.Bold))
        self.txtPrecio.setStyleSheet("border: 2px solid black; padding: 5px; color: black;")
        
        self.lblStock = QLabel("Stock: ")
        self.lblStock.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblStock.setStyleSheet("color: black; font-weight: bold")
        self.txtStock = QLineEdit()
        self.txtStock.setFont(QFont("Courier New", 13, QFont.Bold))
        self.txtStock.setStyleSheet("border: 2px solid black; padding: 5px; color: black;")
        
        # Agregar widgets al formulario
        form_layout.addWidget(self.lblNombreProducto)
        form_layout.addWidget(self.txtNombreProducto)
        form_layout.addWidget(self.lblPrecio)
        form_layout.addWidget(self.txtPrecio)
        form_layout.addWidget(self.lblStock)
        form_layout.addWidget(self.txtStock)

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
                background-color: lightblue;
            }
        """)
        self.btnInsert.clicked.connect(self.insertar_producto)

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
                background-color: lightblue;
            }
        """)
        self.btnReiniciar.clicked.connect(self.reiniciar_campos)

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

        # Botón Atrás
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
                background-color: lightblue;
            }
        """)
        self.btnAtras.clicked.connect(self.atras)

        # Añadir botones al layout
        button_layout.addWidget(self.btnInsert)
        button_layout.addWidget(self.btnReiniciar)
        button_layout.addWidget(self.btnAtras)
        button_layout.addWidget(self.btnSalir)

        layout.addLayout(button_layout)

    def insertar_producto(self):
        # Código de inserción de producto
        pass

    def reiniciar_campos(self):
        self.txtNombreProducto.clear()
        self.txtPrecio.clear()
        self.txtStock.clear()

    def salir(self):
        self.close()
        app.quit()

    def atras(self):
        self.close()  # Cierra la ventana actual
        self.ventana = vm.Ventana()
        self.ventana.show()

# Main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
