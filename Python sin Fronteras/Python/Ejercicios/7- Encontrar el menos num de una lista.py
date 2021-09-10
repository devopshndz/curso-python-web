# Intentar encontrar el menor numero de una lista.
lista = [3,4,2,5,6,-54,-13]
# debemos hacer comparaciones para esto con 2 ciclos for:
menor = 'init'
for x in lista:
    if menor == 'init': # si menor es igual a 'init'
        menor = x # la posicion x será asignada a menor
    elif x < menor: # si x < a menor:
        menor = x # la posicion de x se le asigna a menor
    # otra forma abreviada
    #else:
    #    menor = x if x < menor else menor
print('menor',menor)