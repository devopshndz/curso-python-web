# Los diccionarios son muy similares a las listas, la diferencia radica en que en vez de acceder 
# a los elementos de un diccionarios no se utilizan los indices 0, 1, 2, 3... sino string:

diccionario = {
    "Nombre":"Chanchito feliz",
    "Raza":"Persa",
    "Edad":3
}
# La estructura del diccionario es sencilla, se escribe el nombre del diccionario segudo de = {}
# Dentro de las {} se escriben los elementos, siendo el primer elemento un string seguido por :
# y luego la referencia de ese elemento ejemplo: 'Equipo':'Junior', la coma del final es por si 
# queremos utilizar muchos mas elementos que es lo normal en diccionarios.

#Para acceder a los diccionarios:
print(diccionario)

# Acceder a un valor especifico del diccionario:
# Se debe utilizar [] dentro de la llamada del diccionario y pasar la propiedad que deseamos ver 
# como string
print(diccionario["Nombre"])

#Forma mas explicita para llamar los valores de un diccionario: .get()
print(diccionario.get("Raza"))
print(diccionario.get("Nombre"), diccionario.get("Edad"))

print(diccionario)
# Modificar valores del diccionario: nombre["propiedad a modificar"] = "modificacion" sea string o numero
diccionario["Nombre"] = "Pelusa"
print(diccionario)
print(diccionario.get("Nombre"))

# Tambien se puede utilizar la propiedad len() para ver la cantidad de elementos que contiene el diccionarios
print(len(diccionario))

# Agregar valores al diccionario
diccionario['Ronrronea'] = 'Si' # la sintaxis es nombreDiccionario['nombreCategoriaAagg'] = 'propiedad'
# Al agg un elemento al diccionario este toma el ultimo lugar del diccionario
print(diccionario)

# Hacer una copia del diccionario: 
CopiaGatito = diccionario.copy()
print(CopiaGatito)

# Eliminar un elemento del diccionario: metodo pop()
diccionario.pop('Ronrronea')
# sintaxis: nombreDiccionario.pop('CategoriaAEliminar')
# Debemos tener en cuenta algo, al utilizar .pop() dentro de los parentesis va la categoría, 
# ya que este borra toda la categoría, no se puede borrar el valor de una categoría, se tiene que 
# borrar toda la categoría
print(diccionario)

# Otra forma de eliminar: popitem()
# Este lo que hace es eliminar el utlimo elemento agg al diccionario
diccionario.popitem()
# Al ser el ultimo elemento el que se va a eliminar, popitem se deja vacio.
print(diccionario)

# Otra forma de eliminar categorías de diccionario: palabra reservada del
del diccionario['Raza']
# del significa delete, Sintaxis-> del nombreDiccionario['categoriaAEliminar']
print(diccionario, CopiaGatito)

# Eliminar todos los valores de un diccionarios: .clear()
diccionario.clear()
# Al utilizar el .clear() en el diccionario, se borran todas las categorías y valores dentro de este
# al imprimir se va a mostrar solamente {} vacios en señal de que todos los elementos de ese 
# diccionario han sido eliminados.
print(diccionario, CopiaGatito)

# Otra forma de realizar una copia de diccionario es con dict()
otraCopia = dict(CopiaGatito)
# Sintaxis--> nombreDeLaCopia = metodo dict(NombreDelDiccionarioACopiar)
print(otraCopia)