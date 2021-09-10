# Valor por defecto al argumento para no pasar siempre un parametro a la funcion.
def miFuncion(argumento='chanchito'):
    print(argumento)

miFuncion('Batman')
miFuncion()
# En lo anterior, si definimos un argumento con su parametro desde la cabecera de la funcion, no habrá 
# falta pasar nada mas, simplemente se trabaja con este valor ya establecido. Pero, si al llamar la 
# funcion le pasamos otro parametro, este sustituye al anterior, sin embargo, si luego de esto no le 
# pasamos nada como está en el ejemplo, se ejecuta la funcion como ya estaba definida previamente.
print()

# Pasar una lista como argumento:
def miFuncionLista(lista): # como argumento le pasamos la lista a crear
    for x in lista: # ciclo for para recorrer lista
        print(x) # imprimimos elemento por elemento.

miFuncionLista(['chanchito','feliz']) 
# ojito, al pasar los parametro a la funcion debemos recordar que estamos haciendo una lista y debemos 
# pasar dichos parametro como si fuera una lista, por ende ['chancho','feliz'] 
print() 

# Retornar valor de una funcion;
def concatenarNombres(lista):
    i = '' # definimos un string vacío.
    for x in lista: 
        i = i + x + ' ' # i = vacío + elemento + espacio
    return i # retorna ese valor

# ojo: cuando nosotros retornamos valores (return) necesariamente debemos capturar esos valores en 
# una variable para que quede guardado.
# por ende debemos colocar en una variable la funcion:
nombres = concatenarNombres(['chanchito','feliz']) 
# al pasar estos argumentos se van capturando uno por uno gracias al ciclo for de la funcion y se 
# almacenan dentro de la variable nombre
print(nombres) 
# imprimimos la variable nombre y lo que se imprime será i = i + x + '' o sea chanchito primero y 
# luego feliz.