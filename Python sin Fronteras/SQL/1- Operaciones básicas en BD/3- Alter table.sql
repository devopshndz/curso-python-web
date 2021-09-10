use prueba;
# si al momento de crear la tabla o se colocó mal un dato se puede editar con alter table

# agg campo: add
 alter table Usuario add edad int; # add es para agg una columna o dato
# eliminar campo: drop column
 alter table Usuario drop column edad; # con drop column se elimina campo
# modificar tabla: modify column 
 alter table Usuario modify column email varchar(50); # con modify column se modifica el valor de un campo
 # eliminar un campo en especifico con delete, se coloca limit 1 porque es el primer registro y no posee llave primaria
 delete from Usuario where email = 'alberto@gmail.com' limit 1;
# agg llave primaria con alter table
alter table Usuario add primary key (id);

alter table Usuario modify column id int auto_increment;