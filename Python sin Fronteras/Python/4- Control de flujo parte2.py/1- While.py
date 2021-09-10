# Un loop de while es algo que se va a repetir hasta el infinito hasta que se cumpla una condición
# de salida
# Sitaxis: while (condcion):

i = 0
while i <= 5: # mientras que i sea menor o igual a 5:
    print(i)
    i += 1  # Version corta de i = i+1
    # esto hará que se le suma 1 a la variable de 1

print()
# break y continue
# break se usa para salir del bucle de manera abrupta por medio de una condicion:
b = 0
while b <= 5:
    print(b)
    if b == 3:
        break
    # Aqui utilizamos break para salir del ciclo antes de que llegue a 5, indicamos que cuando el 
    # valor de b sea 3, se genere el break haciendo que termine el cliclo y pasando a otra condiciones 
    # fuera del while
    b += 1

print()
# continue va a continuar con el loop, va a saltarse todo lo que se encuentra debajo de ella y regresa
# al inicio del while, esto puede crear conflicotos asi que se debe de escribir bien el codigo para 
# no caer en un bucle infinito
c = 0
while c < 5:
    c += 1
    if c == 3: # cuando c sea 3 se activa el continue, lo que hace que no se haga la instruccion de
                # print(), se vuelve a dar el ciclo esta vez aumentandolo en 1, siendo 4 pero esta 
                # vez si se va a imprimir print() normalmente
        continue
    print(c)