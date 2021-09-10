        ### __init__extendido ###
# Extender el comportamiento del metodo de __init__:

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def Saludo(self):
        print('Hola, soy un',self.tipo,'y mi sonido es el',self.onomatopeya)
        
    ### init extendido forma 1 ###
class Gato(Animal):
    tipo = 'Gato'
    def __init__(self, nombre, onomatopeya): # Cuando establecemos este init, ignoramos automaticamente
                                            # el de la clase padre, o sea, se utilizan sus propiedades
                                            # pero no lo que el de la clase padre hace.
        Animal.__init__(self, nombre, onomatopeya)
        # se debe referenciar el init de padre para utilizar sus propiedades y realziar otras acciones 
        # como un init diferente
        print('Hola, soy un',self.tipo,' extendido!')

    ### init extendido forma 2 super() ###
class Perro(Animal):
    tipo = 'Perro' 
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya) # super() hace referencia siempre a la clase padre Animal
                                                # y se llama al metodo init pasandole nombre y onomatopeya
        print('Instanciando a un perro')
        
class Ave(Animal):
    tipo = 'Canario'    
    extremidades = '2' 

    def OtroSaludo(self):
        print('Hola, soy un',self.tipo,'y me llamo',self.nombre,'Y tengo',self.extremidades,'extremidades, y mi onomatopeya es el',self.onomatopeya)

gato = Gato('Fluffy','maullido')
perro = Perro('Doki','ladrido')
pajarito = Ave('Piolin','silvido')
gato.Saludo()
perro.Saludo()
pajarito.Saludo()
pajarito.OtroSaludo()