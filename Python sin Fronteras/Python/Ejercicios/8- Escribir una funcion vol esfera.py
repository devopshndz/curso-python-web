# Escribir una funcion que devuelva el volumen de una esfera por su radio.
# formula: 4/3 * pi * r³

def calcularVol(r): # definimos la funcion pasandole como propiedad el radio r
    return 4 / 3* 3.14 * r ** 3 # retornamos el valor que da la operacion de la formula.
                                # para escribir una potenciacion colocamos ** y el exponente: r**3 = r³

resultado = calcularVol(int(input('Digite el radio: '))) # hacemos que el valor lo entreguemos por teclado
print(resultado)