import mysql.connector # importar libreria mysql.connector para conectarse con la bd

midb = mysql.connector.connect( # se pasan los 4 argumentos host, user, password, database
    host='localhost',
    user='root',
    password='beto',
    database='prueba'
)

cursor = midb.cursor() # interaccion con bd

cursor.execute('select * from Usuario') # generar consultas

# .fetchall() devolverá todas las instancias de los elementos que encontro en la bd y se los asignará a la var
# .fetchone() devolverá solamente el primer elemento que este ha encontrado:
resultado = cursor.fetchone() # traer los datos como lista y guardarlos en una variable
resultado2 = cursor.fetchone()


print(resultado) # imprimir el resultado almacenado en la variable
print(resultado2)
