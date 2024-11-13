import sys, os
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QVBoxLayout, QPushButton, QVBoxLayout, QMessageBox
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
import sqlite3

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.personalizarVentana()
        self.personalizarComponentes()

    def personalizarVentana(self):
        self.setFixedSize(800, 600) # Tamaño de la ventana ancho y altura
        self.setWindowTitle("Ventana de Selección de Fútbol") # Título para la ventana
        self.setStyleSheet("background-color: lightgray;") # Color de fondo para la ventana

        # Cambiar el icono de la ventana con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizarComponentes(self):
        self.tblMostrar = QTableWidget(self)
        self.tblMostrar.setColumnCount(4)
        self.tblMostrar.setRowCount(0)
        self.tblMostrar.setHorizontalHeaderLabels(["ID", "Nombre", "Apellidos", "Edad"])
        self.tblMostrar.horizontalHeader().setStyleSheet("color: black; background-color: white;")
        self.tblMostrar.verticalHeader().setStyleSheet("color: black; background-color: white;")
        self.tblMostrar.horizontalHeader().setFont(QFont("Courier New", 16, QFont.Bold)) # Fuente de letra y tamaño de letra de la cabecera
        self.tblMostrar.setFont(QFont("Courier New", 16)) # Fuente de letra y tamaño de letra del cuerpo
        self.tblMostrar.setStyleSheet("color: black; background-color: lightgray;") # Color de fondo del cuerpo

        header = self.tblMostrar.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Ajustar automáticamente el ancho de las columnas
        header.setStretchLastSection(True)  # Estirar la última sección (última columna) para llenar el espacio

        # Botones
        self.btnMostrarSeleccionFutbol = QPushButton("Mostrar Selección de Fútbol", self)
        self.btnMostrarSeleccionFutbol.clicked.connect(lambda: self.cargarDatosTabla("SeleccionFutbol"))

        self.btnMostrarFutbolista = QPushButton("Mostrar Futbolistas", self)
        self.btnMostrarFutbolista.clicked.connect(lambda: self.cargarDatosTabla("Futbolista"))

        self.btnMostrarMasajista = QPushButton("Mostrar Masajistas", self)
        self.btnMostrarMasajista.clicked.connect(lambda: self.cargarDatosTabla("Masajista"))

        self.btnMostrarEntrenador = QPushButton("Mostrar Entrenadores", self)
        self.btnMostrarEntrenador.clicked.connect(lambda: self.cargarDatosTabla("Entrenador"))

        # Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.tblMostrar)
        layout.addWidget(self.btnMostrarSeleccionFutbol)
        layout.addWidget(self.btnMostrarFutbolista)
        layout.addWidget(self.btnMostrarMasajista)
        layout.addWidget(self.btnMostrarEntrenador)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def cargarDatosTabla(self, tabla):
        self.limpiarTabla()
        conexion = self.obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute(f"SELECT * FROM {tabla}")
            rows = cursor.fetchall()
            for row in rows:
                rowPosition = self.tblMostrar.rowCount()
                self.tblMostrar.insertRow(rowPosition)
                for column, data in enumerate(row):
                    self.tblMostrar.setItem(rowPosition, column, QTableWidgetItem(str(data)))
            conexion.close()

    def limpiarTabla(self):
        self.tblMostrar.setRowCount(0)

    def obtener_conexion(self):
        nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_objetos/db_footbol_sqlite3"
        conexion = None
        try:
            conexion = sqlite3.connect(nra)
        except sqlite3.Error as error:
            print("Error al conectar con la base de datos:", error)
        return conexion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())