# Recursividad
# tenemos que escribir la logica que vamos a ejecutar y tambien debemos indicar una condicion de salida.
# con la recursividad lo que hacemos es crear una funcion la cual al final de esta se va a llamar a 
# si misma creando un ciclo hasta que esta pueda detenerse. 
def recursion(i):
    if i < 1:
        return i
    print(i)
    recursion(i-1)
recursion(6)

# en este ejemplo nosotros le pasaremos un numero aleatorio el cual va a ir decrementando hasta 1.
# cada que se llame a la funcion recrusion(i-1) este ira deisminuyendo hasta que se cumpla la 
# condicion de i < 1
print()
def recursion(i):
    if i > 10:
        return i
    print(i)
    recursion(i+1)
recursion(2)
# este ejemplo es el contrario del anterior, utilizaremos recursividad para hacer un incremento de 
# numeros hasta llegar a 10

# la recursividad sirve cuando nosotros queremos trabajar sobre una coleccion de datos o si queremos 
# hacer reintentos en un servidor o en una base de datos para llamarlos en caso de que estos fallen.
# si por ejemplo, si nos conectamos con una API y el primer llamado nos da un error, podemos crear 
# una funcion que lo que haga es intentar una maxima cantidad de 3 o 5 veces, si pasa de este numero 
# de intentos debemos lanzar un error en la aplicación. Si de lo contrario hay fallas pero antes de 
# los intentos establecidos funciona bien, prevenimos entregarle un mensaje de error al usuario.

# cuando queremos hacer un procesamiento en bach