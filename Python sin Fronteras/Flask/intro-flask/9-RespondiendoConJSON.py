# Respondiendo con JSON: ademas de objetos html se pueden devolver objetos JSON

from flask import Flask, request, url_for, redirect, abort, render_template
# importamos el paquete de render_templete para poder utilizarlo
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
    # para devolver un archivo JSON debemos retornar un diccionario
    return {
        "username": "Chanchito Feliz",
        "email": "chancho@gmail.com"
    }

    # retornamos un diccionario con las propiedades que queremos devolver
    # al ir al server y colocar la ruta /lele esta nos devolverá un diccionario el cual es amigable con las 
    # apis rest