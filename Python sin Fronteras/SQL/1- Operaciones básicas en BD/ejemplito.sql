create database Ejemplo;

use Ejemplo;

create table Usuario(
    id int primary key auto_increment,
    nombre varchar(50),
    apellido varchar(50),
    edad INT,
    correo VARCHAR(100)
);

INSERT INTO Usuario (nombre, apellido, edad, correo) VALUES ('Alberto', 'Hernandez', 27, 'betito@gmail.com');
INSERT INTO Usuario (nombre, apellido, edad, correo) VALUES ('Grecia', 'Rocha', 22, 'gress@gmail.com');
INSERT INTO Usuario (nombre, apellido, edad, correo) VALUES ('Maria', 'Gutierrez', 61, 'maria@gmail.com');

update Usuario set direccion = 'carrera 11 # 14-40' where id = 1;
update Usuario set direccion = 'acienda piedras negras' where id = 2;
update Usuario set direccion = 'carrera 11 # 14-40' where id = 3;