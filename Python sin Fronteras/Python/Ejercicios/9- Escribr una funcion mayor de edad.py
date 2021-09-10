# Escribir una funcion que indique si el usuario es mayor de edad.

# definimos la funcion mayor de edad
def MayorEdad(usuario):
    return usuario.edad > 17 # retornaremos un resultado booleano, si es mayo a 17 True, sino, False

# crear la clase de usuario
class Usuario:
    def __init__(self,edad): # propiedad a usar: edad
        self.edad = edad

usuario = Usuario(int(input('Digite la edad del usuario 1: '))) # instanciamos un usuario
usuario2 = Usuario(int(input('Digite la edad del usuario 2: '))) # instanciamos otro usuario

resultado1 = MayorEdad(usuario) # guardamos en una variable el resultado que nos arroja
resultado2 = MayorEdad(usuario2)

print(resultado1,resultado2) # imprimimos los resultados