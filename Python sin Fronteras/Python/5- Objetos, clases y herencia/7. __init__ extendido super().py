        ### super() ###

# Esta función nos permite invocar y conservar un método o atributo de una clase padre (primaria) 
# desde una clase hija (secundaria) sin tener que nombrarla explícitamente. Esto nos brinda la 
# ventaja de poder cambiar el nombre de la clase padre (base) o hija (secundaria) cuando queramos 
# y aún así mantener un código funcional, sencillo  y mantenible.


# Herencia simple de clase y atributos en python con super()
#Supongamos que queremos que una clase hija o secundaria herede los atributos de clase primaria o 
# padre. Si nosotros no recurrimos a la función super, o llamamos al constructor __init__ especificando
#  los atributos. Deberemos reescribirlos, lo cual en una clase por ejemplo con 20 atributos seria una 
# perdida de tiempo enorme! Fíjate en el ejemplo de abajo:

# a la clase padre se le puede asignar (object) para referenciar como ibjeto y se la clase padre
class Padre(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos en el constructor de la clase
        self.ojos = ojos
        self.cejas = cejas
    

class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #Definimos los atributos en el constructor
        self.ojos = ojos #Sobreescribimos cada atributo
        self.cejas = cejas
        self.cara = cara #Especificamos el nuevo atributo para Hijo

Beto = Padre('marron','delineadas')
Apolo = Hijo('negros','largas','ancha')
print(Beto.ojos, Beto.cejas)
print(Apolo.ojos, Apolo.cejas, Apolo.cara)
print()

# Esto podemos también podemos hacerlo así, llamando al constructor de la clase padre especificandola:
class Padre2(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo2(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        Padre.__init__(self, ojos, cejas) #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
        
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)
print()

# O podemos hacerlo, utilizando super(). De esta forma es casi el mismo código pero no necesitamos 
# especificar la clase padre, por lo que podremos cambiarle el nombre en cualquier momento y nuestro 
# código seguirá funcional, fíjate:

class Padre3(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo3(): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
        
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print(Tomas.ojos,Tomas.cejas,Tomas.cara)
# otro ejemplo


class Animales(object):
    def __init__(self,tipo,nombre):
        self.tipo = tipo
        self.nombre = nombre
    
    def Saludo(self):
        print('Hola, soy',self.tipo)

class Gato(Animales):
    def __init__(self,tipo,nombre,onomatopeya):
        super().__init__(tipo,nombre)
        self.onomatopeya = onomatopeya
        print('gatito extendido y hago',self.onomatopeya)

class Perro(Animales):
    def __init__(self,tipo,nombre,patas):
        super().__init__(tipo,nombre)
        self.patas = patas
        print('gatito extendido y tengo',self.patas)

gatito = Gato('Gato','Sashita','Miau')
perrito = Perro('Perro','Buxi',4)
# Al simplemente intanciar la clase Gato o Perro en un objeto hace que se utilice todo lo de dicha clase
gatito.Saludo()
perrito.Saludo()
print()

# la clase super se utiliza demasiado en poo para tomar los atributos de la clase padre y sus metodos
# por parte de las clases hijo pero tambien para agregar propiedades nuevas a las clases hijos 
# conservando las propiedades de las clases padres

# Super en python y Herencia múltiple
# En la herencia múltiple de clases es donde podemos explotar al máximo la función super. 
# Vamos a ver otro ejemplo de herencia múltiple y cómo podemos utilizar la función super en el 
# para llamar métodos de clases padres o bases.

class Perros(object): #Declaramos la clase principal Perros
    def __init__(self,tipo):
        self.tipo = tipo

    def ladrar (self):
        print ("""GUAAAUU GUAAAUU!""")
        
    def grunir (self):
        print ("""GRRRRRR GRRRRR""")
class Caniche (Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""guau guau guau""")
        
    def grunir(self):
        print ("""gññññiii gñññiiii""")
class Pastor_Aleman(Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""GuaUUU GUAAAUUU GuaUUU""")
        
    def grunir(self):
        print ("Agrfgregreff aggrrfsgrrr")
    
class Shepadoodle (Caniche, Pastor_Aleman):#La clase hereda de las clases hijas de su padre Perros
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()

uno = Perros('Raza')
Tommy = Pastor_Aleman('Raza')
Piny = Caniche('Razita')
Cuchele = Shepadoodle('Razota')
print(uno.tipo)
Cuchele.ladrarx(5) # Imprime guau guau guau (5 veces) porque heredo el ladrido de la clase padre CANICHE
                    #Pero si eliminamos o renombramos el método ladrar de CANICHE que imprimiria?
                    #Imprimiria el ladrido del Pastor_Aleman
                    #Y  si borramos ambos? Imprimirá el ladrido de Perros!