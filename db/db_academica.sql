CREATE DATABASE IF NOT EXISTS db_academica;
USE db_academica;

CREATE TABLE usuarios (
    idUsuario INT(10) AUTO_INCREMENT PRIMARY KEY,
    usuario CHAR(35),
    clave CHAR(35),
    nombre CHAR(85),
    direccion CHAR(100),
    telefono CHAR(9)
);
