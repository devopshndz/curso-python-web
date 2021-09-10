# Abortar la ejecucion de nuestro codigo: podriamos devolver cualquier error que existe al usuario para que 
# estos puedan identificar el error

from flask import Flask, request, url_for, redirect, abort # importamos abort desde flask
#abort detiene la ejecucion de la app y devuelve un mensaje
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/post/<post_id>', methods=['GET','POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'este es otro metodo diferente a GET'

@app.route('/lele', methods=['POST','GET']) # agg el metodo GET
def lele():
    abort(404) # para detener la app y mostrar error colocamos abosrt() y dentro el tipo de error: 401, 404...
    return redirect(url_for('lala', post_id='2')) # redireccionamos SIEMPRE HAY QUE RETORNARLA!!
    return 'lele'