import mysql.connector # importar libreria mysql.connector para conectarse con la bd

midb = mysql.connector.connect( # se pasan los 4 argumentos host, user, password, database
    host='localhost',
    user='root',
    password='beto',
    database='prueba'
)

cursor = midb.cursor() # interaccion con bd

### descomentar cada punto para poder ver su funcionamiento, seguir lo que está escrito ###

#1. listar datos: descomentar
cursor.execute('select * from Usuario')
resultado = cursor.fetchall()
print(resultado)

#2. ver definiciones de tablas si no te acuerdas del modelo, comentas el 1. y ejecutar:
# cursor.execute('show create table Usuario')
# resultado = cursor.fetchall()
# print(resultado)

#3. Insertar datos: luego de ver las definiciones el punto 2. lo comentamos y descomentamos este 3er paso:
# sql = 'Insert into Usuario (email, username, edad) values (%s, %s, %s)' # los %s serán los valores a reemplazar, se deben escribir siempre
# values = ('betouuuu@gmail.com', 'beto', 28) # estos serán los valores que iran en cada %s
# cursor.execute(sql, values) # se pasan sql, values para ejecutar la consulta y colocar valores, SIEMPRE
# midb.commit() # sentencia para hacer que en la bd sean efectuados los cambios
# print(cursor.rowcount) # sentencia para ver el conteo de nuevos registros ingresados a la bd

#4. actualizar datos:
# sql = 'update Usuario set email = %s where id = %s' # los %s son conectores para los values
# values = ('DaniloV@gmail.com', 6)
# cursor.execute(sql, values) # se pasan sql, values para ejecutar la consulta y colocar valores, SIEMPRE
# midb.commit() # sentencia para hacer que en la bd sean efectuados los cambios