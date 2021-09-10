# Una variable es como una cajita a la cual le vamos a ir agregando un valor el cual a futuro nostros
# vamos a utilizar referenciandolos.
# En otras palabras, una variable es una cajita que contiene un tipo de dato.

x = 5   # variable x con valor 5 entero
y = 'Chanchito feliz'   # variable y con valor 'Chanchito feliz' el cual es un string al estar entr ''
print(x, y) # print me permite pasarle multiples argumentos para luego yo imprimirlos en pantalla
            # los argumentos pueden ser mensajes entre '', variables, entre otras mas, pero siempre 
            # se debe separar por una , cuando se coloquen 2 o mas argumentos.

email = 'chanchito@feliz.com'
print(email)
nombre_usuario = 'ALberto'  # python no permite utilizar - guiones medios para separar variables
_mivar = "variable1"
miVar = 'variable2'
MIVAR = 'variable3'
# hay tantas formas de escribir una variable, aquí unos cuantos ejemplos
print(nombre_usuario, _mivar, miVar, MIVAR)
# se pueden asiganar como variables numeros, solo si estos van siempre despues de una letra
# un numero no puede ser una variable que contenga un dato, python no lo permite.
a1 = 'variable4'
print(a1)

# multiples variables: python permite agregar variables multiples separadas con una , y con sus 
# respectivos valores tambien separados con una , al declararse:
a, b, c, d = 'beto', 'ama', 'a Grecia', 1000 
# como se puede observar, cada variable toma un respectivo valor en el mismo orden que estan escrita 
# las variables, a = 'beto, b = 'ama', c = 'a Grecia', d = 1000, ventajas que da python
print(a, b, c, d)
# muchas variables con un mismo valor:
e = f = g = 'chancho feliz'
# Como se puede observar, e, f, g son variables que tienen un mismo valor, 'chanchito feliz', 
# se declaran colocando un = entre cada una para indicar que tanto e como f como g van a contener 
# 'chanchito feliz' de valor
print(e, f, g)
print()

# Concatenar en python. 
# Python permite realizar concatenaciones entre variables, en este caso, variables con palabras
# Esto lo que significa es que podemos unir (concatenar) 2 o mas palabras y convertirlas en una frase 
# o en una variable nueva:
inicio = 'Hola '
final = 'mundo '
jo = '2021' # este no es un entero, es un string ya que el 3 está dentro de comillas ''
print(inicio + final + jo)
# NOTA: Para concatenar solo se puede hacer con variables de tipo string, si queremos 
# hacer una concatenación con una variable de tipo entero, nos marcará error.