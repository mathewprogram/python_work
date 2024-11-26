import sys, os
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,
    QTableWidget, QAbstractItemView, QFormLayout, QLabel, QLineEdit,
    QComboBox)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class VentanaGestionUsuarios(QWidget):
    def __init__(self, objeto_ventana_principal):
        super().__init__()
        
        self.personalizar_ventana()
        self.personalizar_componentes()
        self.cargar_datos()
        self.objeto_ventana = objeto_ventana_principal


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
        pass