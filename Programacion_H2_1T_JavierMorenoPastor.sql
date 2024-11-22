create database hito2Python;
use hito2Python;

create table registros (
    nombre varchar(30),
    telefono int unique,
    correo varchar(30) unique,
    id int primary key unique
);
	
create table productos (
    producto varchar(30) primary key
);

create table comprar (
    id_compra int primary key unique,
    id int,
    productos varchar(30),
    foreign key (id) references registros(id),
    foreign key (productos) references productos(producto)
);

	