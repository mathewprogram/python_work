import sys,os
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QWidget, QPushButton
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.personalizarVentana()
        self.personalizarComponentes()

    def personalizarVentana(self):
        self.setWindowTitle("VENTANA ComboBox")  # Título para la ventana
        self.setFixedSize(480, 330)  # Tamaño de la ventana ancho y altura
        self.setStyleSheet("background-color: lightgray; color: black;")  # Color de fondo para la ventana

        # Cambiar el icono de la ventana con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "python_13_ventana/icon.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta) # python_13_ventana/icon.png
        self.setWindowIcon(QIcon(ruta_absoluta))

        self.pnlPrincipal = QWidget() # Crear un contenedor
        self.setCentralWidget(self.pnlPrincipal) # Establecer el contenedor como principal para nuestra ventana
      

    def personalizarComponentes(self):
        self.lblTitulo = QLabel("SELECCIONAR UNA CIUDAD DE UN COMBOBOX", self.pnlPrincipal)
        self.lblTitulo.setFont(QFont("Courier New", 15, QFont.Bold))
        self.lblTitulo.setAlignment(Qt.AlignCenter)
        self.lblTitulo.setGeometry(0, 0, 480, 20)
        self.lblTitulo.setStyleSheet("background-color: black; color: yellow;")
        
        self.lblCiudad = QLabel("SELECCIONE CIUDAD", self.pnlPrincipal)
        self.lblCiudad.setFont(QFont("Courier New", 15, QFont.Bold))
        self.lblCiudad.setAlignment(Qt.AlignCenter)
        self.lblCiudad.setGeometry(0, 80, 480, 20)

        self.cboCiudad = QComboBox(self.pnlPrincipal)
        self.cboCiudad.setFont(QFont("Courier New", 14, QFont.Bold))
        self.cboCiudad.setGeometry(145, 160, 190, 20)
        self.cboCiudad.addItem("Seleccione Ciudad")
        self.cboCiudad.addItem("Barcelona")
        self.cboCiudad.addItem("Bilbao")
        self.cboCiudad.addItem("Madrid")
        self.cboCiudad.addItem("Sevilla")
        self.cboCiudad.addItem("Zaragoza")
        self.cboCiudad.currentIndexChanged.connect(self.itemSeleccionado)

        self.btoReiniciar = QPushButton(self.pnlPrincipal)
        self.btoReiniciar.setText("REINICIAR")
        self.btoReiniciar.setGeometry(150, 240, 80, 20)
        self.btoReiniciar.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btoReiniciar.clicked.connect(self.reiniciar)

        self.btoSalir = QPushButton(self.pnlPrincipal)
        self.btoSalir.setText("SALIR")
        self.btoSalir.setGeometry(250, 240, 80, 20)
        self.btoSalir.setFont(QFont("Courier New", 14, QFont.Bold))
        self.btoSalir.clicked.connect(self.salir)
    
    def reiniciar(self):
        self.cboCiudad.setCurrentIndex(0)

    def salir(self):
        sys.exit()

    def itemSeleccionado(self, index):
        ciudad = self.cboCiudad.currentText()
        if ciudad == "Madrid":
            self.lblCiudad.setText("Madrid es capital del Reyno de España.")
        elif ciudad == "Barcelona":
            self.lblCiudad.setText("Barcelona es capital de la C.A. de Cataluña.")
        elif ciudad == "Sevilla":
            self.lblCiudad.setText("Sevilla es capital de la C.A. de Andalucia.")
        elif ciudad == "Bilbao":
            self.lblCiudad.setText("Biblao es capital de la C.A. de Vizcaya.")
        elif ciudad == "Zaragoza":
            self.lblCiudad.setText("Zaragoza es capital de la C.A. de Aragon.")
        else:
            self.lblCiudad.setText("SELECCIONE CIUDAD")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())