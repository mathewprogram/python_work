import sys, os, sqlite3
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLabel, QLineEdit, 
    QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QComboBox
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QCoreApplication

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
        self.setWindowTitle("Cajero")
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
        self.lblTitulo = QLabel("Insertar Venta")
        self.lblTitulo.setFont(QFont("Courier New", 22, QFont.Bold))
        self.lblTitulo.setStyleSheet("background-color: black; color: white; font-weight: bold")
        self.lblTitulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lblTitulo)

        # Sub-layout para los campos de entrada
        form_layout = QVBoxLayout()
        
        # Campos de texto
        self.lblProducto = QLabel("Producto: ")
        self.lblProducto.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblProducto.setStyleSheet("color: black; font-weight: bold")
        self.txtProducto = QLineEdit()
        self.txtProducto.setFont(QFont("Courier New", 13, QFont.Bold))
        self.txtProducto.setStyleSheet("border: 2px solid black; padding: 5px; color: black;")
        
        self.lblFecha = QLabel("Fecha: ")
        self.lblFecha.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblFecha.setStyleSheet("color: black; font-weight: bold")
        self.txtFecha = QLineEdit()
        self.txtFecha.setFont(QFont("Courier New", 13, QFont.Bold))
        self.txtFecha.setStyleSheet("border: 2px solid black; padding: 5px; color: black;")
        
        self.lblTotal = QLabel("Total: ")
        self.lblTotal.setFont(QFont("Courier New", 18, QFont.Bold))
        self.lblTotal.setStyleSheet("color: black; font-weight: bold")
        self.txtTotal = QLineEdit()
        self.txtTotal.setFont(QFont("Courier New", 13, QFont.Bold))
        self.txtTotal.setStyleSheet("border: 2px solid black; padding: 5px; color: black;")
        
        # Agregar widgets al formulario
        form_layout.addWidget(self.lblProducto)
        form_layout.addWidget(self.txtProducto)
        form_layout.addWidget(self.lblFecha)
        form_layout.addWidget(self.txtFecha)
        form_layout.addWidget(self.lblTotal)
        form_layout.addWidget(self.txtTotal)

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
        self.btnInsert.clicked.connect(self.insertar_venta)

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
                background-color: red;  /* Cambiar el color de fondo a rojo */
                color: white;  /* Cambiar el color del texto a blanco */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: darkred;  /* Cambiar el color cuando se hace hover */
            }
        """)
        self.btnSalir.clicked.connect(self.salir)


        button_layout.addWidget(self.btnInsert)
        button_layout.addWidget(self.btnReiniciar)
        button_layout.addWidget(self.btnSalir)

        layout.addLayout(button_layout)

    def insertar_venta(self):
        producto = self.txtProducto.text().strip()
        fecha_venta = self.txtFecha.text().strip()
        total = self.txtTotal.text().strip()

        if not producto or not fecha_venta or not total:
            QMessageBox.warning(self, "Advertencia", "Complete todos los campos antes de insertar.")
            return
        connection = get_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                sql = """INSERT INTO Venta (producto, fecha_venta, total) VALUES (?, ?, ?);"""
                cursor.execute(sql, (producto, fecha_venta, total))
                connection.commit()
                QMessageBox.information(self, "Éxito", "Venta insertada correctamente.")
            except sqlite3.IntegrityError:
                QMessageBox.critical(self, "Error", "Venta ya existe.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Error al insertar: {e}")
            finally:
                connection.close()

    def reiniciar_campos(self):
        self.txtProducto.clear()
        self.txtFecha.clear()
        self.txtTotal.clear()

    def salir(self):
        self.close()
        QCoreApplication.instance().quit()


# Main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_insert_venta = Ventana()
    ventana_insert_venta.show()
    sys.exit(app.exec())  # Ejecutar la aplicación Qt
