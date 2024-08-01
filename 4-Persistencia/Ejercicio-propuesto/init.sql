-- Crear la base de datos y el usuario
CREATE DATABASE IF NOT EXISTS paisesdb;
CREATE USER IF NOT EXISTS 'pepito'@'%' IDENTIFIED BY 'pepe1234';
GRANT ALL PRIVILEGES ON paisesdb.* TO 'pepito'@'%';
FLUSH PRIVILEGES;

-- Seleccionar la base de datos
USE paisesdb;

-- Crear las tablas
CREATE TABLE IF NOT EXISTS CONTINENTES (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS PAISES (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    id_continente INT,
    FOREIGN KEY (id_continente) REFERENCES CONTINENTES(id)
);

-- Insertar datos iniciales
INSERT INTO CONTINENTES (id, nombre) VALUES (1, 'Europa');
INSERT INTO PAISES (id, nombre, id_continente) VALUES (1, 'España', 1);
