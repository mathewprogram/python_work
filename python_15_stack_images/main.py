import sys
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, 
    QPushButton, QLabel, QStackedLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

# 0. CONSTRUIR UNA APLICACION
app = QApplication(sys.argv) 

# 1. CREAR LA VENTANA PRINCIPAL
ventana_principal = QMainWindow()


# 2. CREAR UN PANEL PRINCIPAL QWIDGET
panel_principal = QWidget()

# 3. CREAR UN ADMINISTRADOR PRINCIPAL PARA EL PANEL PRINCIPAL
layout_principal = QVBoxLayout()

# 4. CREAR COMPONENTES Y AÑADIRLOS AL ADMINISTRADOR PRINCIPAL
layout_stack = QStackedLayout()

# Crear lista de imágenes
images = []
relative_path = "python_15_stack_images/images"
for i in range(1, 15):
    images_path = f"{relative_path}/{i}.jpeg"
    images.append(images_path)

# Agregar imágenes al layout_stack
for image in images:
    panel = QWidget()
    layout = QVBoxLayout()
    pixmap = QPixmap(image)
    lblimage = QLabel()
    lblimage.setPixmap(pixmap.scaled(600,400))  

    pixmap = QPixmap(image)

    if pixmap.isNull():
        lblimage.setText("No se pudo cargar la imagen.")
    else:
        # Escalar la imagen para que quepa en el QLabel manteniendo la proporción
        scaled_pixmap = pixmap.scaled(
            lblimage.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        lblimage.setPixmap(scaled_pixmap)
    
    layout.addWidget(lblimage)    
    panel.setLayout(layout)
    layout_stack.addWidget(panel)  # Añadir panel al stack layout

layout_principal.addLayout(layout_stack)

# Funciones para cambiar de imagen
def mostrar_anterior():
    index = layout_stack.currentIndex()    
    if index > 0:
        layout_stack.setCurrentIndex(index - 1)
    #actualizar_botones()

def mostrar_siguiente():
    index = layout_stack.currentIndex()
    if index < layout_stack.count() - 1:
        layout_stack.setCurrentIndex(index + 1)
    #actualizar_botones()

def ir_primera():
    layout_stack.setCurrentIndex(0)
    actualizar_botones()

def ir_ultima():
    layout_stack.setCurrentIndex(layout_stack.count() - 1)
    actualizar_botones()

def actualizar_botones():
    """Actualiza la visibilidad de los botones según la posición actual."""
    index = layout_stack.currentIndex()
    btnAnterior.setVisible(index > 0)
    btnSiguiente.setVisible(index < layout_stack.count() - 1)
    btnPrimera.setVisible(index > 0)
    btnUltima.setVisible(index < layout_stack.count() - 1)

# Crear botones de navegación
layout_botones = QHBoxLayout()
layout_principal.addLayout(layout_botones)

btnPrimera = QPushButton("Primera")
btnPrimera.clicked.connect(ir_primera)
layout_botones.addWidget(btnPrimera)

btnAnterior = QPushButton("<<")
btnAnterior.clicked.connect(mostrar_anterior)
layout_botones.addWidget(btnAnterior)

btnSiguiente = QPushButton(">>")
btnSiguiente.clicked.connect(mostrar_siguiente)
layout_botones.addWidget(btnSiguiente)
    
btnUltima = QPushButton("Última")
btnUltima.clicked.connect(ir_ultima)
layout_botones.addWidget(btnUltima)

# Configurar visibilidad inicial de botones
#actualizar_botones()       si quieres que los botones estén ocultos al inicio descomenta esta línea

# 5. PONER EL ADMINISTRADOR PRINCIPAL AL PANEL PRINCIPAL
panel_principal.setLayout(layout_principal)

# 6. PONER EL PANEL PRINCIPAL A LA VENTANA PRINCIPAL
ventana_principal.setCentralWidget(panel_principal)

# 7. MOSTRAR VENTANA PRINCIPAL
ventana_principal.show()

# 8. EJECUTAR APLICACION
sys.exit(app.exec())
