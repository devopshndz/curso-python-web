create database user;
use user;

create table usuario(
    id int primary key auto_increment,
    nombre varchar(100) not null,
    apellido varchar(100) not null,
    edad int(3),
    correo varchar(100)
);

insert into usuario (nombre,apellido,edad,correo) values ('beto','hernandez',27,'betito@gmail.com');
insert into usuario (nombre,apellido,edad,correo) values ('grecia','rocha',22,'gres@gmail.com');
insert into usuario (nombre,apellido,edad,correo) values ('aisha','hernandez',5,'aisha@gmail.com');