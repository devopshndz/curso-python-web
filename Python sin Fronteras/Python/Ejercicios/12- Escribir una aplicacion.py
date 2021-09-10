# escribir una aplicación que reciba una cantidad infinita de numeros hasta decir para, luego que 
# devuelva la suma de los numeros ingresados.

lista = [] # creamos una lista vacía
print('Ingrese numeros y para salir escriba basta: ')
while True: # ciclo while True para hacer que se cumpla y sea verdadero si....
    valor = input('ingrese un valor: ') # empezamos a agregar valores desde teclado.
    if valor == 'para':
        break
    # algo importante, no podemos colocar int(input())  ya que al colocar el inf valor == 'basta' 
    # estamos estableciendo que al escribir basta se va a salir del ciclo, si escribimos basta y 
    # tenemos int(input()) no nos va a aceptar la palabra basta porque al colocar el int no acepta str
    else:
        try: # elaboramos una excepcion en la cual pasaremos que el valor recibido ahora si pase a int
            valor = int(valor)
            lista.append(valor) # agg el valor a la lista
        except: # un except de que si no se agrega un numero sino una letra o una palabra 
                # arroje dato no valido
            print('Dato no valido')
            exit() # salida del except

resultado = 0 # variable resultado para la sumatoria debe inicializarce en 0
for x in lista: # ciclo for para recorrer la lista
    resultado += x # resultado va a ser igual a resultado + el numero de la poscion en la lista
print('la lista es:',lista) # imprimimos la lista
print('La sumatoria de los numeros dentro de la lista es:',resultado) 
# imprimimos la sumatoria de la lista