# compartir código entre clases:
# Lo primero será crear una clase Animales que contendrá nombre y onomatopeya del animal.
# Se crearán subclases de Gato, Perro, Ave que heredarán a la clase Animal y sus propiedades y metodos
# Aestas subclases le podremos agg otras propiedades, la sintaxis será: nombreProp = valor y para 
# llamar dicha propiedad se debe utilizar si o si el self.nombrePRopi

            ### Superclase Animal ###
class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def Saludo(self):
        print('Hola, soy un',self.tipo,'y mi sonido es el',self.onomatopeya)
        # self.tipo no aparece por ningún lado en la clase Animal, pero si aparece en las subclases 
        # hijas Gato, Perro, Ave, como propiedad, esto hace que, como dicha propiedad está declarada 
        # en esas clases, a la hora de llamar el metodo Saludo() desde un objeto instaciado con las 
        # subclases, el metodo detecta la propiedad tipo y le permite interactuar.

            ### Subclase Gato hereda Animal ###
class Gato(Animal):
    tipo = 'Gato' # Propiedad tipo con nombre 'Gato'

            ### Subclase Perro hereda Animal ###
class Perro(Animal):
    tipo = 'Perro' # Propiedad tipo con nombre 'Perro'

            ### Subclase Ave hereda Animal ###
class Ave(Animal):
    tipo = 'Canario'    # Propiedad tipo con nombre 'Canario'
    extremidades = '2'  # Propiedad extremidades con valor '2

            ### Otro método de saludo exclusivo de la clase Ave en donde están todas las propiedades ###
    def OtroSaludo(self):
        print('Hola, soy un',self.tipo,'y me llamo',self.nombre,'Y tengo',self.extremidades,'extremidades, y mi onomatopeya es el',self.onomatopeya)

gato = Gato('Fluffy','maullido')
perro = Perro('Doki','ladrido')
pajarito = Ave('Piolin','silvido')
gato.Saludo()
perro.Saludo()
pajarito.Saludo()
pajarito.OtroSaludo()


# metodo simplificado
class Animal:
    def __init__(self, nombre, onomatopeya, tipo):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
        self.tipo = tipo
    def Saludo(self):
        print('Hola, soy un',self.tipo,'y mi sonido es el',self.onomatopeya)

class Ave(Animal):
    extremidades = '2'
    
    def OtroSaludo(self):
        print('Hola, soy un',self.tipo,'y me llamo',self.nombre,'Y tengo',self.extremidades,'extremidades, y mi onomatopeya es el',self.onomatopeya)

gato = Animal('Fluffy','maullido','Gato')
perro = Animal('Doki','ladrido','Perro')
pajarito = Ave('Piolin','silvido','Canario')
gato.Saludo(), perro.Saludo(), pajarito.Saludo()
pajarito.OtroSaludo()