# condicional if: de las mas basicas y nos permitirá tomar decisiones en nuestro código.
if 2 < 5:
    print('2 es menor que 5')

# Evaluar si 2 variables son iguales:
# 2 == 2: igualdad
# 2 < 3: una variables es menor a otra
# 2 > 3: una variables es mayor a otra
# 2 != 3: una variable es diferente a la otra
# 2 <= 3: menor o igual
# 2 >= 3: mayor o igual

if 2 == 2:
    print('2 es igual a 2')

if 2 == 3:
    print('2 es iguala 3')

if 2 > 5:
    print('2 es mayor que 5')

if 5 > 2:
    print('5 es mayor a 2')

if 2 != 2:
    print('2 es distinto a 2')

if 3 != 2:
    print('3 es distinto a 2')

if 2 <= 3:
    print('2 es menor o igual a 3')

if 3 >= 2:
    print('3 es mayor o igual a 2')

print()

# else y elif

# elif lo que hace es que si la primera condición retorna una valor False, va a pasar a la siguiente 
# linea y realizará otra evaluación automáticamente.
# se utiliza cuando la primera condicion no se cumple.
if 2 > 3:
    print("2 es mayor a 3 em if")
elif 2 < 1:
    print("2 es menor a 3 en elif")
elif 2 < 3:
    print("2 es menor a 3 en segundo elif")
# aca se ve como se pueden ir encadenando elif, esto se da si la primera instruccion de elif 
# evalua en falso, se coloca otra instruccion elif si así lo requiere y se sigue evaluando.
else:
    print("Yo me imprimo si todo lo anterior se evalúa en falso")
# else lo que hace es que en el caso de que todas las condiciones que anteriormente fueron efectuadas 
# tanto en if como elif, y fueron False, else ejecuta la instrucción que está dentro de ella.
# else es como elif, simplemente que por estética y estandar se utiliza mas que todo para dar 
# finalizacion a un ciclo if.
print()
if "Beto" == "Grecia":
    print("es igual")
else:
    print("Yo me imprimo solo si todo lo anterior es falso")
# else lo vamos a utilizar como si fuera un aviso de finalizacion mientras que elif lo utilizamos 
# para evaluar mas condiciones