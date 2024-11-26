import sys, os
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QWidget,
)
from PySide6.QtGui import QIcon

from ventana_gestion_producto import VentanaGestionProducto
from ventana_gestion_usuarios import VentanaGestionUsuarios
from gestion_ventas import VentanaGestionVentas_enClase
from ventana_gestion_ventas import VentanaGestionCajero
from ventana_gestion_detallesVenta import VentanaGestionAlmacen


class VentanaPrincipal(QMainWindow):
    def __init__(self, rol, objeto_ventana_login):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        self.setWindowIcon(QIcon("icono.png"))
        self.setFixedSize(400, 200)
        self.objeto_ventana_login = objeto_ventana_login
        self.rol = rol

        layout_principal = QVBoxLayout()
        panel_principal = QWidget()
        panel_principal.setLayout(layout_principal)
        self.setCentralWidget(panel_principal)

        # Dependiendo del rol, mostrar los botones adecuados
        if rol == "Administrador":
            self.abrir_ventana_administrador(layout_principal)
        elif rol == "Cajero":
            self.abrir_ventana_cajero(layout_principal)
        elif rol == "Almacén":
            self.abrir_ventana_almacen(layout_principal)

    def abrir_ventana_administrador(self, layout_principal):
        # Botones para el rol de Administrador
        btn_gestionar_usuarios = QPushButton("Gestionar usuarios")
        btn_gestionar_usuarios.clicked.connect(self.abrir_ventana_gestion_usuarios)
        btn_gestionar_productos = QPushButton("Gestionar productos")
        btn_gestionar_productos.clicked.connect(self.abrir_ventana_gestion_producto)
        btn_gestionar_ventas_y_detalles = QPushButton("Gestionar Ventas y Detalles")
        btn_gestionar_ventas_y_detalles.clicked.connect(self.abrir_ventana_gestion_ventas_y_detalles)
        btn_gestionar_ventas = QPushButton("Gestionar Ventas")
        btn_gestionar_ventas.clicked.connect(self.abrir_ventana_gestion_ventas)
        btn_gestionar_detallesVenta = QPushButton("Gestionar Detalles Ventas")
        btn_gestionar_detallesVenta.clicked.connect(self.abrir_ventana_gestion_detallesVenta)
        btn_cerrar_sesion = QPushButton("Cerrar sesión")
        btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)

        # Añadir botones al layout
        layout_principal.addWidget(btn_gestionar_usuarios)
        layout_principal.addWidget(btn_gestionar_productos)
        layout_principal.addWidget(btn_gestionar_ventas_y_detalles)
        layout_principal.addWidget(btn_gestionar_ventas)
        layout_principal.addWidget(btn_gestionar_detallesVenta)

        layout_principal.addWidget(btn_cerrar_sesion)

    def abrir_ventana_cajero(self, layout_principal):
        # Botones para el rol de Cajero
        btn_gestionar_ventas_y_detalles = QPushButton("Gestionar Ventas y Detalles")
        btn_gestionar_ventas_y_detalles.clicked.connect(self.abrir_ventana_gestion_ventas_y_detalles)
        btn_gestionar_productos = QPushButton("Gestionar productos")
        btn_gestionar_productos.clicked.connect(self.abrir_ventana_gestion_producto)
        btn_gestionar_pedidos = QPushButton("Gestionar Ventas")
        btn_gestionar_pedidos.clicked.connect(self.abrir_ventana_gestion_ventas)
        btn_cerrar_sesion = QPushButton("Cerrar sesión")
        btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)

        # Añadir botones al layout
        layout_principal.addWidget(btn_gestionar_ventas_y_detalles)
        layout_principal.addWidget(btn_gestionar_productos)
        layout_principal.addWidget(btn_gestionar_pedidos)
        layout_principal.addWidget(btn_cerrar_sesion)

    def abrir_ventana_almacen(self, layout_principal):
        # Botones para el rol de Almacén
        btn_gestionar_stock = QPushButton("Gestionar Stock")
        btn_gestionar_stock.clicked.connect(self.abrir_ventana_gestion_stock)
        btn_cerrar_sesion = QPushButton("Cerrar sesión")
        btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)

        # Añadir botones al layout
        layout_principal.addWidget(btn_gestionar_stock)
        layout_principal.addWidget(btn_cerrar_sesion)

    def cerrar_sesion(self):
        # Muestra la ventana de login y cierra la ventana principal
        self.close()
        self.objeto_ventana_login.show()
        

    def abrir_ventana_gestion_usuarios(self):
        self.ventana_gestion_usuarios = VentanaGestionUsuarios(self)
        self.ventana_gestion_usuarios.show()
        self.hide()


    def abrir_ventana_gestion_producto(self):
        self.ventana_gestion_producto = VentanaGestionProducto(self)
        self.ventana_gestion_producto.show()
        self.hide()

    def abrir_ventana_gestion_ventas(self):
        self.ventana_gestion_producto = VentanaGestionCajero(self)
        self.ventana_gestion_producto.show()
        self.hide()

    def abrir_ventana_gestion_stock(self):
        self.ventana_gestion_producto = VentanaGestionAlmacen(self)
        self.ventana_gestion_producto.show()
        self.hide()
        
    def abrir_ventana_gestion_ventas_y_detalles(self):
        self.gestion_ventas = VentanaGestionVentas_enClase(self)
        self.gestion_ventas.show()
        self.hide()


