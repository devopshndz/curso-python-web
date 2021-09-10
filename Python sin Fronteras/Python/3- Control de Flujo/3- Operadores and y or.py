# and y or: sirven para evaluar mas de una condicion dentro de un if o de un elif.
# and significa y, y solo se da si todas las condiciones se cumplen.
# or significa o, y se efectua cuando 1 o mas condiciones se cumplen.

# and
if 2 < 5 and 3 > 2:
    print("instruccion and verificada, ambas devuelven True")

if 2 < 5 and 3 < 2:
    print("esta instuccion no se mostrará, ya que no se cumple el operador and y da False")
print()
# si hay varias instrucciones y con que una sola no cumpla el operador and, devolverá false

# or
if 2 < 5 or 3 > 2:
    print("instruccion or verificada, ambas dan true")
if 2 < 5 or 3 < 2:
    print("instruccion or verificada, un de las 2 instrucciones da true")
if 2 == 3 or 3 == 2:
    print("esta instruccion no se mostrará, ya que no se cumple el operador or y da Flase")
# con or pueden cumplirse todas las instrucciones o puede que se cumpla 1 sola, dará True, pero
# si no se cumple ninguna dará False

if 2 < 3 and 3 < 4 or 5 == 5:
    print("Todo se cumple")
# Se pueden conbinar and y or, siempre y cuando, todo de True por parte del and. 
# Si por parte del or no se cumple, no hay problema ya que el mismo operador or está anidado con el o 
# los operadores and que si se cumplieron:
if 2 < 3 and 3 < 4 or 5 != 5:
    print("Los and se cumplen pero el or no se cumple, sin embargo la salida va a ser verdadera gracias a los and")