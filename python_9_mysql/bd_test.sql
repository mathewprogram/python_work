-- 1. ELIMINAR LA BASE DATOS SI EXISTE

DROP DATABASE IF EXISTS TEST0001;

-- 2. CREAR LA BASE DE DATOS SI NO EXISTE

CREATE DATABASE IF NOT EXISTS TEST0001;

-- 3. SELECCIONARA LA BASE DE DATOS A USAR

USE TEST0001;

-- 4. CREAR LA TABLA SI NO EXISTE

CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente        INT           AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nombre            VARCHAR(50)   NOT NULL,
    edad              INT           NOT NULL,
    ingresos          DECIMAL(10,2) NOT NULL,
    historial_compras INT           NOT NULL 
);

-- 5. MOSTRAR LA ESTRUCTURA DE LA TABLA

DESCRIBE Cliente; 

-- 5. INSERTAR REGISTROS EN LA TABLA

INSERT INTO Cliente VALUES
(1, 'Juan Díaz', 25, 50000, 3),
(2, 'María Alonso', 30, 75000, 5),
(3, 'Pedro Pique', 22, 40000, 2),
(4, 'Ana de Armas', 35, 90000, 7),
(5, 'Luis Armstrong', 28, 60000, 2),
(6, 'Juan Perez', 25, 60000, 1),
(7, 'Patricia Gooday', 25, 90000, 7),
(8, 'Ismael Sarraguro', 28, 75000, 2),
(9, 'María Cruz', 30, 40000, 2),
(10, 'Liz Beth', 30, 50000, 5);

-- 6. MOSTRAR TODOS LOS REGISTROS

SELECT * FROM Cliente;

-- 7. APUNTES

-- historial_compras: Indica la frecuencia o cantidad de compras que un cliente ha realizado