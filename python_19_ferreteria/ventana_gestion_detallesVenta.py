import sys, os
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,
    QTableWidget, QAbstractItemView, QFormLayout, QLabel, QLineEdit,
    QComboBox, )
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt



class VentanaGestionAlmacen(QWidget):
    def __init__(self, objeto_ventana_principal):
        super().__init__()
        
        self.personalizar_ventana()
        self.personalizar_componentes()
        self.cargar_datos()
        self.objeto_ventana = objeto_ventana_principal

    def personalizar_ventana(self):
        self.setWindowTitle("Gestión Detalle Ventas")
        self.setFixedSize(800, 600)
        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizar_componentes(self):
        layout = QVBoxLayout()

        # Tabla de Detalle Ventas
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID Venta", "ID Producto", "Cantidad", "Subtotal"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.tabla)

        # Campos para CRUD
        self.txt_id_venta = QLineEdit()
        self.txt_id_venta.setPlaceholderText("ID Venta")
        self.txt_id_producto = QLineEdit()
        self.txt_id_producto.setPlaceholderText("ID Producto")
        self.txt_cantidad = QLineEdit()
        self.txt_cantidad.setPlaceholderText("Cantidad")
        self.txt_subtotal = QLineEdit()
        self.txt_subtotal.setPlaceholderText("Subtotal")

        self.btn_insertar = QPushButton("Insertar detalle")
        self.btn_insertar.clicked.connect(self.insertar_detalle)
        self.btn_actualizar = QPushButton("Actualizar detalle")
        self.btn_actualizar.clicked.connect(self.actualizar_detalle)
        self.btn_eliminar = QPushButton("Eliminar detalle")
        self.btn_eliminar.clicked.connect(self.eliminar_detalle)
        self.btn_menu = QPushButton("Menu")
        self.btn_menu.clicked.connect(self.menu)
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)

        # Layouts para los campos y botones
        insert_layout = QHBoxLayout()
        insert_layout.addWidget(self.txt_id_venta)
        insert_layout.addWidget(self.txt_id_producto)
        insert_layout.addWidget(self.txt_cantidad)
        insert_layout.addWidget(self.txt_subtotal)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.btn_insertar)
        botones_layout.addWidget(self.btn_actualizar)
        botones_layout.addWidget(self.btn_eliminar)
        botones_layout.addWidget(self.btn_menu)
        botones_layout.addWidget(self.btn_salir)

        layout.addLayout(insert_layout)
        layout.addLayout(botones_layout)

        self.setLayout(layout)

    def get_connection(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Passw0rd!",
            database="ferreteria"
        )
        return conexion

    def menu(self):
        self.hide()
        self.objeto_ventana.show()
        

    def cargar_datos(self):
        connection = self.get_connection()

        if connection is not None:
            try:
                cursor = connection.cursor()

                query = "SELECT id_venta, id_producto, cantidad, subtotal FROM DetalleVentas"
                cursor.execute(query)

                detalles = cursor.fetchall()
                self.tabla.clearContents()
                self.tabla.setRowCount(len(detalles))

                for i, detalle in enumerate(detalles):
                    for j, dato in enumerate(detalle):
                        item = QTableWidgetItem(str(dato))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.tabla.setItem(i, j, item)

                self.tabla.clearSelection()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar datos: {e}")
            finally:
                connection.close()

    def insertar_detalle(self):
        connection = self.get_connection()

        if connection is not None:
            try:
                cursor = connection.cursor()

                query = """
                    INSERT INTO DetalleVentas (id_venta, id_producto, cantidad, subtotal)
                    VALUES (%s, %s, %s, %s);
                """
                registro = (
                    int(self.txt_id_venta.text()),
                    int(self.txt_id_producto.text()),
                    int(self.txt_cantidad.text()),
                    float(self.txt_subtotal.text())
                )
                cursor.execute(query, registro)
                connection.commit()
                self.cargar_datos()

                QMessageBox.information(self, "Éxito", "Detalle insertado con éxito.")
                self.limpiar_campos()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al insertar detalle: {e}")
            finally:
                connection.close()

    def actualizar_detalle(self):
        connection = self.get_connection()

        if connection is not None:
            try:
                fila_seleccionada = self.tabla.currentRow()
                if fila_seleccionada == -1:
                    QMessageBox.warning(self, "Error", "Seleccione un detalle para actualizar.")
                    return

                id_venta = self.tabla.item(fila_seleccionada, 0).text()
                id_producto = self.tabla.item(fila_seleccionada, 1).text()

                query = """
                    UPDATE DetalleVentas
                    SET cantidad = %s, subtotal = %s
                    WHERE id_venta = %s AND id_producto = %s;
                """
                registro = (
                    int(self.txt_cantidad.text()),
                    float(self.txt_subtotal.text()),
                    int(id_venta),
                    int(id_producto)
                )
                cursor = connection.cursor()
                cursor.execute(query, registro)
                connection.commit()
                self.cargar_datos()

                QMessageBox.information(self, "Éxito", "Detalle actualizado con éxito.")
                self.limpiar_campos()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al actualizar detalle: {e}")
            finally:
                connection.close()

    def eliminar_detalle(self):
        connection = self.get_connection()

        if connection is not None:
            try:
                fila_seleccionada = self.tabla.currentRow()
                if fila_seleccionada == -1:
                    QMessageBox.warning(self, "Error", "Seleccione un detalle para eliminar.")
                    return

                id_venta = self.tabla.item(fila_seleccionada, 0).text()
                id_producto = self.tabla.item(fila_seleccionada, 1).text()

                query = "DELETE FROM DetalleVentas WHERE id_venta = %s AND id_producto = %s;"
                cursor = connection.cursor()
                cursor.execute(query, (int(id_venta), int(id_producto)))
                connection.commit()
                self.cargar_datos()

                QMessageBox.information(self, "Éxito", "Detalle eliminado con éxito.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar detalle: {e}")
            finally:
                connection.close()

    def limpiar_campos(self):
        self.txt_id_venta.clear()
        self.txt_id_producto.clear()
        self.txt_cantidad.clear()
        self.txt_subtotal.clear()
    
if __name__ == "__main__":
    app = QApplication()
    #ventana = VentanaGestionProducto()
    #ventana.show()
    sys.exit(app.exec())
