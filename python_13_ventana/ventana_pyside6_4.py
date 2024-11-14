import sys,os
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.personalizarVentana()
        self.personalizarComponentes()
        self.cargarDatosTabla()

    def personalizarVentana(self):
        self.setFixedSize(480, 330) #Tamaño de la ventana ancho y altura
        self.setWindowTitle("VENTANA PYQT5") #Título para la ventana
        self.setStyleSheet("background-color: lightgray;") #Color de fondo para la ventana

        # Cambiar el icono de la ventana con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "python6_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta) 
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizarComponentes(self):
        self.tblMostrar = QTableWidget(self)
        self.tblMostrar.setColumnCount(3)
        self.tblMostrar.setRowCount(0)
        self.tblMostrar.setHorizontalHeaderLabels(["ID", "NOMBRE", "ESTATURA"])
        self.tblMostrar.horizontalHeader().setStyleSheet("color: black; background-color: white;")
        self.tblMostrar.verticalHeader().setStyleSheet("color: black; background-color: white;")
        self.tblMostrar.horizontalHeader().setFont(QFont("Courier New", 16, QFont.Bold)) #Fuente de letra y tamaño de letra de la cabecera
        self.tblMostrar.setFont(QFont("Courier New", 16)) #Fuente de letra y tamaño de letra del cuerpo
        self.tblMostrar.setStyleSheet("color: black; background-color: lightgray;") #Color de fondo del cuerpo
        self.tblMostrar.setGeometry(10, 10, 460, 307)

        header = self.tblMostrar.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Ajustar automáticamente el ancho de las columnas
        header.setStretchLastSection(True)  # Estirar la última sección (última columna) para llenar el espacio

    def cargarDatosTabla(self):
        self.limpiarTabla()
        for i in range(len(id)):
            self.tblMostrar.insertRow(i) #Añadir una nueva fila en blanco en la posición i: 0,1,2,3...14
            self.tblMostrar.setItem(i, 0, QTableWidgetItem(str(id[i]))) #Posición i: fila, 0: columna
            self.tblMostrar.setItem(i, 1, QTableWidgetItem(nombre[i]))
            self.tblMostrar.setItem(i, 2, QTableWidgetItem(self.decimalesfijo(estatura[i])))
        
        # Almacenar el índice de la columna "ID" para ajustar la alineación al centro más tarde
        self.indice_id = 0 #self.indice_id = self.tblMostrar.horizontalHeader().visualIndex(0)
        # Almacenar el índice de la columna "ESTATURA" para ajustar la alineación a la derecha 
        self.indice_estatura = 2 #self.indice_estatura = self.tblMostrar.horizontalHeader().visualIndex(2)
        for i in range(self.tblMostrar.rowCount()):
            # Alinear la columna "ID" al centro
            item0 = self.tblMostrar.item(i, self.indice_id)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            # Alinear la columna "ESTATURA" a la derecha
            item2 = self.tblMostrar.item(i, self.indice_estatura)
            item2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    
    def decimalesfijo(self,estatura):
        parte_entera = int(estatura)
        parte_decimal = estatura - parte_entera
        parte_decimal_1 = int(parte_decimal * 100)
        if parte_decimal_1 % 10 == 0:
           return str(estatura) + "0"
        else:
           return str(estatura)

    def limpiarTabla(self):
        self.tblMostrar.setRowCount(0)

id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nombre = ["Luis", "Miguel", "Carlos", "Javier", "Carmen", "Maria", "Lucia", "Carmen", "Arturo", "Ismael", "Delly", "Vanessa", "Melissa", "Raul", "Arturo"]
estatura = [1.72, 1.73, 1.74, 1.75, 1.76, 1.60, 1.61, 1.62, 1.63, 1.64, 1.65, 1.56, 1.64, 1.67, 1.61]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())