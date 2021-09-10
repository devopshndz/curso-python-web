# Construyendo URL
# Redireccionando a usuarios

from flask import Flask, request, url_for # importamos url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/post/<post_id>', methods=['GET','POST'])
def lala(post_id):
    if request.method == 'GET': # con request hacemos que se pueda utilizar varios tipos de metodos en porciones
        return 'El id del post es: ' + post_id
    else:
        return 'este es otro metodo diferente a GET'

@app.route('/lele', methods=['POST'])
def lele():
    print(url_for('lala', post_id='2')) # En este caso estamos llamando la funcion lala y pasamos el argumento post_id con valor de 2
    # llamamos con POST desde terminal a la funcion lala con valor post_id=2, se ejecutará la funcion lala de arriba
    # indicamos en url_for el nombre de la funcion a la cual vamos a redireccionar al usuario
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'lele'

# al llamar los datos con -d y -X POST nos va a arrojar al inicio la ruta / ya que está llamando a la funcion index que es la /
# si queremos cambiar de ruta nos dirigimos a la funcion de la ruta que queremos cambiar, ejemplo: lala, ojito que aqui debemos ver
# que en lala tenemos metodos: