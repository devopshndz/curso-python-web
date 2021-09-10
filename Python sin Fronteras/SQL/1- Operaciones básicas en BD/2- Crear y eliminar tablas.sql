use prueba; # sintaxis para escoger una bd y usarla
create table Usuario( # sintaxis para crear una tabla, siempre se abre parentesis y dentro de el se escribe todo
id int, email varchar(255), username varchar(50));
# hay distintos tipos de datos, int para indicar numeros enteros, float para num decimales, varchar para cadena 
# de textos, bool para num boleanos.
# para ver la informacion de la tabla, nos vamos a la bd y le damos a Tables/clic derecho sobre la tabla a ver/
# select rows o table inspector

# drop table Usuario; comando para eliminar una tabla