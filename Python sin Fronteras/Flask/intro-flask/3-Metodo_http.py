# configurar rutas para que sean accesibles a traves de metodos: sea uno o muchos.
# un metodo web nos indica la accion deseada que se quiere realizar sobre la ruta que nosotros hemos construido
# GET: cuando quieres listar o mostrar algo
# POST: cuando quieres crear algo
# PUT: cuando quieres actualizar
# DELETE: cuandoq ueires eliminar algo
# PATCH: actualizar parcialmente un registro 
from flask import Flask 
from flask import request # se importa tambien el metodo request. OJITO: se puede colocar al lado de Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

# se declara el methods y dentro de ella se colocan los metodos a utilizar
# separamos por funciones la utilizacion de los metodos para que sean independientes
# GET
# @app.route('/post/<post_id>', methods=['GET'])
# def lala(post_id):
#     return 'El id del post es: ' + post_id

# # POST
# @app.route('/post/<post_id>', methods=['POST'])
# def lele(post_id):
#     return 'El id del post es: ' + post_id

# Si quieren que una funcion maneje varios metodos se utiliza request:
@app.route('/post/<post_id>', methods=['GET','POST'])
def lili(post_id):
    if request.method == 'GET': # con request hacemos que se pueda utilizar varios tipos de metodos en porciones
        return 'El id del post es: ' + post_id
    else:
        return 'este es otro metodo diferente a GET'

# para llamar los metodos se escribe en una nueva ventana del terminal con venv activado:
# $ curl -X GET http:localhost:(num del puerto de conexion)/post/1
# $ curl -X POST http:localhost:(num del puerto de conexion)/post/1

# recordar que al final el /post/1 son los valores de la ruta y la variable, no se pueden olvidar