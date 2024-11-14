import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QRadioButton, QComboBox

# 0. Crear la aplicación de Qt
app = QApplication(sys.argv)

# 1. Crear la ventana principal
ventana_principal = QMainWindow()

# 2. Crear un panel qwidget
panel = QWidget()

# 3. Crear un administrador(layout) del panel
layout = QGridLayout()

# 4. Crear componentes y gestionarlos

lblName = QLabel("Nombre")
txtName = QLineEdit()


layout.addWidget(lblName, 0, 0)
layout.addWidget(txtName, 0, 1)













ventana_principal.show()

sys.exit(app.exec())