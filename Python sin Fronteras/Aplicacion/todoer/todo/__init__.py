import os # para acceder a variables de entorno

from flask import Flask

def create_app(): # testing o crear varias instancias de nuestra app
    app = Flask(__name__) # todas las app que creamos en flask son una instancia de la clase flask, esta va a mantener un estado interno con distintas conf de entorno y variables de usuario etc.

    app.config.from_mapping( # definir variables de configuracion que utilizaremos despues
        SECRET_KEY = 'mikey',
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE = os.environ.get('FLASK_DATABASE_HOST')
        
        
        # SECRET_KEY es una llave que se utilizara para definir las secciones en nuestra app
        # una seccion es cuando generamos es una llave para el cliente, para utilizarla como referencia con datos que se ecnuentran guardados en el servidor = una cookie
    )

    from import db # para traernos el archivo db

    db.init_app(app) # ejecutamos la funcion de init_app con la aplicacion app. volvemos a db y...

    # CREAR UNA RUTA DE PRUEBA
    @app.route('/hola')
    def hola():
        return 'Chanchito feliz'

    return app