# eliminar propiedades y objetos: del

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def saludo(self): 
        print('Hola, mi nombre es', self.nombre, self.apellido)
        
usuario = Usuario('Grecia','Rocha')
usuario2 = Usuario('Alberto','Hernandez')

# Modificar argumentos de propiedades: 
# en este ejemplo vamos a midificar el nombre que tiene el usuario, luego de hacer eso al pasar el 
# metodo de saludo se visualiza el cambio aplicado. Tener en cuenta que siempre que se modifica alguna 
# propiedad, ya cambia el valor de esta, y se debe de escrbir codigo despues de esto para utilizarlo.
usuario.nombre = "Chanchito"
usuario.saludo()

# Para eliminar propiedades de una clase utilizamos la palabra reservada del.

#del usuario.nombre # la sintaxis: palabra reservada del objeto.NombreDePropiedad
#usuario.saludo()

# Al tratar de imprimir con el metodo de saludo que utliza la propiedad nombre nos marca error 
# porque hemos eliminado esa propiedad lo que hace que el codigo quede incompleto en el metodo saludo.

# Eliminar un objeto completo
del usuario
print(usuario)

# El objeto usuario no estará definido ya que con del lo eliminamos.