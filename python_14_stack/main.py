import sys, sqlite3
from PySide6.QtWidgets import *
from PySide6.QtCore import QDate, Qt

def get_connection():
    nra = "/Users/mihaitamatei/Documents/personal/Projects/python/python_work_in_class/python_14/persona.sqlite3"
    connection = None
    try:
        connection = sqlite3.connect(nra)
    except sqlite3.Error as e:
        connection = None
    return connection

def insert(nombre, apellido, sexo):
    connection = get_connection()
    if connection is not None:
        QMessageBox.information(None, "Data", "Connection established.")
        
        try:
            cursor = connection.cursor()
            query = "INSERT INTO Persona (nombre, apellido, sexo) VALUES (?, ?, ?);"
            registro_t = (nombre, apellido, sexo)
            cursor.execute(query, registro_t)
            connection.commit()
            QMessageBox.information(None, "Data", "Data inserted.")
        except sqlite3.Error as e:
            QMessageBox.critical(None, "Error", f"Error: {e}")
    else:
        QMessageBox.critical(None, "Error", "Cannot create the database connection.")

def show():
    connection = get_connection()
    if connection is not None:
        QMessageBox.information(None, "Data", "Connection established.")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM persona;")
        rows = cursor.fetchall()
        for row in rows:
            QMessageBox.information(None, "Data", f"Name: {row[1]}\nSurname: {row[2]}\nSex: {row[3]}")
        connection.close()
    else:
        QMessageBox.critical(None, "Error", "Cannot create the database connection.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario Persona")
        self.setGeometry(100, 100, 600, 400)

        self.panel = QWidget()
        self.layoutGrid = QGridLayout()

        # Name
        self.lblName = QLabel("Name: ")
        self.txtName = QLineEdit()
        self.layoutGrid.addWidget(self.lblName, 0, 0)
        self.layoutGrid.addWidget(self.txtName, 0, 1)

        # Surname
        self.lblSurname = QLabel("Surname: ")
        self.txtSurname = QLineEdit()
        self.layoutGrid.addWidget(self.lblSurname, 1, 0)
        self.layoutGrid.addWidget(self.txtSurname, 1, 1)

        # Date
        self.lblDate = QLabel("Date: ")
        self.txtDate = QLineEdit()
        self.txtDate.setReadOnly(True)
        self.txtDate.setAlignment(Qt.AlignCenter)
        self.layoutGrid.addWidget(self.lblDate, 3, 0)
        self.layoutGrid.addWidget(self.txtDate, 3, 1)

        # Calendar
        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.clicked[QDate].connect(self.mostrarFechaSeleccionada)
        self.layoutGrid.addWidget(self.calendario, 4, 1)

        # Sex
        self.cboSex = QComboBox()
        self.cboSex.addItem("Select")
        self.cboSex.addItem("Homme")
        self.cboSex.addItem("Femme")
        self.layoutGrid.addWidget(self.cboSex, 2, 1)

        # Send Button
        self.btnSend = QPushButton("Send")
        self.btnSend.clicked.connect(self.get_data)
        self.layoutGrid.addWidget(self.btnSend, 5, 1)

        # Show Button
        self.btnShow = QPushButton("Show")
        self.btnShow.clicked.connect(show)
        self.layoutGrid.addWidget(self.btnShow, 6, 1)

        self.panel.setLayout(self.layoutGrid)
        self.setCentralWidget(self.panel)

    def mostrarFechaSeleccionada(self, fecha):
        """Muestra la fecha seleccionada en txtDate."""
        self.txtDate.setText(fecha.toString("yyyy/MM/dd"))

    def get_data(self):
        name = self.txtName.text()
        surname = self.txtSurname.text()
        sex = self.cboSex.currentText()
        flag = False
        if sex == "Select":
            QMessageBox.critical(None, "Error", "Select a sex")
        elif sex == "Homme":
            sex = "H"
            flag = True
        else:
            sex = "F"
            flag = True

        if flag:
            insert(name, surname, sex)
            QMessageBox.information(None, "Data", f"Name: {name}\nSurname: {surname}\nSex: {sex}")

# Ejecutar aplicación
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
