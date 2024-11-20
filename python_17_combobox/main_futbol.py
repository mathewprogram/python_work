import sys, os, sqlite3
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QComboBox, QLabel, 
    QWidget, QPushButton, QLineEdit, QVBoxLayout,
    QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
    )
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from herencia_seleccionfutbol import SeleccionFutbol, Entrenador, Masajista, Futbolista
 

def get_connection():
    nra = (
    "/Users/mihaitamatei/Documents/personal/Projects/"
    "python/python_work_in_class/python_16_stack_tablas/"
    "seleccionfutbol.sqlite3"
        )

    connection = None
    try:
        connection = sqlite3.connect(nra)
    except sqlite3.Error as e:
        connection = None
    return connection

def cargar_combobox():
    connection = get_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT id_seleccionfutbol FROM SeleccionFutbol"
            cursor.execute(query)
            idseleccionfutbol_lt = cursor.fetchall()
            cboIdSeleccionFutbol.addItem("Seleccione ID")
            for idseleccionfutbol_t in idseleccionfutbol_lt:
                id_seleccionfutbol, = idseleccionfutbol_t
                cboIdSeleccionFutbol.addItem(str(id_seleccionfutbol))

        except sqlite3.Error as e:
            QMessageBox.critical(None, "Error", f"Error: {e}")
    else:
        QMessageBox.critical(None, "Error", "No se pudo establecer la Conexion")

def cambiar_item():
    idSeleccionFutbol = cboIdSeleccionFutbol.currentText()
    if idSeleccionFutbol == "Seleccione ID":
        reiniciar()
        #lblInformacion.setText("Informacion miembro seleccion futbol.")
        return
        
    seleccionfutbol_lo = obtener_lista_seleccionfutbol_objeto()
    
    for objeto in seleccionfutbol_lo:
        if objeto.id_seleccionfutbol == idSeleccionFutbol:
            # Obtener información común
            nombre = objeto.nombre
            apellidos = objeto.apellidos
            edad = objeto.edad
            
            if isinstance(objeto, Futbolista):
                dorsal = objeto.dorsal
                demarcacion = objeto.demarcacion
                # Construir y mostrar información del futbolista
                #lblInformacion.setText(f"Futbolista: {nombre} {apellidos}, Edad: {edad}\nDorsal: {dorsal}, Demarcación: {demarcacion}")
                                       
                construir_tabla(["Id","Nombre", "Apellidos", "Edad", "Dorsal", "Demarcación", "Rol"],7,objeto)
            if isinstance(objeto, Entrenador):
                id_federacion = objeto.id_federacion
                # Construir y mostrar información del entrenador
                #lblInformacion.setText(f"Entrenador: {nombre} {apellidos}, Edad: {edad}\nID Federación: {id_federacion}")
                construir_tabla(["Id","Nombre", "Apellidos", "Edad", "Id Federación","Rol"],6,objeto)
            if isinstance(objeto, Masajista):
                titulacion = objeto.titulacion
                anio_experiencia = objeto.anio_experiencia
                # Construir y mostrar información del masajista
                #lblInformacion.setText(f"Masajista: {nombre} {apellidos}, Edad: {edad}\nTitulación: {titulacion}, Años de experiencia: {anio_experiencia}")
                construir_tabla(["Id","Nombre", "Apellidos", "Edad", "Titulación", "Años de experiencia","Rol"],7,objeto)
            

