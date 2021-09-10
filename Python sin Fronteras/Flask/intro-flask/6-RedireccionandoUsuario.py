# redireccionando al usuario desde una ruta hacia otra

from flask import Flask, request, url_for, redirect # importamos redirect desde flask
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
    return redirect(url_for('lala', post_id='2')) # redireccionamos SIEMPRE HAY QUE RETORNARLA!!
    return 'lele'