# El input() se utiliza para que a una variable que va a recibir un valor, el usuario 
# desde teclado pueda ingresar ese valor.

dato = input("Escribe el dato: ")
print(dato)
print(type(dato))
# Para tener en cuenta: Cuando utilizamos input, python reconoce que el dato a ingresar es un dato
# tipo string, de ahi que cuando imprimimos el dato y lo pasamos por la funcion type() nos arroja str

dato2 = int(input("Ingresa un dato numerico: "))
print(dato2)
print(type(dato2))
# En este ejemplo estamos pidiendo un dato numerico tipo int, siempre antes del input debemos colocar
# el tipo de dato que queremos para que no arroje un resultado string, en este caso colocamos 
# int(input()) pero se pueden colocar mas datos como float(input())

# otro ejemplo rapido que veremos en el ciclo for es la entrada por teclado de valores a una lista:
lista = []
for x in range(int(input("Ingresa cuantos valores va a tener la lista: "))):
    lista.append(int(input("Ingresa el valor: ")))
print(lista)
# 1. creamos la lista de nombre lista = []

# 2. creamos un ciclo for el cual x va a se la posicion inicial hasta range que será la funcion para 
# generar un rango de valores, este por lo general esta definido antes, pero esta vez vamos a hacer 
# que el usuario diga cuantos valores tendrá la lista, seguido del tipo de dato int para establecer 
# el monto de valores ya que si no pasamos este tipo de valores en entero arroja un error a creer 
# que es un string y no generara la lista con valores.

# 3. agg valores a la lista con append: lista.append y ojito aquí: si seguido de append() 
# colocamos dentro de los parentesis input("") los datos a agregar serán de tipo string. Pero, 
# si dentro del append colocamos int(input("")) ó float(input("")) ya le estamos estableciendo 
# nosotros que el tipo de dato a ingresar será diferente a string, puede ser int o float.

# 4. imprimimos la lista