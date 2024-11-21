CREATE TABLE Usuario (
    id_usuario  INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario      TEXT NOT NULL UNIQUE,
    contrasena          TEXT NOT NULL,
    rol                 TEXT NOT NULL CHECK (rol IN ('Admin', 'Cajero', 'Almacen'))
);

CREATE TABLE Venta (
    id_venta    INTEGER PRIMARY KEY AUTOINCREMENT,
    producto    TEXT NOT NULL,
    fecha_venta TEXT NOT NULL,
    total       REAL NOT NULL
);

CREATE TABLE Producto (
    id_producto  INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_producto     TEXT NOT NULL,
    precio              REAL NOT NULL,
    stock               INTEGER NOT NULL
);

