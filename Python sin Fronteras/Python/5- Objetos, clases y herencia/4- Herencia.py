# herencia es un concepto de poo y se utiliza para poder reutilizar lo maximo posible el codigo 
# en estructuras que sean similares

# vamos a crear una clase de administrador:

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self): 
        print('Hola, mi nombre es', self.nombre, self.apellido)

# por fuera de la clase Usuario y de su metodo creamos la otra clase a la cual aplicaremos herencia:
class Admin(Usuario): # para aplicar la herencia creamos una clase y le pasamos como propiedades la clase que va a heredar
    def superSaludo(self):
        print('Hola!, me llamo',self.nombre,'y soy administrador')

usuario = Usuario('Grecia','Rocha')
usuario2 = Usuario('Alberto','Hernandez')

admin = Admin('Super','felíz') # Creamos objeto de admin
admin.saludo() # lo llamamos con el metodo saludo que hace parte de la clase Usuario, esto es valido
# porque la clase Admin está heredando todos los metodos y propiedades de Usuario
admin.superSaludo()

# realización:
# primero creamos una clase por fuera de la clase que va a ser heredada.
# le pasamos como propiedades a dicha clase la clase heredada: class Admin(Usuario): con esto ya está 
# tomando heredado tanto sus propiedades como metodos y se podrán utilizar.
# Acto seguido lo que queda es, o agregar mas propiedades que solo dicha clase podra acceder o agg mas 
# metodos que tambien dicha clase solamente podrá acceder.
# se crea la instancia (objeto de admin y se le pasan los argumentos de nombre y apellido que son heredados)
# y se utiliza en este caso el metodo saludo y super saludo, uno heredado y otro propio.