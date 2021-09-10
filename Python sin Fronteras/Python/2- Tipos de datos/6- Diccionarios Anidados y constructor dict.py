# Colección de mas diccionarios: diccionarios anidados.

gatitos = {
    "Flyffy": {"Nombre": "Fluffy", "Edad": 5},
    "Mamba": {"Nombre": "Mamba","Edad": 24}
}

# Los diccionarios anidados son diccionarios dentro de un diccionario.
# En el ejemplo anterior, tenemos un diccionario de gatitos, el cual contiente a Fluffy y a Mamba, 
# ambos son dos diccionarios tipo string y se caracterizan porque ambos inician con 
# "nombre del diccionario": {todas las categorías que queramos agregar separadas de ,} ,
print(gatitos)

# Tambien se pueden realizar diccionarios anidados utilizando variables que contengan diccionarios:
buxi = {
    "Nombre": "Buxi",
    "Edad": 10
}
Pelusa = {
    "Nombre": "Pelusa",
    "Edad": 9
}
# Ahora creamos un diccionario Perritos el cual le vamos a pasar los valores de buxi y Pelusa:
perritos = {
    "Buxi" :buxi,
    "Pelusa" : Pelusa
}
# Esta forma lo que hace es que al crear el diccionario perritos, colocamos los demas diccionarios 
# "Buxi" y " Pelusa" pero en vez de escribir todos las categoría dentro de ellas, colocamos 
# "Buxi": buxi,
# "Pelusa": Pelusa
# Se les pasan las variables que dentro de ellas ya contienen los diccionarios
print(perritos)
print()

# Contructor dict para hacer diccionarios:
# Se crea una variable y a esta se le asigna la funcion dict() dentro de los () van a ir todos los 
# valores que va a tener el diccionario
perros = dict(nombre="Rodolfo", edad=10)
# Al utilizar la funcion dict() python detecta que queremos hacer un diccionario, por ende, no hay 
# necesidad de escribir la categoría entre comillas "" ya que es detectada como categoría, los 
# siguiente es escribir = y ahora si podemos escribir entre "" el valor de la categoría o en 
# numeros 1, 2, 3... si queremos un valor numerico. Para agregar mas valores simplemente colocamos , y 
# luego la categoria = "valor".  
print(perros)
gatos = dict(nombre="Misifu", edad=10)
print(gatos)
print(perros, gatos)

# Anidar diccionarios usando dict
animales = {
    "Perros":perros,
    "Gatos":gatos
}
print(animales)