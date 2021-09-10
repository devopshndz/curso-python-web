# Las funciones son bloques de codigo que no se van a ejecutar a menos que nosotros llamemos a estas. 
# Se utilizan tambien para reutilizar codigos que nostros ya hemso escrito para que no tengamos que 
# escribir nuevamente codigo.

# definir una funcion: def
def miFuncion():
    # Aquí va el códogo de la función, lo que queramos que ejecute la función.
    print('Mi primera funcion')

# llamamos la funcion para que la ejecute:
miFuncion()
miFuncion()
miFuncion()
# Para tener en cuenta, a veces las funciones son llamadas dentro de print()
print()

# las funciones pueden recibir argumentos. Estos son variables que podemos utilizar dentro de las 
# funciones para que estas sean flexibles dependiendo de nuestras necesidades.

def imprimeDato(argumentoUno): # le estamos pasando argumento dentro de los ()
    print('mi argumento es', argumentoUno)

imprimeDato('parametro 1') 

# cuando le damos valor al argumento inicializado previamente, se llama parametro
# esto hace referencia a que el texto 'parametro 1' es el valor correspondiente al argumento argumentoUno

# cuando llamamos una funcion y le pasamos un valor a los () este valor se llama parametro.
# cuando nosotros hacemos referencia a ese valor dentro de la funcion, se llama argumento.
print()

def miOtraFuncion(nombre, apellido): # <-- lo de adentro se llama argumento
    print('El nombre completo es:',nombre,apellido)

miOtraFuncion('Alberto', 'Hernandez') # <-- estos son los parametros de los argumentos
print()

# pasar a nuestras funciones una cantidad variable de argumentos.

def funcion2(*nombre): # al colocar el simbolo reservado de * como argumento en la funcion 
                        # estamos haciendo que los datos que nosotros le pasamos a la 
                        # funcion sean variables, en este caso nos entregará el dato de nombre como 
                        # si este fuese una lista que en realidad sería una tupla.
    print('El nombre completo es',nombre)
    print('El nombre completo es',nombre[2]) # si queremos ver un elemento de la tupla colocamos [posicion]
    # se pueden utilizar las funciones de for para poder ver los elementos
    for x in nombre:
        print(x)

funcion2('beto', 'grecia', 'te amo', 'con mi vida', 'al', 1000)

print()
# pasar los nombre de los argumentos cuando le vayamos a pasar los parametros:
def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

nombreCompleto(nombre='Chanchito', apellido='Feliz')
# otra sintaxis:
def nombreCompleto2(**kwargs): # Agrupar como si estos fueran un diccionario.
    print(kwargs['nombre'], kwargs['apellido']) # sintaxis de diccionarios
nombreCompleto2(nombre='maria',apellido='gutierrez')

# con **kewargs creamos una funcion de diccionario.
# colocamos la palabra reservada kwargs seguido de la sintaxis de diccionario ['']
# llamamos la funcion y necesariamente debemos pasar los argumentos seguidos de = y los parametros.


# al colocar el * estamos diciendo que el argumento nombre va a ser una tupla de elementos ya que 
# no se puede modificar, al pasarle como parámetros tantos elementos como queramos, estos se 
# guardarán en dicha lista y se imprimiran.

print()
def suma():
    n1 = int(input("Digita un numero: "))
    n2 = int(input("Digita un numero: "))
    sum = n1 + n2
    print(sum)
    
def resta():
    n1 = input("Digita un numero: ")
    n2 = int(input("Digita un numero: "))
    res = n1 - n2
    print(res)

def multi():
    n1 = int(input("Digita un numero: "))
    n2 = int(input("Digita un numero: "))
    multi = n1 * n2
    print(multi)

def divi():
    n1 = int(input("Digita un numero: "))
    n2 = int(input("Digita un numero: "))
    div = n1 / n2
    print(div)


print("""Escoge 1:
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. salir""")
dato=input("Digita la opción:")
while dato < "1" or dato >= "6":
    print("Opcion invalida, vuelve a digitar: ")
    print("""Escoge 1:
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. salir""")
    dato=input("Digita la opción:")
else:
    if dato == "1":
        suma()
    elif dato == "2":
        resta()
    elif dato == "3":
        multi()
    elif dato == "4":
        divi()
    elif dato == 5:
        print("Programa terminado.")
        exit



