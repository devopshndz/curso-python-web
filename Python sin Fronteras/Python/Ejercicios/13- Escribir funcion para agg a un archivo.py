# escrbir una funcion que reciba nombre y apellido y se vayan agg a un archivo.

def AggNomArchivo(nombre, apellido): # creamos función de agg nombre y apellido
    c = open('Python/Ejercicios/nombrecompleto.txt','a') # a una variable c le damos apertura y permisos 
    # escribimos la ruta donde va a crearse el archivo y le damos el permiso de a = append que será 
    # el responsable de ir agregando los nombres y apellidos al archivo.
    c.write(nombre + ' ' + apellido + '\n') # damos escritura y concatenamos nombre y apellido
    c.close() # cerramos el archivo

AggNomArchivo(input('Escriba el nombre: '),input('Escriba el apellido: '))
# agg nombre y apellido por teclado.