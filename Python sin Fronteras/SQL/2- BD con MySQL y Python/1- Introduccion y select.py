# python puede conectarse a mysql, para hacer esto se debe hacer es:
# 1 instalar pip3 install mysql-connector-python
# 2 se crea un archivo llamado db.py
# 3 dentro del archivo se importa la libreria: import mysql.connector
# 4 mysql.connector.connect

import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='beto',
    database='prueba'
)

cursor = midb.cursor()
cursor.execute('select * from Usuario')
resultado = cursor.fetchall()
print(resultado)
# el cursor es un objeto que nos permitirá interactuar con la base de datos mediante el lenguaje sql
# con el cursor se podrá llamar al metodo de execute() el cual podremos pasarle consultas con sql
# para devolver esa consulta como datos debemos declarar una variable en donde se guardara dicho resultado
# al objeto cursor se debe llamar el metodo fetchall(), lo cual traera TODOS los valores y lo imprimiremos con print como lista
