# si lo que queremos es que se realice validacion de datos cuando estos se ingresen:
primero1 = input("Ingrese el primer numero: ")

try:
    primero1 = int(primero1)
except:
    primero1 = 'chanchito feliz'

if primero1 == 'chanchito feliz':
    print("El valor ingresado no es un entero.")
    exit()
# ya aquí estamos realizando la validación si es entero el valor ingresado en la primera variable.
segundo2 = input("Ingrese el segundo numero: ")
try:
    segundo2 = int(segundo2)
except:
    segundo2 = 'chanchito feliz'

if segundo2 == 'chanchito feliz':
    print("El valor ingresado no es un entero.")
    exit()

# Tomamos el simbolo por parte del usuario o la operacion:
simbolo = input('Ingrese operación: ')

if simbolo == '+':
    print('Suma:', primero1 + segundo2)
elif simbolo == '-':
    print('Resta: ', primero1 - segundo2)
elif simbolo == '*':
    print('Resta: ', primero1 * segundo2)
elif simbolo == '/':
    print('Resta: ', primero1 / segundo2)
else:
    print("El simbolo ingresado no es valido")
