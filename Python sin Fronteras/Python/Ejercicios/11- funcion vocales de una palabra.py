# Escribir una funcion que indique cuantas vocales tiene una palabra o un string

palabra = input('introduce la palabra: ')
vocales = 0

for x in palabra:
    y = x.lower() # este metodo hace que el valor que tiene x si es MAYUSCULA pase a minusucula, 
                    # para que a la hora de comparar tambien se tengan en cuenta valores en mayusuculas.
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
    # vocales irá aumentando en uno si y es igual a a,e,i,o,u y sino, será 0 (el else del final 
    # es por si no hay vocales en el string)
print('hay ', vocales , ' vocales en la palabra o string')

# lower() toma que la variable que la esté llamando vuelva sus letras que estan en mayusculas 
# a minusculas
