# clases y objetos.
# Una clase es como el plano de una vcasa, nuestra clase nos va a indicar las dimenciones que tiene 
# la 'casa', el # de habitaciones, nos va a dar una idea de como van a ser las 'casas' cuando nosotros 
# las construyamos. 
# las instancias (objetos) son las 'casas' construidas de la vida real.
# las instancias u objetos irán dentro de las clases.

# el plano = las clases
# instancias = objetos.

# Clases: palabra reservada class
# ejemplo de un usuario, el plano de un usuario, como se debiese ver un usuario:
class Usuario: # Sintaxis: class NombreDeLaClase (siempre inicia en mayuscula, SIEMPRE):
    nombre = 'Felipe'

# crear una instancia para la clase Usuario
usuario = Usuario()
# sintaxis: nombreDeInstancia = NombreDeLaClasePerteneciente()
# para crear un objeto (instancia) colocamos el nombre de dicho objeto y lo instanciamos (le damos 
# como valor la clase a la que pertenece, así estamos diciendo que ese objeto pertenece a dicha clase)
# NOTA!!!!!! --> todas las instancias de la clase deben estar escritas 100½ en minúsculas.
print(usuario) # al imprimir nuestro objeto nos saldrá <__main__.Usuario object at 0x7f4585defe10>
# nos está indicando que este objeto es una instancia de la clase usuario

# otro ejemplo de una clase con una instancia.
class User:
    nombre = 'Beto'
    apellido = 'Hernández'
usuario1 = User()
print(usuario1)
# si queremos acceder a las propiedades que tiene el objeto debemos colocar objeto.nombrePropiedad
print(usuario1.nombre, usuario1.apellido)
# al colocar el . estamos creando un enlace entre el objeto y la propiedad para así traer el valor de 
# dicha pripiedad y poder tenerla a disposicion.

# Cuando nosotros estemos trabajando en la vida real con una base de datos, va a ser muy dificil 
# encontrar objetos con datos similares. 
# Aquí por ejemplo, vamos a optar por objetos con distintos nombres y apellidos:
print()
class User2:
    def __init__(self, nombre, apellido): #sintaxis: def __init__(self, argumentos):
        self.nombre = nombre # self tendrá la propiedad nombre con valor = nombre
        self.apellido = apellido # cuando decimos que self tendra la propiedad tal, le damos el valor
                                # de dicha propiedad previamente inicializada en el __init__

        # self va a ser la referencia del objeto cuando lo instanciamos.
        # Siempre que en python genermos una instancia (objeto) el primer metodo que se va a ejecutar 
        # será el __init__ y con todos sus self.
        # self no es necesario que se lo pasemos como parametro a cada usuario, self es un valor reservado 
        # las clases que podemos llamar para hacer referencia siempre a las instancias de nuestras clases
usuario = User2('felipe','feliz')
usuario2 = User2('Beto','Hernandez')
print(usuario.nombre, usuario.apellido)
print()

# creamos clase
class Amor:
# inicializamos metodo __init__:
    def __init__(self, nombre, apellido, edad, estado):
        # pasamos las propiedades:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estado = estado
# definimos las instancias:
enamorado1 = Amor('Alberto','Hernandez',27,'Felizmente enamorado')
enamorado2 = Amor('Grecia','Rocha',22,'Felismente enamorada')
# imprimimos a los enamorados:
print('Nombre:',enamorado1.nombre,'Apellido:',enamorado1.apellido,'Edad:',enamorado1.edad,'Estado:',enamorado1.estado)
print('Nombre:',enamorado2.nombre,'Apellido:',enamorado2.apellido,'Edad:',enamorado2.edad,'Estado:',enamorado2.estado)
print("El señor " + enamorado1.nombre, enamorado1.apellido + " está enamorado de la señora", 
enamorado2.nombre, enamorado2.apellido + " y ambos son muy felices") # concatenamos
print("El señor ", enamorado1.nombre, enamorado1.apellido, " está enamorado de la señora", 
enamorado2.nombre, enamorado2.apellido, " y ambos son muy felices") # sin concatenar
print("Así se crean clases con objetos")

# las clases serán el plano de lo que queremos crear, debemos siempre definir el metodo __init__ para
# a traves de él, declarar las propiedades de la clase. Creamos las propiedades. 
# creamos unos usuarios en este caso enamorados y a esos usuarios los creamos como instancias (objetos). los objetos tendran una serie propiedades 
# (nombre, apellido, edad, etc.) los cuales instanciaremos en la clase y luego en los self, 
# que es una palabra reservada para las clases que nos servirá para poder hacer referencia a los objetos.
# al instanciar un objeto le pasaremos a este la clase correspondiente y los parametros de esta clase.