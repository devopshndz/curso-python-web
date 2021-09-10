# Metodos: se crean para hacer que se puedan hacer acciones con las propiedades de las clases.
# Crearemos un metodo que muestre un saludo, mostrando el nombre y apellido de los usuarios:


class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # definimos el metod a utilizar debajo de la clase creada con sus propiedades.
    def saludo(self):   # sintaxis: def NombreMetodo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)
        # el metodo no va a recibir ningun argumento, se escribe el self para referenciarce a si mismo
        # ya creamos el metodo que va a traer a pantalla los nombres y apellidos de los usuarios
usuario = Usuario('Grecia','Rocha')
usuario2 = Usuario('Alberto','Hernandez')

# Ahora llamamos al metodo desde los objetos:
usuario.saludo()
usuario2.saludo()

# Explicación: Lo que hacemos con los metodos es ahorrarnos escribir tantas lineas de código repetidas
# y simplemente crear un codigo que se va a ejecutar cada vez que lo llamemos. Tener en cuenta las 
# propiedades de las clases y de los metodos porque deben coincidir. En este ejemplo creamos una clase 
# con usuarios con nombre y apellido, creamos un metodo de saludo que va a traer el nombre y el apellido 
# de un usuario en concreto, el metodo no tiene propiedades, se referencia a si mismo con self y en su 
# "composicion" tiene dentro self.nombre y self.apellido porque tomará de estas propiedades los argumentos 
# que se les haya pasado. Al final, instanciamos los objetos con los argumentos y llamamos al metodo 
# con cada objeto: usuario.saludo() y usuario2.saludo()

# La finalidad de los metodos es la de poder reutilizar cuantas veces queramos el código de estos para 
# ahorrarnos tiempo, lineas de codigo y sobre todo, hacer un programa mas dinamico.
print()
# Ejemplo de calculadora:
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    # def metodo de suma:
    def suma(self):
        total = self.num1 + self.num2
        print('El resultado de la suma es:',total)

    # def metodo de resta:
    def resta(self):
        total = self.num1 - self.num2
        print('El resultado de la resta es:',total)

    # def metodo de multiplicación:
    def multi(self):
        total = self.num1 * self.num2
        print('El resultado de la multiplicación es:',total)
    
    # def metodo de division:
    def divi(self):
        total = self.num1 / self.num2
        print('El resultado de la división es:',total)

print("""Escoge una opción:
        1. Suma
        2. Resta
        3. Multiplicacion
        4. División
        5. Salir""")

dato = input('Escribe una opción: ')
if dato == "5":
    print("Hasta pronto!")
    exit
else:
    resultado = Calculadora(int(input("Escribe el primer dígito: ")),(int(input("Escribe el sugundo dígito: "))))
    if dato == "1":
        resultado.suma()
    elif dato == "2":
        resultado.resta()
    elif dato == "3":
        resultado.multi()
    elif dato == "4":
        resultado.divi()
    else:
        print("Opción invalida")