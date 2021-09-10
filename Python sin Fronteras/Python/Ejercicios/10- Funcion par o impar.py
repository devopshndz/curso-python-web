# escribir una funcion que diga si un numero es par o impar
# utilizaremos el operador de modulo % que indica el resto de una division: 10 Mod 2=0
def es_Par(num):
    return num % 2 == 0 # retornamos la operacion de que el numero que demos %(mod) 2 sea igual a 0
                        # esto efectua la division entre 2 y al final debe dar True si su mod es 0 
                        # sino arrojara False porque su mod sea 1
    
resultado = es_Par(int(input('Escribe un numero: '))) # creamos variable a la cual le asignaremos la funcion
print(resultado) # imprimimos la variable