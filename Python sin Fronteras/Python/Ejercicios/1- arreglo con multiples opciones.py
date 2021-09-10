# Crear un areglo que contenga una lista de opciones.
# Será una lista que contenga multiples opciones, intentaremos adivinar que se 
# encuentra dentro de la lista

# 1. pedimos ingresar un dato por teclado, este dato será string
dato = input("Ingrese el dato: ")

# 2. creamos una lista con varios datos dentro de esta
lista = ['Hola', 'Mundo', 'Chanchito', 'Feliz', 'dragones']

# 3. en un ciclo if hacemos un conteo de todos los datos que están dentro de 
# la lista pasando el dato que ingresamos para saber si este está dentro, 
# si no está significa que el dato no es mayor a 0 y no se cumple la condicion. 
# Pero si está, se efectua la condicion y se imprime el dato.
if lista.count(dato) > 0:
    print('El dato existe, y es:', dato)
else:
    print('El dato no existe')

# 1. pedimos ingresar un dato por teclado, este dato será string

# 2. creamos una lista con varios datos dentro de esta

# 3. en un ciclo if hacemos un conteo de todos los datos que están dentro de 
# la lista pasando el dato que ingresamos para saber si este está dentro, 
# si no está significa que el dato no es mayor a 0 y no se cumple la condicion. 
# Pero si está, se efectua la condicion y se imprime el dato.