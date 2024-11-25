import sys, os
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,
    QTableWidget, QAbstractItemView, QFormLayout, QLabel, QLineEdit,
    QComboBox, QDateTimeEdit)
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QDateTime



class VentanaGestionCajero(QWidget):
    def __init__(self, objeto_ventana_principal):
        super().__init__()
        
        self.personalizar_ventana()
        self.personalizar_componentes()
        self.cargar_datos()
        self.objeto_ventana = objeto_ventana_principal
        



    def personalizar_ventana(self):
        self.setWindowTitle("Gestión Cajero")                          # Título de la ventana
        self.setFixedSize(800, 600)                                         # Tamaño de la ventana
        #self.setStyleSheet("background-color: lightgray; color: black;")   # Color de fondo

        # Cambiar el icono de la ventana con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta) # Imprime la ruta absoluta
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizar_componentes(self):
        layout = QVBoxLayout()

        # Tabla de ventas
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Total"])

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        fuente_encabezados = QFont()
        fuente_encabezados.setPointSize(14)  # Tamaño de fuente
        fuente_encabezados.setBold(True)  # Negrita
        self.tabla.horizontalHeader().setFont(fuente_encabezados)
        layout.addWidget(self.tabla)

        # Selector de fecha y hora
        self.date_time_picker = QDateTimeEdit(self)
        self.date_time_picker.setCalendarPopup(True)
        self.date_time_picker.setDateTime(QDateTime.currentDateTime())  # Fecha actual por defecto
        self.date_time_picker.setDisplayFormat("yyyy-MM-dd HH:mm")  # Formato de fecha y hora

        self.txt_total_venta = QLineEdit()
        self.txt_total_venta.setPlaceholderText("Total de venta")

        self.btn_insertar = QPushButton("Insertar venta")
        self.btn_insertar.clicked.connect(self.insertar_venta)
        self.btn_actualizar = QPushButton("Actualizar venta")
        self.btn_actualizar.clicked.connect(self.actualizar_venta)
        self.btn_eliminar = QPushButton("Eliminar venta")
        self.btn_eliminar.clicked.connect(self.eliminar_venta)
        self.btn_menu = QPushButton("Menu")
        self.btn_menu.clicked.connect(self.menu)
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)

        insert_layout = QHBoxLayout()
        insert_layout.addWidget(self.date_time_picker)
        insert_layout.addWidget(self.txt_total_venta)

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
                query = "SELECT fecha, total FROM Venta"
                cursor.execute(query)

                ventas = cursor.fetchall()
                self.tabla.clearContents()
                self.tabla.setRowCount(len(ventas))

                fuente_contenido = QFont()
                fuente_contenido.setPointSize(12)
                fuente_contenido.setBold(True)

                for i, venta in enumerate(ventas):
                    item_fecha = QTableWidgetItem(str(venta[0]))
                    item_total = QTableWidgetItem(f"{venta[1]:.2f}")

                    item_fecha.setFont(fuente_contenido)
                    item_total.setFont(fuente_contenido)

                    item_fecha.setTextAlignment(Qt.AlignCenter)
                    item_total.setTextAlignment(Qt.AlignCenter)

                    self.tabla.setItem(i, 0, item_fecha)
                    self.tabla.setItem(i, 1, item_total)

                self.tabla.clearSelection()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar datos: {e}")
            finally:
                connection.close()


           

    def insertar_venta(self):
        connection = self.get_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                fecha = self.date_time_picker.dateTime().toString("yyyy-MM-dd HH:mm:ss")
                total = self.txt_total_venta.text().strip()

                if not total or not total.replace('.', '', 1).isdigit():
                    QMessageBox.critical(self, "Error", "El total debe ser un número válido.")
                    return

                query = "INSERT INTO Venta (fecha, total) VALUES (%s, %s)"
                cursor.execute(query, (fecha, float(total)))
                connection.commit()

                self.cargar_datos()
                self.txt_total_venta.clear()
                QMessageBox.information(self, "Éxito", "Venta insertada con éxito.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al insertar venta: {e}")
            finally:
                connection.close()

    def actualizar_venta(self):
        connection = self.get_connection()
        if connection is not None:
            try:
                fila_seleccionada = self.tabla.currentRow()
                if fila_seleccionada == -1:
                    QMessageBox.critical(self, "Error", "Debe seleccionar una venta.")
                    return

                id_venta = self.tabla.item(fila_seleccionada, 0).data(Qt.UserRole)
                nueva_fecha = self.date_time_picker.dateTime().toString("yyyy-MM-dd HH:mm:ss")
                nuevo_total = self.txt_total_venta.text().strip()

                if not nuevo_total or not nuevo_total.replace('.', '', 1).isdigit():
                    QMessageBox.critical(self, "Error", "El total debe ser un número válido.")
                    return

                query = "UPDATE Venta SET fecha = %s, total = %s WHERE id_venta = %s"
                cursor = connection.cursor()
                cursor.execute(query, (nueva_fecha, float(nuevo_total), id_venta))
                connection.commit()

                self.cargar_datos()
                QMessageBox.information(self, "Éxito", "Venta actualizada con éxito.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al actualizar venta: {e}")
            finally:
                connection.close()

    def eliminar_venta(self):
        connection = self.get_connection()
        if connection is not None:
            try:
                fila_seleccionada = self.tabla.currentRow()
                if fila_seleccionada == -1:
                    QMessageBox.critical(self, "Error", "Debe seleccionar una venta.")
                    return

                id_venta = self.tabla.item(fila_seleccionada, 0).data(Qt.UserRole)
                query = "DELETE FROM Venta WHERE id_venta = %s"
                cursor = connection.cursor()
                cursor.execute(query, (id_venta,))
                connection.commit()

                self.cargar_datos()
                QMessageBox.information(self, "Éxito", "Venta eliminada con éxito.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar venta: {e}")
            finally:
                connection.close()

    
    

    
if __name__ == "__main__":
    app = QApplication()
    #ventana = VentanaGestionProducto()
    #ventana.show()
    sys.exit(app.exec())
