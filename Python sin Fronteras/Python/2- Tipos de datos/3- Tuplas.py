# Las tuplas son muy parecidas a las listas, pero, estas, una vez que las creas NO PUEDES MODIFICARLAS.
# Necesariamente se debe generar una copia de estas en el caso de querer cambiarlas

# Sintaxis:
tupla = ('Hola', 'Mundo', 'somos', 'tupla') # las tuplas son como las listas, pero en vez de 
                                            # utilizar [] utilizamos ()
print(tupla)
# Podemos observar que al imprimir la tupla, nos muestra sus valores dentro de () 
# a difierencia de las listas que nos los muestran dentro de []

# Las tuplas a diferencia de las listas tienen bastante menos metodos.

# metodo count: contará cuantas veces está un argumento en la tupla.
print(tupla.count('Hola'))

# Metodo index: sirve para saber en que posición se encuentra un elemento dentro de una tupla
print(tupla.index('Hola'))

# Modificar contenido de una tupla: Python no permite hacer modificaciones a una tupla, pero,
# se puede realizar modificaciones y convertimos una tupla en una lista.

listaDeTupla = list(tupla)
# lo que se hace es lo siguiente: 
# 1. se crea una variable y se le asigna la funcion list() la cual va a convertir valores a lista
# 2. dentro de list() se coloca nuestra tupla: list(tupla)
# 3. se imprime la nueva lista para comprobar que ya no es una tupla sino una lista:
print(listaDeTupla)
# Ya podemos trabajar con la nueva lista creada a partir de la tupla.
listaDeTupla.append('Junior tu papa')
print(listaDeTupla)