# Datos de formulario

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/post/<post_id>', methods=['GET','POST'])
def lili(post_id):
    if request.method == 'GET': # con request hacemos que se pueda utilizar varios tipos de metodos en porciones
        return 'El id del post es: ' + post_id
    else:
        return 'este es otro metodo diferente a GET'

@app.route('/lele', methods=['POST'])
def lele():
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'lele'
# Debemos colocar print(request.form['llave1']) para que nos arroje este dato al pedirlo por medio de flask 

# en una terminar a parte de nuestro servidor que esté corriendo, se escribe lo siguiente:
# $ curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000
# curl: herramientos para llamados a nuestros servicios o api
# -d es la data que le estemos enviando a nuestro servicio
# -X para ejecutar
# POST,GET....
# ruta localhost:puerto/ruta
