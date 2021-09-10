# el for es un loop que se utiliza para iterar sobre listas o tuplas, pero generalmente sobre una 
# secuencia de datos incluso diccionarios.

usuarios = ['chanchito feliz', 'roberto', 'nicolas', 'pepe']

for usuario in usuarios: # sintaxis: for indicador in nombreLista:
# El indicador o iterador, será el que va a ir iterando en toda la lista, se define como una variable 
# la cual su funcion será ir recorriendo uno por uno toda la lista.
    print(usuario) # este print hará que se imprima el valor que se encuentra en la posición del 
                    # iterador, uno a uno, el iterador se posiciona en la 0 e imprime, luego sigue a 
                    # 1 e imprime y así hasta el ultimo valor.

# iterar stings:
print()
estudiantes = 'hola', 'mundo', 'grecia', 'beto'
for i in estudiantes:
    print(i)

print()
# iterar sobre un string
strin = 'hola mi amor'
for a in strin:
    print(a)
# esto lo que hará es que al tener un string solo, se iteren en sus caracteres y los imprima

print()
# utilizando el break en for
carros = ['audi', 'bmw', 'lambo', 'bochito']
for c in carros:
    if c == 'lambo':
        break
    print(c)
# cuando llegue la iteración a 'lambo' en el if se activará la condición lo que hará que 
# el break se active y termine el loop for.

print()
# utilizando continue en for
carros = ['audi', 'bmw', 'lambo', 'bochito']
for c in carros:
    if c == 'lambo':
        continue # continue, como en while, hace que vuelva al ciclo y se salte la condicion que 
                    # la activa, en este caso, cuando el iterador llegue a lambo no lo va a imprimir.
    print(c)

print()
# range en for loop
for x in range(6):
    print(x)
# lo que hace el range es establecer un rango numerico en el for, para este caso es 6 y se va a 
# imprimir dicho rango al iterarse.

# podemos manipular el range para decir desde que valor se va a establecer un rango:
print()
for x in range(2, 6): # inicia en 2 hasta 6
    print(x)
# recordemos que en las listas no es que va a contra 2, 3, 4, 5, 6, sino hasta 5, esto porque 
# python toma como la primera poscion 0, al escribir el valor 2, 6, estamos diciendo que la 
# iteracion iniciará en el valor 2 y terminará en la posción 6 = 0,1,2,3,4,5

print()
# manipulación del incremento de la iteracion: 3 valores (valorInicial, posicion hasta, incremento)
for x in range(2,20,4):
    print(x)
# decimos que inicie en el valor 2, hasta la posción 20 y se va a ir incrementando de 4 en 4, 
# terminará en 18 que es el valor que mas se aproxima a 20 sin excederlos
print()

# en los for loop podemos utilizar la palabra reservada else: la cual la utilizaremos cuando 
# nostros hayamos terminado de iterera dentro de un range o dentro de un ciclo simple.
for x in range(3,30,6):
    print(x)
else:
    print('Hemos terminado de iterar')

print()
# agregar a una lista valores desde el teclado e iterar
# 1era forma:
listica = [] # creamos una lista vacia.
for x in range(int(input('Digita cuantos elementos ingresaran a la lista: '))): 
    x = input("Digita un elemento: ")
    listica.append(x)
print(listica)
# establecemos desde teclado un rango, se debe pasar el valor en entero  para que sea valido 
# el numero de elementos que vamos a ingresar, luego de eso, ingresamos en el iterador x los 
# valores desde teclado para que al final a la listica le pasemos con la funcion append() los valores
# que ingresamos por teclado.
print()
# 2da forma:
listica = [] # creamos una lista vacia.
for x in range(int(input('Digita cuantos elementos ingresaran a la lista: '))):
    listica.append(input("Digita un elemento: "))
print(listica)
# esta es la forma simplificada de la anterior, lo que se hace es despues de establecer un rango por 
# teclado indicamos que listica se le agg esos valores de una con append.

print()
# for dentro de otro for: for anidados.
usuarios = ['chanchito feliz', 'roberto', 'nicolas', 'pepe']
edades = [24, 25, 26, 35]
# iteraremos los usuarios y dentro de esta iteracion sus edades:
for x in usuarios:
    for y in edades:
        print(x, y)
# nota: al imprimir estas 2 iteraciones una dentro de la otra, lo que se hara es que se toma 
# el primer valor que esté en la lista de usuarios y a este, se le va a iterar con los valores de la 
# segunda lista, cosa que se repetira en este ejemplo 4 veces cada usuario con las 4 edades.
print()

