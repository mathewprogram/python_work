import mysql.connector


def get_connection():
        connection = mysql.connector.connect(
            host="localhost",
            port = 3306,
            user="root",
            password="Passw0rd!",
            database="ferreteria"
        )
        return connection

def get_available_products():
    connection = get_connection()
    if connection != None:
       try:
          cursor = connection.cursor()
          query = "SELECT id_producto, nombre, precio, stock FROM Producto WHERE stock > 0"
          cursor.execute(query)
          productos_lt = cursor.fetchall()
          productos_disponibles_d = {}
          productos_disponibles_d = {f"{p[0]} - {p[1]}": p for p in productos_lt}
          #print(productos_disponibles_d)
       except Exception as e:
          print("ERROR: QUERY SELECT", e)  
    else:
       print("ERROR: CONEXION") 
    return productos_disponibles_d




if __name__ == "__main__":
    get_available_products()