-- 1. CREAR UNA TABLA
DROP TABLE IF EXISTS Persona;

CREATE TABLE Persona (
    
  id_persona        INTEGER    NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre            TEXT(50)   NOT NULL,
  apellido          TEXT(50)   NOT NULL,
  fecha_nacimiento  TEXT(10)   NOT NULL,
  sexo              CHAR(1)    NOT NULL
);  

-- 2. INSERTAR DATOS EN LA TABLA
INSERT INTO Persona (nombre, apellido, fecha_nacimiento, sexo) VALUES ('Mihai', 'Matei', '17/01/1991', 'H');

-- 5. Mostrar los datos de la tabla
SELECT * FROM Persona;