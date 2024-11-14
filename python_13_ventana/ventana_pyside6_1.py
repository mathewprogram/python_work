#pip install PySide6
#https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html - documentacion de QWidget

import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())







"""
app = QApplication(sys.argv)
ventana = QWidget()
ventana.show()
sys.exit(app.exec())
"""