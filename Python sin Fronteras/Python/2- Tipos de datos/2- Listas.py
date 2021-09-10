# Las listas en python son una colección de datos o varios datos agrupados dentro de una lista.

lista = ["Hola", "Mundo", 3, "Chanchito feliz"] # definir lista vacía
print(lista) # imprime la lista

lista2 = lista.copy() # Aquí lo que se genera es que se cree una copia en la lista, lista2 
                        #toma todos los valores de lista 

# Agg un elemento a la lista: metodo append:
lista.append(4) # append lo que hace es que agarra un elemento que se le indique dentro del parentesis
                    # y lo agg al final de la lista. Uno y solo uno.
                    # la sintaxis es nombredelista.append(valor)
print(lista, lista2) # imprimimos la lista como va con medificaciones e imprimimos 

# metodo clear: elimina todo los elementos que contiene una lista: se debe colocar nombre.clear()
#lista.clear()
print(lista) # Al imprimir la lista aparece vacía.
print()

# Contar elemento y ver cuantas vaces se repite en un a lista. IMPORTANTE!
# se utiliza el metodo count() y dentro del parentesis se pasa el valor que se desea averiguar
print(lista.count(2)) # aquí contamos cuantas veces está el elemento 2 en la lista, en este caso 1 vez

# Saber cual es la longitud de la lista (cuantos elementos hay dentro de la lista) funsion len()
print(len(lista)) # dentro del () va la lista a contar: len(lista) arrojará en este caso el valor de 4
print(len(lista), len(lista2)) # aquí se cuenta las longitudes de ambas listas, lista y lista2
# Se puede hacer de esta manera, creando variables que serán llamadas:
LargoLista = len(lista)
LargoLista2 = len(lista2)
print(LargoLista, LargoLista2)
print()

# Accediendo a elementos de la lista.
print(lista[0]) # aca lo que estamos haciendo es imprimir lista pero solo el elemento 0 se debe 
                # escribir dentro de [] la posicion del elemento a ver, recordar que en python
                #  el primer elemento es el indice 0
print(lista[0], lista[1], lista[3]) # imprimimos multiples elementos de la lista
print()
# Eliminar elementos de la lista
# Metodo pop: nombrelista.pop = va a eliminar el ultimo elemento de la lista
print(lista) # lista normal
lista.pop() # borramos el ultimo elemento que es el 4
print(lista)
lista.pop()
print(lista)
lista.pop()
print(lista)
lista.pop()
print(lista)
# Como vemos se van eliminando uno a uno el ultimo elemento que queda de la lista
# Ahora, si queremos optar por eliminar cualquier elemento de la lista sin importar la posicion
# debemos utilizar el metodo remove():
lista3 = ["Hola", "Mundo", 3, "Chanchito feliz"]
print(lista3)
# para utilizar remove() debemos escribir dentro del parentesis EL ELEMENTO que queremos borrar:
lista3.remove("Mundo") # vamos a borrar el elemento "Mundo"
print(lista3)
# Debemos tener en cuenta, que al utilziar remove() este metodo es suceptible a mayusculas, por ende,
# debemos escribir tal cual está el elemento
lista3.remove(3)
print(lista3)
print()

# Alternar el orden de la lista: reverse
lista4 = ["Hola", "Mundo", 3, "Chanchito feliz"]
print(lista4)
# llamamos al metodo reverse()
lista4.reverse()
print(lista4)
# nos muestra que el orden de la lista está ahora invertido, el ultimo elemente es ahora el primero y 
# viceversa

print()
# Ordenar la lista: sort
# debemos tener cuidado y tener en cuenta,q ue al utilizar el metodo sort para ordenar la lista, 
# los datos dentro de la lista deben ser del mismo tipo, sino nos arrojará un error.
# vamos a borrar el numero 3 que es entero de nuestra lista y vamos a agregarlo como str:
lista4.remove(3)
lista4.append('3')
print(lista4) # recordemos que anteriormente habíamos invertido la lista con reverse.
lista4.sort()
print(lista4) # como podemos observar al imprimir la lista4 se a ordenado como estaba anteriormente, 
# sort() loq ue hace es revertir el metodo reverse()

# Metodo index: sirve para saber en que posición se encuentra un elemnto dentro de la lista
print(lista4.index('3')) 