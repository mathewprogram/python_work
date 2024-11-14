import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QRadioButton, QComboBox

# 0. Crear la aplicación de Qt
app = QApplication(sys.argv)

# 1. Crear la ventana principal
ventana_principal = QMainWindow()

# 2. Crear un panel qwidget
panel = QWidget()

# 3. Crear un administrador(layout) del panel
layoutGrid = QGridLayout()

# 4. Crear componentes y gestionarlos
    # Name 
lblName = QLabel("Name: ")
txtName = QLineEdit()
layoutGrid.addWidget(lblName, 0, 0)
layoutGrid.addWidget(txtName, 0, 1)

    # Surname
lblSurname = QLabel("Surname: ")
txtSurname = QLineEdit()
layoutGrid.addWidget(lblSurname, 1, 0)
layoutGrid.addWidget(txtSurname, 1, 1)

    # Send
btnSend = QPushButton("Send")
layoutGrid.addWidget(btnSend, 2, 1)


# 5. Asignar el administrador(layout) al panel
panel.setLayout(layoutGrid)

# 6. Asignar el panel a la ventana principal
ventana_principal.setCentralWidget(panel)

# 7. Mostrar la ventana principal
ventana_principal.show()

sys.exit(app.exec())
