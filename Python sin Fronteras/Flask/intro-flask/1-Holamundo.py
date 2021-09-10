### para comenzar en flask hay que importar la libreria de flask
from flask import Flask # esta librería nos servirá para crear nuestra aplicacion.
app = Flask(__name__) # va a tener el valor de main

# utilizacion de decoradores @
@app.route('/') # la ruta del trabajo en este caso de la raiz de nuestra aplicacion. se pueden agg mas rutas

# definimos una funcion en este caso un index que hará un retorno de hola mundo
def index():
    return 'Hola mundo'

# para correr la aplicacion debemos irnos al entorno de desarollo de flask en la terminal y:
# venv$ export FLASK_APP=1-Holamundo.py
# venv$ flask run
# todo desde la terminal para que este lo pueda correr.
# luego de esto nos saldrá corriendo el programa en ambiente de produccion, nos arrojará una ip a la cual si
# pinchamos nos llevará a el servidor donde esta corriendo nuestra app, pero sigue siendo ambiente de produccion
# debemos cambiar a ambiente de desarrollo, development

# agg otra ruta
@app.route('/lala')
def lala():
    return 'lala'

@app.route('/lele')
def lele():
    return 'lele'

# para verla en nuestra app debemos ir al navegador y en nuestra ip dada por flask se coloca /lala para que se vea
# pero al estar en ambiente de produccion esto no es posible, debemos pasar a ambiente de desarrollo:
# para activar el modo de desarrollo debemos:
# 1 cancelamos el servidor
# 2 volvemos a activar flask y escribimos:
# $ export FLASK_ENV=development
# esto hará que el entorno sea de desarrollo y ahora si se pueda ver la ruta /lala y cualquiera