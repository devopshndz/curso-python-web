use prueba;

# actualizar campos: update tabla set....
update Usuario set edad = 23 where id = 2;
# la condicion de where siempre debe ir, de lo contrario al actualizar un campo se actualizarian todos
select * from Usuario;