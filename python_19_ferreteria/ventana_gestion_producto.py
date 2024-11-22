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


class VentanaGestionUsuarios(QWidget):
    def __init__(self):
        super().__init__()
        self.personalizar_ventana()
        self.personalizar_componentes()
        self.cargar_datos()


    def personalizar_ventana(self):
        self.setWindowTitle("Gestión de productos")                          # Título de la ventana
        self.setFixedSize(800, 600)                                         # Tamaño de la ventana
        #self.setStyleSheet("background-color: lightgray; color: black;")   # Color de fondo

        # Cambiar el icono de la ventana con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta) # Imprime la ruta absoluta
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizar_componentes(self):
        layout = QVBoxLayout()

        # Tabla de usuarios
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Descripción", "Precio", "Stock", "Categoría"])

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        fuente_encabezados = QFont()
        fuente_encabezados.setPointSize(14)  # Tamaño de fuente
        fuente_encabezados.setBold(True)  # Negrita
        self.tabla.horizontalHeader().setFont(fuente_encabezados)
       
        layout.addWidget(self.tabla)

        # Campos para CRUD
        self.txt_nombre_producto = QLineEdit()
        self.txt_nombre_producto.setPlaceholderText("Nombre producto")

        self.txt_descripcion = QLineEdit()
        self.txt_descripcion.setPlaceholderText("Descripcion")

        self.txt_precio = QLineEdit()
        self.txt_precio.setPlaceholderText("Precio")

        self.txt_stock = QLineEdit()
        self.txt_stock.setPlaceholderText("Stock")

        self.txt_categoria_edit = QLineEdit()
        self.txt_categoria_edit.setPlaceholderText("Categorías")

        self.cbo_categoria = QComboBox()
        # Poblar el combobox con las categorías existentes en la base de datos
        self.poblar_combo_categorias()

        # Agregar las categorías al combobox manualmente
        """        
        self.cbo_categoria.addItem("Categorías")
        self.cbo_categoria.addItem("Herramientas")
        self.cbo_categoria.addItem("Medición")
        self.cbo_categoria.addItem("Fijaciones")
        self.cbo_categoria.addItem("Construcción")
        self.cbo_categoria.addItem("Plomería")
        self.cbo_categoria.addItem("Electricidad")
        self.cbo_categoria.addItem("Pintura")
        self.cbo_categoria.addItem("Adhesivos")
        self.cbo_categoria.addItem("Seguridad")
        """

        self.btn_insertar = QPushButton("Insertar producto")
        self.btn_insertar.clicked.connect(self.insertar_producto)
        self.btn_actualizar = QPushButton("Actualizar producto")
        self.btn_actualizar.clicked.connect(self.actualizar_producto)
        self.btn_eliminar = QPushButton("Eliminar producto")
        self.btn_eliminar.clicked.connect(self.eliminar_producto)
        self.btn_mostrar_categoria = QPushButton("Mostrar categoria")
        self.btn_mostrar_categoria.clicked.connect(self.cargar_categorias)
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)

        insert_layout = QHBoxLayout()
        insert_layout.addWidget(self.txt_nombre_producto)
        insert_layout.addWidget(self.txt_descripcion)
        insert_layout.addWidget(self.txt_precio)
        insert_layout.addWidget(self.txt_stock)
        insert_layout.addWidget(self.txt_categoria_edit)
        insert_layout.addWidget(self.cbo_categoria)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.btn_insertar)
        botones_layout.addWidget(self.btn_actualizar)
        botones_layout.addWidget(self.btn_eliminar)
        botones_layout.addWidget(self.btn_mostrar_categoria)
        botones_layout.addWidget(self.btn_salir)        


        layout.addLayout(insert_layout)
        layout.addLayout(botones_layout)

        # Establecer el layout en la ventana principal
        self.setLayout(layout)

    def get_connection(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Passw0rd!",
            database="ferreteria"
        )
        return conexion

    def cargar_datos(self):
        connection = self.get_connection()

        if connection is not None:
            try:
                cursor = connection.cursor()

                # Consulta para obtener todos los productos de la tabla Producto
                query = "SELECT nombre, descripcion, precio, stock, categoria FROM Producto"
                cursor.execute(query)

                productos = cursor.fetchall()

                # Limpiar la tabla antes de cargar los nuevos datos
                self.tabla.clearContents()
                self.tabla.setRowCount(len(productos))  # Ajustar el número de filas según los productos

                if productos:
                    # Configurar la fuente para el contenido
                    fuente_contenido = QFont()
                    fuente_contenido.setPointSize(12)  # Tamaño de fuente
                    fuente_contenido.setBold(True)  # Negrita

                    # Mostrar los datos en la tabla
                    for i, producto in enumerate(productos):
                        # Crear los items para cada celda
                        item_nombre = QTableWidgetItem(producto[0])
                        item_descripcion = QTableWidgetItem(producto[1])
                        item_precio = QTableWidgetItem(str(producto[2]))
                        item_stock = QTableWidgetItem(str(producto[3]))
                        item_categoria = QTableWidgetItem(producto[4])

                        # Aplicar la fuente al contenido
                        item_nombre.setFont(fuente_contenido)
                        item_descripcion.setFont(fuente_contenido)
                        item_precio.setFont(fuente_contenido)
                        item_stock.setFont(fuente_contenido)
                        item_categoria.setFont(fuente_contenido)

                        # Asignar los items a la tabla
                        self.tabla.setItem(i, 0, item_nombre)
                        self.tabla.setItem(i, 1, item_descripcion)
                        self.tabla.setItem(i, 2, item_precio)
                        self.tabla.setItem(i, 3, item_stock)
                        self.tabla.setItem(i, 4, item_categoria)

                        # Alinear los textos al centro
                        item_nombre.setTextAlignment(Qt.AlignCenter)
                        item_descripcion.setTextAlignment(Qt.AlignCenter)
                        item_precio.setTextAlignment(Qt.AlignCenter)
                        item_stock.setTextAlignment(Qt.AlignCenter)
                        item_categoria.setTextAlignment(Qt.AlignCenter)

                else:
                    QMessageBox.information(self, "Información", "No se encontraron productos.")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar datos: {e}")
            finally:
                connection.close()  # Siempre cerrar la conexión


           

    def insertar_producto(self):
        connection = self.get_connection()

        if connection is not None:
            try:
                cursor = connection.cursor()

                # Determinar si se usa una categoría nueva o existente
                categoria_nueva = self.txt_categoria_edit.text().strip()  # Categoría nueva ingresada
                categoria_seleccionada = self.cbo_categoria.currentText()  # Categoría seleccionada
                categoria_final = categoria_nueva if categoria_nueva else categoria_seleccionada

                print(f"Categoria nueva: {categoria_nueva}")
                print(f"Categoria seleccionada: {categoria_seleccionada}")
                print(f"Categoria final: {categoria_final}")

                # Verificar si no se seleccionó una categoría válida
                if categoria_final == "" or categoria_final == "Categorías":
                    QMessageBox.critical(self, "Error", "Debe seleccionar o ingresar una categoría válida.")
                    return

                # Consulta de inserción
                query = "INSERT INTO Producto (nombre, descripcion, precio, stock, categoria) VALUES (%s, %s, %s, %s, %s);"
                registro_t = (
                    self.txt_nombre_producto.text(),
                    self.txt_descripcion.text(),
                    float(self.txt_precio.text()),  # Asegurar formato numérico
                    int(self.txt_stock.text()),     # Asegurar formato entero
                    categoria_final
                )

                # Ejecutar la consulta
                cursor.execute(query, registro_t)
                connection.commit()

                # Refrescar datos y campos
                self.cargar_datos()
                self.poblar_combo_categorias()  # Actualizar el combo box con la nueva categoría
                self.txt_nombre_producto.clear()
                self.txt_descripcion.clear()
                self.txt_precio.clear()
                self.txt_stock.clear()
                self.txt_categoria_edit.clear()
                self.cbo_categoria.setCurrentIndex(0)

                QMessageBox.information(self, "Éxito", "Producto insertado con éxito.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al insertar producto: {e}")
            finally:
                connection.close()  # Siempre cerrar la conexión
        else:
            QMessageBox.critical(self, "Error", "Error al conectarse a la base de datos")




    
    def actualizar_producto(self):
        connection = self.get_connection()
        if connection is not None:
            try:
                # Obtener la fila seleccionada en la tabla
                fila_seleccionada = self.tabla.currentRow()
                if fila_seleccionada == -1:
                    QMessageBox.critical(self, "Error", "Debe seleccionar un producto")
                    return
                
                # Obtener los datos del producto seleccionado
                nombre_producto_seleccionado = self.tabla.item(fila_seleccionada, 0).text()

                # Obtener los nuevos valores ingresados para actualizar el producto
                nuevo_nombre_producto = self.txt_nombre_producto.text()
                nueva_descripcion = self.txt_descripcion.text()
                nuevo_precio = self.txt_precio.text()
                nuevo_stock = self.txt_stock.text()

                # Determinar si se usa una categoría nueva o existente
                categoria_nueva = self.txt_categoria_edit.text().strip()  # Categoría nueva ingresada
                categoria_seleccionada = self.cbo_categoria.currentText()  # Categoría seleccionada
                nueva_categoria = categoria_nueva if categoria_nueva else categoria_seleccionada

                if not nueva_categoria or nueva_categoria == "Categorías":
                    QMessageBox.critical(self, "Error", "Debe seleccionar o ingresar una categoría válida.")
                    return

                # Construir la consulta según si el nombre del producto cambia o no
                if nuevo_nombre_producto == nombre_producto_seleccionado:
                    query = """
                        UPDATE Producto
                        SET descripcion = %s, precio = %s, stock = %s, categoria = %s
                        WHERE nombre = %s;
                    """
                    registro_t = (nueva_descripcion, nuevo_precio, nuevo_stock, nueva_categoria, nombre_producto_seleccionado)
                else:
                    query = """
                        UPDATE Producto
                        SET nombre = %s, descripcion = %s, precio = %s, stock = %s, categoria = %s
                        WHERE nombre = %s;
                    """
                    registro_t = (nuevo_nombre_producto, nueva_descripcion, nuevo_precio, nuevo_stock, nueva_categoria, nombre_producto_seleccionado)

                # Ejecutar la consulta de actualización
                cursor = connection.cursor()
                cursor.execute(query, registro_t)
                connection.commit()

                # Recargar los datos actualizados en la tabla
                self.cargar_datos()

                # Actualizar las categorías en el combo box si es necesario
                self.poblar_combo_categorias()

                # Limpiar los campos de entrada después de la actualización
                self.txt_nombre_producto.clear()
                self.txt_descripcion.clear()
                self.txt_precio.clear()
                self.txt_stock.clear()
                self.txt_categoria_edit.clear()
                self.cbo_categoria.setCurrentIndex(0)

                QMessageBox.information(self, "Éxito", "Producto actualizado con éxito")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al actualizar producto: {e}")
            finally:
                connection.close()  # Siempre cerrar la conexión
        else:
            QMessageBox.critical(self, "Error", "Error al conectarse a la base de datos")



    def eliminar_producto(self):
        connection = self.get_connection()

        if connection is not None:
            try:
                cursor = connection.cursor()

                # Obtener el nombre del producto seleccionado en la tabla
                nombre_producto_seleccionado = self.tabla.item(self.tabla.currentRow(), 0).text()

                # Confirmar si realmente desea eliminar el producto
                respuesta = QMessageBox.question(self, "Confirmar eliminación", 
                                                f"¿Está seguro de que desea eliminar el producto '{nombre_producto_seleccionado}'?",
                                                QMessageBox.Yes | QMessageBox.No)

                if respuesta == QMessageBox.Yes:
                    # Ejecutar la consulta de eliminación
                    query = "DELETE FROM Producto WHERE nombre = %s;"
                    cursor.execute(query, (nombre_producto_seleccionado,))
                    connection.commit()

                    # Recargar los datos actualizados en la tabla
                    self.cargar_datos()

                    # Limpiar los campos de entrada después de la eliminación
                    self.txt_nombre_producto.clear()
                    self.txt_descripcion.clear()
                    self.txt_precio.clear()
                    self.txt_stock.clear()
                    self.cbo_categoria.setCurrentIndex(0)

                    QMessageBox.information(self, "Éxito", "Producto eliminado con éxito")
                else:
                    QMessageBox.information(self, "Cancelado", "Eliminación de producto cancelada.")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar producto: {e}")
            finally:
                connection.close()  # Siempre cerrar la conexión
        else:
            QMessageBox.critical(self, "Error", "Error al conectarse a la base de datos")

    
    def cargar_categorias(self):
        connection = self.get_connection()
        if connection is not None:
            try:
                # Obtener el rol seleccionado desde el combobox
                categoria_seleccionado = self.cbo_categoria.currentText()

                # Comprobar si el rol seleccionado es "Seleccionar categoria"
                if categoria_seleccionado == "Categorias":
                    self.cargar_datos()  # Recarga todos los productos cuando no se ha seleccionado categoría
                    return

                # Comprobar si el rol seleccionado no está vacío
                if not categoria_seleccionado:
                    QMessageBox.warning(self, "Advertencia", "Seleccione una categoría")
                    return

                # Consulta para obtener todos los productos con la categoría seleccionada
                query = "SELECT nombre, descripcion, precio, stock, categoria FROM Producto WHERE categoria = %s;"
                cursor = connection.cursor()
                cursor.execute(query, (categoria_seleccionado,))
                
                # Obtener todos los productos con la categoría seleccionada
                productos = cursor.fetchall()

                # Limpiar la tabla o cualquier otro componente que muestre los resultados
                self.tabla.setRowCount(0)  # Limpiar la tabla antes de mostrar nuevos datos

                if productos:
                    # Configurar la fuente para el contenido
                    fuente_contenido = QFont()
                    fuente_contenido.setPointSize(12)  # Tamaño de fuente
                    fuente_contenido.setBold(True)  # Negrita

                    # Mostrar los datos en la tabla (suponiendo que tienes cinco columnas: nombre, descripcion, precio, stock, categoria)
                    for i, producto in enumerate(productos):
                        self.tabla.insertRow(i)

                        # Crear los items para cada celda
                        item_nombre = QTableWidgetItem(producto[0])
                        item_descripcion = QTableWidgetItem(producto[1])
                        item_precio = QTableWidgetItem(str(producto[2]))
                        item_stock = QTableWidgetItem(str(producto[3]))
                        item_categoria = QTableWidgetItem(producto[4])

                        # Aplicar la fuente al contenido
                        item_nombre.setFont(fuente_contenido)
                        item_descripcion.setFont(fuente_contenido)
                        item_precio.setFont(fuente_contenido)
                        item_stock.setFont(fuente_contenido)
                        item_categoria.setFont(fuente_contenido)

                        # Asignar los items a la tabla
                        self.tabla.setItem(i, 0, item_nombre)
                        self.tabla.setItem(i, 1, item_descripcion)
                        self.tabla.setItem(i, 2, item_precio)
                        self.tabla.setItem(i, 3, item_stock)
                        self.tabla.setItem(i, 4, item_categoria)

                        # Alinear los textos al centro
                        item_nombre.setTextAlignment(Qt.AlignCenter)
                        item_descripcion.setTextAlignment(Qt.AlignCenter)
                        item_precio.setTextAlignment(Qt.AlignCenter)
                        item_stock.setTextAlignment(Qt.AlignCenter)
                        item_categoria.setTextAlignment(Qt.AlignCenter)

                else:
                    QMessageBox.information(self, "Información", "No se encontraron productos con la categoría seleccionada")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar productos por categoría: {e}")
            finally:
                connection.close()  # Siempre cerrar la conexión

    def poblar_combo_categorias(self):
        connection = self.get_connection()
        if connection is not None:
            try:
                # Consulta para obtener todas las categorías
                query = "SELECT DISTINCT categoria FROM Producto;"
                cursor = connection.cursor()
                cursor.execute(query)
                
                # Obtener todas las categorías
                categorias = cursor.fetchall()

                # Limpiar el combobox antes de poblarlo
                self.cbo_categoria.clear()

                # Agregar las categorías al combobox
                self.cbo_categoria.addItem("Categorias")
                for categoria in categorias:
                    self.cbo_categoria.addItem(categoria[0])

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar categorías: {e}")
            finally:
                connection.close()  # Siempre cerrar la conexión




if __name__ == "__main__":
    app = QApplication()
    ventana = VentanaGestionUsuarios()
    ventana.show()
    sys.exit(app.exec_())
