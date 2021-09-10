# interactuar con bases de datos
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/post/<post_id>') # escribimos <> el cual contendrá la variable que mas adelante utilizaremos
def lala(post_id):
    return 'El id del post es: ' + post_id
# cuando escrbimos en la ip de la pagina el nombre de la ruta debemos pasarle el valor de la variable que declaramos
# en este caso el de post_id
# el post_id se utiliza mucho para ver entradas por ejemplo en blogs ya que cada post_id sería una entrada
# por otro lado, se puede tambien hacer interacciones con otros tipos de datos como enteros:
#@app.route('/post/int:post) si escribimos int: antes de la variable, flask declara que la variable es entera

@app.route('/lele')
def lele():
    return 'lele'