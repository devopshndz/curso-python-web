# Los rangos nos permiten tener un numero de elementos desde un numero inicial hasta un numero 
# final que nosotros le vamos a tener que dar.

# Creamos una variable rango con el metodo range()
rango = range(5)
print(rango)

# Se nos muestra que el rango con el que vamos a trabajar será desde 0 a 5
# Este tipo de datos nos será util cuando utilicemos las iteraciones.
# Forma de ingresar un conjunto de datos dados por el usuario a una lista usando range
x = []
for i in range(int(input("Digita la cantidad de numeros a ingresar: "))):
    x.append(input('Ingresa un dato: '))
print('Los datos ingresados son: ',x)
