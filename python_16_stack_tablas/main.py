
import sys
from PySide6.QtWidgets import (
     QVBoxLayout, QApplication, QMainWindow, QWidget, 
     QLabel, QLineEdit, QPushButton,
     QHBoxLayout, QStackedLayout
)

from ventana_seleccionfutbol import Ventana as v1
from ventana_seleccion_entrenador import Ventana as v2
from ventana_seleccion_masajista import Ventana as v3
from ventana_seleccion_futbolista import Ventana as v4


def mostrar_panel_1():
    layout_stack.setCurrentIndex(0)

def mostrar_panel_2():
    layout_stack.setCurrentIndex(1)

def mostrar_panel_3():
    layout_stack.setCurrentIndex(2)

def mostrar_panel_4():
    layout_stack.setCurrentIndex(3)

# 0. CONSTRUIR UNA APLICACION
app = QApplication(sys.argv) 

# 1. CREAR LA VENTANA PRINCIPAL
ventana_principal = QMainWindow()
ventana_principal.setWindowTitle("Herencia Selección de Fútbol")
ventana_principal.resize(800, 460)

# 2. CREAR UN PANEL PRINCIPAL QWIDGET
panel_principal = QWidget()

# 3. CREAR UN ADMINISTRADOR PRINCIPAL PARA ELL PANEL PRINCIPAL
layout_principal = QVBoxLayout()

# 4. CREAR COMPONENTES Y AÑADIRLOS AL ADMINSTRADOR PRINCIPAL
# PANEL TABLA 1
panel_1 = QWidget()
layout_1 = QVBoxLayout()
ventana1 = v1()
tblMostrar1 = ventana1.obtener_tabla()

layout_1.addWidget(tblMostrar1)
panel_1.setLayout(layout_1)

# PANEL TABLA 2
panel_2 = QWidget()
layout_2 = QVBoxLayout()
ventana2 = v2()
tblMostrar2 = ventana2.obtener_tabla()

layout_2.addWidget(tblMostrar2)
panel_2.setLayout(layout_2)

# PANEL TABLA 3
panel_3 = QWidget()
layout_3 = QVBoxLayout()
ventana3 = v3()
tblMostrar3 = ventana3.obtener_tabla()

layout_3.addWidget(tblMostrar3)
panel_3.setLayout(layout_3)

# PANEL TABLA 4
panel_4 = QWidget()
layout_4 = QVBoxLayout()
ventana4 = v4()
tblMostrar4 = ventana4.obtener_tabla()

layout_4.addWidget(tblMostrar4)
panel_4.setLayout(layout_4)

layout_stack = QStackedLayout()
layout_stack.addWidget(panel_1) # 0
layout_stack.addWidget(panel_2) # 1
layout_stack.addWidget(panel_3) # 2
layout_stack.addWidget(panel_4) # 3

# LAYOUT DE LOS 4 BOTONES
layout_4 = QHBoxLayout()
btn1 = QPushButton("Base de Datos")
btn2 = QPushButton("Entrenadores")
btn3 = QPushButton("Masajistas")
btn4 = QPushButton("Futbolistas")
btn5 = QPushButton("Salir")
btn1.clicked.connect(mostrar_panel_1)
btn2.clicked.connect(mostrar_panel_2)
btn3.clicked.connect(mostrar_panel_3)
btn4.clicked.connect(mostrar_panel_4)
btn5.clicked.connect(ventana_principal.close)

layout_4.addWidget(btn1)
layout_4.addWidget(btn2)
layout_4.addWidget(btn3)
layout_4.addWidget(btn4)
layout_4.addWidget(btn5)

layout_principal.addLayout(layout_stack)
layout_principal.addLayout(layout_4)

# 5. PONER EL ADMINISTRADOR PRINCIPAL AL PANEL PRINCIPAL
panel_principal.setLayout(layout_principal)

# 6. PONER EL PANEL PRINCIPAL A LA VENTANA PRINCIPAL
ventana_principal.setCentralWidget(panel_principal)

# 7. MOSTRAR VENTANA PRINCIPAL
ventana_principal.show()

# 8. EJECUTAR APLICACION
sys.exit(app.exec())  
