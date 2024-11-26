from datetime import datetime
import sys, os
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QVBoxLayout, QHBoxLayout, 
    QComboBox, QSpinBox, QLabel, QMessageBox
)
from PySide6.QtGui import QIcon

class VentanaGestionVentas_enClase(QWidget):
    def __init__(self, objeto_ventana_principal):
        super().__init__()
        self.productos_disponibles_d = {}
        self.carrito_lt = []
        self.connection = self.get_connection()
        self.personalizar_ventana()
        self.personalizar_componentes()
        self.cargar_datos_combo()
        self.objeto_ventana = objeto_ventana_principal

    def personalizar_ventana(self):
        self.setWindowTitle("Gestión de ventas")
        self.setFixedSize(800, 300)

        # Cambiar el icono de la ventana
        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizar_componentes(self):
        layout_principal = QVBoxLayout()

        # Tabla carrito
        self.tblCarrito = QTableWidget()
        self.tblCarrito.setColumnCount(5)
        self.tblCarrito.setHorizontalHeaderLabels(["Id", "Producto", "Cantidad", "Precio", "Subtotal"])
        self.tblCarrito.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Combobox
        self.cboProducto = QComboBox()

        # Spin
        self.spinCantidad = QSpinBox()
        self.spinCantidad.setRange(1, 100)

        # Botónes
        self.btnAgregar = QPushButton("Agregar")
        self.btnAgregar.clicked.connect(self.agregar_al_carrito)
        self.btnEliminarSeleccion = QPushButton("Eliminar")
        self.btnEliminarSeleccion.clicked.connect(self.eliminar_seleccion)
        self.btnEliminarTodo = QPushButton("Eliminar todo")
        self.btnEliminarTodo.clicked.connect(self.eliminar_todo)
        self.btnMenu = QPushButton("Menú")
        self.btnMenu.clicked.connect(self.menu)

        # Layout de botones
        layout_horizontal_botones = QHBoxLayout()
        layout_horizontal_botones.addWidget(self.cboProducto)
        layout_horizontal_botones.addWidget(self.spinCantidad)
        layout_horizontal_botones.addWidget(self.btnAgregar)
        layout_horizontal_botones.addWidget(self.btnEliminarSeleccion)
        layout_horizontal_botones.addWidget(self.btnEliminarTodo)
        layout_horizontal_botones.addWidget(self.btnMenu)

        # Botón de confirmar venta
        self.btnVender = QPushButton("Vender")
        self.btnVender.clicked.connect(self.vender)

        # Etiqueta Total
        self.lblTotal = QLabel("Total: €0.00")

        layout_principal.addWidget(self.tblCarrito)
        layout_principal.addLayout(layout_horizontal_botones)
        layout_horizontal_botones.addWidget(self.lblTotal)
        layout_horizontal_botones.addWidget(self.btnVender)
        self.setLayout(layout_principal)

    def get_connection(self):
        # Conexión a la base de datos MySQL
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Passw0rd!",
                database="ferreteria"
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            return None
    
    def menu(self):
        self.hide()
        self.objeto_ventana.show()

    def cargar_datos_combo(self):
        self.productos_disponibles_d = self.get_available_products()
        self.cboProducto.clear()
        self.cboProducto.addItems(self.productos_disponibles_d.keys())

    def agregar_al_carrito(self):
        producto_seleccionado = self.cboProducto.currentText()
        cantidad = self.spinCantidad.value()
        if producto_seleccionado not in self.productos_disponibles_d:
            QMessageBox.critical(self, "Error", "Producto no encontrado")
            return

        id_producto, nombre, precio, stock = self.productos_disponibles_d[producto_seleccionado]

        if cantidad > stock:
            QMessageBox.critical(self, "Error", f"Stock insuficiente. Máximo disponible: {stock}")
            return

        # Actualizar el stock
        self.productos_disponibles_d[producto_seleccionado] = (id_producto, nombre, precio, stock - cantidad)

        # Agregar al carrito
        subtotal = round(precio * cantidad, 2)
        self.carrito_lt.append([id_producto, nombre, cantidad, precio, subtotal])
        self.actualizar_tabla_carrito()

    def actualizar_tabla_carrito(self):
        self.tblCarrito.setRowCount(len(self.carrito_lt))
        total = 0
        for fila, (id_producto, nombre, cantidad, precio, subtotal) in enumerate(self.carrito_lt):
            total += subtotal
            self.tblCarrito.setItem(fila, 0, QTableWidgetItem(str(id_producto)))
            self.tblCarrito.setItem(fila, 1, QTableWidgetItem(nombre))
            self.tblCarrito.setItem(fila, 2, QTableWidgetItem(str(cantidad)))
            self.tblCarrito.setItem(fila, 3, QTableWidgetItem(str(precio)))
            self.tblCarrito.setItem(fila, 4, QTableWidgetItem(f"{subtotal:.2f}"))
        self.lblTotal.setText(f"Total: €{total:.2f}")

    def eliminar_seleccion(self):
        fila_seleccionada = self.tblCarrito.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "No hay ninguna fila seleccionada")
            return

        id_producto = self.tblCarrito.item(fila_seleccionada, 0).text()
        cantidad = int(self.tblCarrito.item(fila_seleccionada, 2).text())
        producto_seleccionado = next(
            (key for key, value in self.productos_disponibles_d.items() if str(value[0]) == id_producto),
            None
        )

        if producto_seleccionado:
            id_producto, nombre, precio, stock = self.productos_disponibles_d[producto_seleccionado]
            self.productos_disponibles_d[producto_seleccionado] = (id_producto, nombre, precio, stock + cantidad)

        del self.carrito_lt[fila_seleccionada]
        self.actualizar_tabla_carrito()
        QMessageBox.information(self, "Éxito", "Producto eliminado del carrito")

    def vender(self):
        connection = self.get_connection()
        if not connection:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos.")
            return

        cursor = connection.cursor()

        if not self.carrito_lt:
            QMessageBox.warning(self, "Advertencia", "El carrito está vacío, no hay nada que vender")
            return

        try:
            total = sum(subtotal for _, _, _, _, subtotal in self.carrito_lt)

            # Insertar venta
            query_venta = "INSERT INTO Venta (fecha, total) VALUES (%s, %s)"
            cursor.execute(query_venta, (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), total))
            connection.commit()

            # Obtener el ID de la venta
            id_venta = cursor.lastrowid

            # Insertar detalles de la venta
            query_detalle = "INSERT INTO DetalleVentas (id_venta, id_producto, cantidad, subtotal) VALUES (%s, %s, %s, %s)"
            for id_producto, _, cantidad, _, subtotal in self.carrito_lt:
                cursor.execute(query_detalle, (id_venta, id_producto, cantidad, subtotal))
            connection.commit()

            # Reiniciar el carrito y actualizar la tabla de productos
            self.carrito_lt.clear()
            self.productos_disponibles_d = self.get_available_products()
            self.cargar_datos_combo()
            self.spinCantidad.setValue(1)
            self.actualizar_tabla_carrito()
            QMessageBox.information(self, "Éxito", "Venta registrada correctamente")
            

        except Exception as e:
            connection.rollback()
            QMessageBox.critical(self, "Error", f"No se pudo completar la venta: {str(e)}")
        finally:
            cursor.close()
            connection.close()

    def eliminar_todo(self):
        if not self.carrito_lt:
            QMessageBox.warning(self, "Advertencia", "El carrito ya está vacío")
            return

        for id_producto, nombre, cantidad, precio, subtotal in self.carrito_lt:
            producto_seleccionado = next(
                (key for key, value in self.productos_disponibles_d.items() if str(value[0]) == str(id_producto)),
                None
            )
            if producto_seleccionado:
                _, _, _, stock = self.productos_disponibles_d[producto_seleccionado]
                self.productos_disponibles_d[producto_seleccionado] = (id_producto, nombre, precio, stock + cantidad)

        self.carrito_lt.clear()
        self.actualizar_tabla_carrito()
        QMessageBox.information(self, "Éxito", "Todos los productos han sido eliminados del carrito")

    def get_available_products(self):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT id_producto, nombre, precio, stock FROM Producto WHERE stock > 0"
                cursor.execute(query)
                productos_lt = cursor.fetchall()
                productos_disponibles_d = {f"{p[0]} - {p[1]} ({p[3]})": p for p in productos_lt}
                return productos_disponibles_d
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar los productos: {str(e)}")
            finally:
                cursor.close()
                connection.close()
        return {}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #ventana = VentanaGestionVentas()
    #ventana.show()
    sys.exit(app.exec())
