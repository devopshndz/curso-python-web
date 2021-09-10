# este archivo lo utilizaremos para poder manipuela el archivo de Chanchito.py

### leer archivos:


# utilizamos la funcion open() de python para abrir el archivo
# debemos colocar la ruta en donde se encuentra el archivo
c = open('7- Gestion de archivos/chancho.txt') 
print(c.read())
# el metodo read() es complemento de open() siempre se debe escribir cuando se use open()
# lo que hará read será leer todo el archivo
# hay que tener cuidado con .read() porque al utilizar archivos de textos muy extensos o que contengan 
# imagenes lo que hará es que arroje una infinidad de caracteres muy complicados de leer.

### ver permisos con los cuales podremos abrir los archivos en python
d = open('Python/7- Gestion de archivos/chancho.txt')
print(d.readline())
print(d.readline())
print(d.readline())

# 'r' permitirá tener el permiso de leer el archivo, este permiso viene por defecto.
# 'append' o 'a' abreviado, permitirá ir modificando el archivo pero lo modificado irá al final del 
# archivo (como en listas)
# 'write' o 'w' para modificar todo el archivo. Si el archivo no exite, python crea este archivo.
# 'x' permiso para crear un archivo, si el archvio ya se encuentra creado nos va a devolver un error 
# para leer solamente lineas una a una usamos readline()
# tambien se puede iterar con las lineas de los archivos directamente con la variable que contenga el 
# archivo en este caso d, se hace un ciclo for y se para la posición:
for x in d:
    print(x)
# arrojará una a una las lineas del archivo.
d.close()
# al terminar de leer un archivo es buenas practicas pasar el metodo .close() y cerrar el archivo.