def obtener_lista_seleccionfutbol_objeto():
    seleccionfutbol_lo = []
    connection = get_connection()
    if connection != None:
       cursor = connection.cursor()
       try:
          query_seleccionfutbol = "SELECT * FROM SeleccionFutbol" 
          cursor.execute(query_seleccionfutbol)
          seleccionfutbol_lt = cursor.fetchall()
          for seleccionfutbol_t in seleccionfutbol_lt:
              id_seleccionfutbol, nombre, apellidos, edad = seleccionfutbol_t

              cursor.execute('SELECT * FROM Futbolista WHERE id_futbolista = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_futbolista, dorsal, demarcacion = resultado_t
                 seleccionfutbol_o = Futbolista(id_futbolista, nombre, apellidos, edad, dorsal, demarcacion)
                 seleccionfutbol_lo.append(seleccionfutbol_o)

              cursor.execute('SELECT * FROM Entrenador WHERE id_entrenador = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_entrenador, id_federacion = resultado_t
                 seleccionfutbol_o = Entrenador(id_entrenador, nombre, apellidos, edad, id_federacion)
                 seleccionfutbol_lo.append(seleccionfutbol_o)

              cursor.execute('SELECT * FROM Masajista WHERE id_masajista = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_masajista, titulacion, anio_experiencia = resultado_t
                 seleccionfutbol_o = Masajista(id_masajista, nombre, apellidos, edad, titulacion, anio_experiencia)
                 seleccionfutbol_lo.append(seleccionfutbol_o)
          #print("OK: LISTA SELECCION FUTBOL")
          return seleccionfutbol_lo             
       except Exception as e:
          print("ERROR: SELECT ", e)
          return None
    else:
        print("ERROR: CONEXION")

def construir_tabla(cabecera,n,objeto):
        #tblMostrar = QTableWidget()
        tblMostrar.setColumnCount(n)
        tblMostrar.setRowCount(0)
        tblMostrar.setHorizontalHeaderLabels(cabecera)
        tblMostrar.horizontalHeader().setStyleSheet("color: black; background-color: white;")
        tblMostrar.verticalHeader().setStyleSheet("color: black; background-color: white;")
        tblMostrar.horizontalHeader().setFont(QFont("Courier New", 14, QFont.Bold)) 
        tblMostrar.insertRow(0)
        tblMostrar.setItem(0, 0, QTableWidgetItem(objeto.id_seleccionfutbol))
        tblMostrar.setItem(0, 1, QTableWidgetItem(objeto.nombre))
        tblMostrar.setItem(0, 2, QTableWidgetItem(objeto.apellidos))
        tblMostrar.setItem(0, 3, QTableWidgetItem(str(objeto.edad)))
        if isinstance(objeto, Futbolista):
            tblMostrar.setItem(0, 4, QTableWidgetItem(str(objeto.dorsal)))
            tblMostrar.setItem(0, 5, QTableWidgetItem(objeto.demarcacion))
            tblMostrar.setItem(0, 6, QTableWidgetItem(objeto.__class__.__name__))
        if isinstance(objeto, Entrenador):
            tblMostrar.setItem(0, 4, QTableWidgetItem(str(objeto.id_federacion)))
            tblMostrar.setItem(0, 5, QTableWidgetItem(objeto.__class__.__name__))
        if isinstance(objeto, Masajista):
            tblMostrar.setItem(0, 4, QTableWidgetItem(objeto.titulacion))
            tblMostrar.setItem(0, 5, QTableWidgetItem(str(objeto.anio_experiencia)))
            tblMostrar.setItem(0, 6, QTableWidgetItem(objeto.__class__.__name__))
        return tblMostrar

def item_seleccionado():
    """Handle the selected item from the combo box."""
    id_seleccion = cboIdSeleccionFutbol.currentText()
    connection = get_connection()
    
    if connection:
        try:
            cursor = connection.cursor()
            
            # Determinar el tipo del registro
            tipo_query = """
            SELECT 'Futbolista' AS tipo FROM Futbolista WHERE id_futbolista = ?
            UNION
            SELECT 'Masajista' AS tipo FROM Masajista WHERE id_masajista = ?
            UNION
            SELECT 'Entrenador' AS tipo FROM Entrenador WHERE id_entrenador = ?
            """
            cursor.execute(tipo_query, (id_seleccion, id_seleccion, id_seleccion))
            tipo_result = cursor.fetchone()
            
            if tipo_result:
                tipo = tipo_result[0]  # Recuperamos el tipo de registro

                # Obtener información común de la tabla SeleccionFutbol
                seleccion_query = """
                SELECT nombre, apellidos, edad
                FROM SeleccionFutbol
                WHERE id_seleccionfutbol = ?
                """
                cursor.execute(seleccion_query, (id_seleccion,))
                seleccion_info = cursor.fetchone()

                if seleccion_info:
                    nombre, apellidos, edad = seleccion_info

                    # Obtener información específica según el tipo
                    if tipo == "Futbolista":
                        futbolista_query = """
                        SELECT dorsal, demarcacion
                        FROM Futbolista
                        WHERE id_futbolista = ?
                        """
                        cursor.execute(futbolista_query, (id_seleccion,))
                        futbolista_info = cursor.fetchone()

                        if futbolista_info:
                            dorsal, demarcacion = futbolista_info
                            lblInformacion.setText(
                                f"Tipo: Futbolista\n"
                                f"Nombre: {nombre} {apellidos}, Edad: {edad}\n"
                                f"Dorsal: {dorsal}, Demarcación: {demarcacion}"
                            )
                    elif tipo == "Masajista":
                        masajista_query = """
                        SELECT titulacion, anio_experiencia
                        FROM Masajista
                        WHERE id_masajista = ?
                        """
                        cursor.execute(masajista_query, (id_seleccion,))
                        masajista_info = cursor.fetchone()

                        if masajista_info:
                            titulacion, anio_experiencia = masajista_info
                            lblInformacion.setText(
                                f"Rol: Masajista\n"
                                f"Nombre: {nombre} {apellidos}, Edad: {edad}\n"
                                f"Titulación: {titulacion}, Años de experiencia: {anio_experiencia}"
                            )
                    elif tipo == "Entrenador":
                        entrenador_query = """
                        SELECT id_federacion
                        FROM Entrenador
                        WHERE id_entrenador = ?
                        """
                        cursor.execute(entrenador_query, (id_seleccion,))
                        entrenador_info = cursor.fetchone()

                        if entrenador_info:
                            id_federacion = entrenador_info[0]
                            lblInformacion.setText(
                                f"Tipo: Entrenador\n"
                                f"Nombre: {nombre} {apellidos}, Edad: {edad}\n"
                                f"ID Federación: {id_federacion}"
                            )
                else:
                    lblInformacion.setText("No se encontró información básica.")
            else:
                # Si no se encuentra el id en Futbolista, Masajista ni Entrenador, solo mostramos info de SeleccionFutbol
                seleccion_query = """
                SELECT nombre, apellidos, edad
                FROM SeleccionFutbol
                WHERE id_seleccionfutbol = ?
                """
                cursor.execute(seleccion_query, (id_seleccion,))
                seleccion_info = cursor.fetchone()

                if seleccion_info:
                    nombre, apellidos, edad = seleccion_info
                    lblInformacion.setText(
                        f"Nombre: {nombre} {apellidos}, Edad: {edad}\n"
                        f"No tiene una categoría asignada."
                    )
                else:
                    lblInformacion.setText("No se encontró información.")
        except sqlite3.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error retrieving data: {e}")
        finally:
            connection.close()

def reiniciar():
    #lblInformacion.setText("Informacion miembro seleccion futbol.")
    tblMostrar.setRowCount(0)
    tblMostrar.setColumnCount(0)
    cboIdSeleccionFutbol.setCurrentIndex(0)


# 0. CONSTRUIR UNA APLICACION
app = QApplication(sys.argv) #<------------

# 1. CREAR LA VENTANA PRINCIPAL
ventana_principal = QMainWindow()
ventana_principal.setWindowTitle("Selección de Fútbol")
ventana_principal.resize(500, 150)


# 2. CREAR UN PANEL QWIDGET
panel_principal = QWidget()

# 3. CREAR UN ADMINISTRADOR(LAYOUT) DEL PANEL
layout_principal = QVBoxLayout()

# 4. Creamos componentes y añadimos administrador principal

#lblInformacion = QLabel("Informacion miembro seleccion futbol.")
#lblInformacion.setFont(QFont("Courier New", 14, QFont.Bold))
tblMostrar = QTableWidget()



cboIdSeleccionFutbol = QComboBox()
cboIdSeleccionFutbol.setFont(QFont("Courier New", 14, QFont.Bold))
cboIdSeleccionFutbol.currentIndexChanged.connect(cambiar_item)
#cboIdSeleccionFutbol.currentIndexChanged.connect(item_seleccionado)

btnReiniciar = QPushButton("Reiniciar")
btnReiniciar.setFont(QFont("Courier New", 14, QFont.Bold))
btnReiniciar.clicked.connect(reiniciar)

btnSalir = QPushButton("Salir")
btnSalir.setFont(QFont("Courier New", 14, QFont.Bold))
btnSalir.clicked.connect(sys.exit)

layout_botones = QHBoxLayout()
layout_botones.addWidget(btnReiniciar)
layout_botones.addWidget(btnSalir)

#layout_principal.addWidget(lblInformacion)
layout_principal.addWidget(tblMostrar)
layout_principal.addWidget(cboIdSeleccionFutbol)
layout_principal.addLayout(layout_botones)

cargar_combobox()


# 5. ASIGNAR EL ADMINISTRADOR AL PANEL
panel_principal.setLayout(layout_principal)

# 6. PONER EL PANEL A LA VENTANA PRINCIPAL
ventana_principal.setCentralWidget(panel_principal)

# 7. MOSTRAR VENTANA PRINCIPAL
ventana_principal.show()

# 8. EJECUTAR APLICACION
sys.exit(app.exec())        #<------------


