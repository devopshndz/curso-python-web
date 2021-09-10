# Renderizar plantillas: Que le vamos a devolver nosotros al usuario_ Objetos json o una pagina en html
# Como podemos devolverle algo al usuario en este caso una pagina html 

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
    return render_template('lele.html')
    # render_template nos servirá para devolverle al usuario una pagina o una plantilla
    # cuando llamemos la ruta /lele este buscará en la carpeta template dentro de intro-flask la plantilla
    # de lele.html alojada en ella
    # vamos al server y le damos la ruta de /lele y este nos lleva a la pagina lele.html alojada en la carpeta templates