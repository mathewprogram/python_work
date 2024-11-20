import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QCalendarWidget
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QDate

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.personalizarVentana()
        self.personalizarComponentes()

    def personalizarVentana(self):
        self.setWindowTitle("Calendario")

        ruta_relativa = "python_13_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta)
        self.setWindowIcon(QIcon(ruta_absoluta))

        self.setStyleSheet("color: black; background-color: lightgray;")
        self.setFixedSize(480, 330) 

        self.pnlPrincipal = QWidget() # Crear un contenedor
        self.setCentralWidget(self.pnlPrincipal) # Establecer el contenedor como principal para nuestra ventana
    
    def personalizarComponentes(self):
        self.lblFecha = QLabel("Fecha Seleccionada", self.pnlPrincipal)
        self.lblFecha.setFont(QFont("Courier New", 14, QFont.Bold))
        self.lblFecha.setStyleSheet("color: #FF0000;")
        self.lblFecha.setAlignment(Qt.AlignCenter)
        self.lblFecha.setGeometry(0, 290, 480, 20)

        self.calendario = QCalendarWidget(self.pnlPrincipal)
        self.calendario.setGridVisible(True)
        self.calendario.setGeometry(10, 10, 460, 250)
        self.calendario.clicked[QDate].connect(self.mostrarFechaSeleccionada) #1 

    def mostrarFechaSeleccionada(self, fecha):
        fecha_str = "{:02d}/{:02d}/{:04d}".format(fecha.day(), fecha.month(), fecha.year())
        self.lblFecha.setText(fecha_str)  
        print(fecha.toString())  
        print(fecha.day())
        print(fecha.month())
        print(fecha.year()) 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

'''
1. Entonces, aunque no se pasa explícitamente la fecha como argumento cuando se llama 
a mostrarFechaSeleccionada, el argumento fecha se llena automáticamente con la fecha 
seleccionada cuando el método es llamado por la señal clicked del QCalendarWidget.
'''

"""
Ejericio 1: Traer los insert del main.py a fecha.py y en vez de que la fecha se muestre 
en un label, creamos una nueva cajita, donde se muestre la fecha seleccionada.
Esa cajita debe ser la fecha de naciminento de la persona.
Luego atraves de un boton enviamos los datos a la base de datos.
"""