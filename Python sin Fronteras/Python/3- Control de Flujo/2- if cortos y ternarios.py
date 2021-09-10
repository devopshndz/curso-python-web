# se puede escribir un if en una sola linea: esto se da cuando nosotros tenemos que 
# hacer pequeñas evaluaciones.
if 2 < 5: print("Estamos haciendo un if de una sola linea")
# se debe tener en cuenta la sintaxis if condicion: espacio resultado.
# Esta forma se da si y solo si, el resultado de nuestra consulta va a dar True

# Otra forma: cuando nuestra consulta da False:
# 1ero debemos escribir un mensaje en print que diga cuando devuelve true
# 2do escribimos el if y la condicion
# 3ero escribimos un else con un print() para decir que devuelve false:
print("cuando devuelve True se imp esto ") if 2 != 2 else print("cuando devuelve false imprimer esto")
# tener algo en cuenta:                           aquí no se escribe : despues del if. 
# Se coloca despues de la instrucción el else seguido del print

# Esto que acabamos de ver se denomina operador ternario: un OT es cuando dentro de un if de 
# una sola linea tenemos el caso de evaluar en true y en false
