# Construir una pequeña calculadora que sume con input()

primero = input("Ingrese el primer numero: ")
segundo = input("Ingrese el segundo numero: ")
# Python reconoce que al utilizar input() los valores dentro de él son string, debemos pasarlos a int 
# de lo contrario lo que arrojará sera una concatenación y no una suma

primerNumero = int(primero)
segundoNumero = int(segundo)

# Aquí ya pasamos los datos a valor entero y ya puede hacerse la suma.
suma = primerNumero + segundoNumero
print("La sumatoria de la suma es: ", suma)
print()
# Otra forma de hacerlo y de ahorrar codigo es antes de input declarar que tipo de dato va a entrar:
#primero = int(input('Primer numero: '))
#segundo = int(input('Segundo numero: '))
#print('Resultado: ',primero + segundo)

primero1 = input("Ingrese el primer numero: ")

# Ahora, vamos a colocar una validación para que si por error no ingresa ningun dato numerico no se 
# dañe el programa, para ello utilizamos la funcion try: la cual nos permite realizar validaciones.

# En este caso vamos a intentar pasar un valor string que coloquemos a entero, si esto no se puede, 
# ese valor tendra el valor de 'chanchito feliz'
try:
    primero1 = int(primero1)
    # ojo: aca se hace la validación, si el valor ingresado es un numero, se queda como está y todo ok
except:
    primero1 = 'chanchito feliz'
    # pero si el valor ingresado no es un numero, la variable toma por valor 'chanchito feliz' que es un
    # string, puede ser cualquier string que coloquemos, en este caso es 'chanchito feliz'
    # ojito a esto porque ya ahora el valor que hayamos ingresado no entero, tiene el valor de 
    # 'chanchito feliz'


segundo2 = input("Ingrese el segundo numero: ")
try:
    segundo2 = int(segundo2)
except:
    segundo2 = 'chanchito feliz'

# atencion: se crea un if para validar la validación de arriba, si la primera o la segunda variable 
# tiene en su valor 'chanchito feliz' (porque recordemos que si ingresamos un valor no numerico la 
# variable en donde la ingresamos automaticamente toma el valor de 'chanchito feliz') nos da el 
# aviso de que no estamos ingresando un valor numerico y debemos volver a ingresarlo.
if primero1 == 'chanchito feliz' or segundo2 == 'chanchito feliz':
    print('Ingresaste mal un dato, prueba de nuevo con un numero.')
    # si por el contrario los 2 datos ingresados son enteros se omite el if y se va de una al else 
    # y se efectúa la sumatoria. 
else:
    print(primero1 + segundo2)