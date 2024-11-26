import sys, os
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,
    QTableWidget, QAbstractItemView, QFormLayout, QLabel, QLineEdit,
    QComboBox, QSpinBox,  )
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

sys.path.append(os.path.abspath("python_19_ferreteria/ventanas_en_clase"))
from metodos import get_available_products

class VentanaGestionVentas_enClase(QWidget):
    def __init__(self):#, objeto_ventana_principal):
        super().__init__()
        self.productos_disponibles_d = {}
        self.carrito_lt = []        
        self.personalizar_ventana()
        self.personalizar_componentes()
        #self.objeto_ventana = objeto_ventana_principal

        


    def personalizar_ventana(self):
        self.setWindowTitle("Gestión de ventas")      
        self.setFixedSize(800, 300)                   
        

        # Cambiar el icono de la ventana con una ruta 
        # absoluta que se crea a partir de una relativa
        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta) # Imprime la ruta absoluta
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizar_componentes(self):
        
        layout_principal = QVBoxLayout()

        self.tblCarrito = QTableWidget()
        self.tblCarrito.setColumnCount(5)
        self.tblCarrito.setHorizontalHeaderLabels(
            ["Id", "Producto", "Cantidad", "Precio", "Subtotal"]
            )
        self.tblCarrito.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        

        # Combobox
        self.cboProducto = QComboBox()
        self.cargar_datos_combo()

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

        # Layout horizontal botones
        layout_horizontal_botones = QHBoxLayout()
        layout_horizontal_botones.addWidget(self.cboProducto)
        layout_horizontal_botones.addWidget(self.spinCantidad)
        layout_horizontal_botones.addWidget(self.btnAgregar)
        layout_horizontal_botones.addWidget(self.btnEliminarSeleccion)
        layout_horizontal_botones.addWidget(self.btnEliminarTodo)
        
        # Boton confirmar venta
        self.btnVender = QPushButton("Vender")
        self.btnVender.clicked.connect(self.vender)                

        # Etiqueta
        self.lblTotal = QLabel("Total: €0.00")
        #self.lblTotal.setAlignment(Qt.AlignRight)
    

        layout_principal.addWidget(self.tblCarrito)
        layout_principal.addLayout(layout_horizontal_botones)
        #layout_principal.addWidget(self.lblTotal)
        layout_horizontal_botones.addWidget(self.lblTotal)
        layout_horizontal_botones.addWidget(self.btnVender)
        self.setLayout(layout_principal) 

    def cargar_datos_combo(self):
        self.productos_disponibles_d = get_available_products()
        print("Productos disponibles:", self.productos_disponibles_d)
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
            QMessageBox.critical(
                self,
                "Error",
                f"Stock insuficiente. Máximo disponible: {stock}"
            )
            return
        
        self.productos_disponibles_d[producto_seleccionado] = (id_producto, nombre, precio, stock - cantidad)

        subtotal = round(precio * cantidad,2)
        self.carrito_lt.append([id_producto, nombre, cantidad, precio, subtotal])
        self.actualizar_tabla_carrito()


    def actualizar_tabla_carrito(self):
        self.tblCarrito.setRowCount(len(self.carrito_lt))
        total = 0
        for fila, (id_producto, nombre, cantidad, precio, subtotal) in enumerate(self.carrito_lt):
            total = total + subtotal
            # Pintar los datos en la tabla
            self.tblCarrito.setItem(fila, 0, QTableWidgetItem(str(id_producto)))
            self.tblCarrito.setItem(fila, 1, QTableWidgetItem(nombre))
            self.tblCarrito.setItem(fila, 2, QTableWidgetItem(str(cantidad)))
            self.tblCarrito.setItem(fila, 3, QTableWidgetItem(str(precio)))
            self.tblCarrito.setItem(fila, 4, QTableWidgetItem(f"{subtotal:.2f}"))  
        self.lblTotal.setText(f"Total: €{total:.2f}")

    def eliminar_seleccion(self):
        fila_seleccionada = self.tblCarrito.currentRow()  # Obtener fila seleccionada
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "No hay ninguna fila seleccionada")
            return

        # Recuperar datos de la fila seleccionada
        id_producto = self.tblCarrito.item(fila_seleccionada, 0).text()
        cantidad = int(self.tblCarrito.item(fila_seleccionada, 2).text())
        producto_seleccionado = next(
            (key for key, value in self.productos_disponibles_d.items() if str(value[0]) == id_producto),
            None
        )

        if producto_seleccionado:
            # Actualizar el stock del producto en el diccionario
            id_producto, nombre, precio, stock = self.productos_disponibles_d[producto_seleccionado]
            self.productos_disponibles_d[producto_seleccionado] = (id_producto, nombre, precio, stock + cantidad)

        # Eliminar el producto del carrito
        del self.carrito_lt[fila_seleccionada]

        # Actualizar la tabla
        self.actualizar_tabla_carrito()
        QMessageBox.information(self, "Éxito", "Producto eliminado del carrito")


    def vender(self):
        if not self.carrito_lt:
            QMessageBox.warning(self, "Advertencia", "El carrito está vacío, no hay nada que vender")
            return

        # Simular el registro de la venta
        try:
            # Puedes reemplazar esto con la lógica para registrar la venta en la base de datos
            print("Registrando la venta:", self.carrito_lt)
            
            # Reiniciar el carrito y la tabla
            self.carrito_lt.clear()
            self.actualizar_tabla_carrito()
            QMessageBox.information(self, "Éxito", "Venta registrada correctamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo completar la venta: {str(e)}")


    def eliminar_todo(self):
        if not self.carrito_lt:
            QMessageBox.warning(self, "Advertencia", "El carrito ya está vacío")
            return

        # Restablecer los stocks de los productos
        for id_producto, nombre, cantidad, precio, subtotal in self.carrito_lt:
            producto_seleccionado = next(
                (key for key, value in self.productos_disponibles_d.items() if str(value[0]) == str(id_producto)),
                None
            )
            if producto_seleccionado:
                _, _, _, stock = self.productos_disponibles_d[producto_seleccionado]
                self.productos_disponibles_d[producto_seleccionado] = (id_producto, nombre, precio, stock + cantidad)

        # Vaciar el carrito
        self.carrito_lt.clear()

        # Actualizar la tabla
        self.actualizar_tabla_carrito()
        QMessageBox.information(self, "Éxito", "Todos los productos han sido eliminados del carrito")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaGestionVentas_enClase()
    ventana.show()
    sys.exit(app.exec())