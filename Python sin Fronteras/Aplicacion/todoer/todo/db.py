import mysql.connector

import click # para ejecutar comandos en la terminal
from flask import current_app, g # g es una variable que esta en la app, usuario almacenado dentro de g
from flask.cli import with_appcontext # cuando estemos ejecutando el scipt de la bd para saber el contexto de esta
from .schema import instructions # archivo que va a contener todos los scripts que necesitamos para crear la base de datos

# funcion para obtener base de datos
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        # acceder al cursor para ejecutar las consultas de sql
        g.c = g.db.cursor(dicctionary=True)
    return g.db, g.c

# funsion que cierre la conexion de la bd cada vez que realizemos una peticion para no dejar la conexion abierta
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# funcion que pasemos argumento app de __init__ y agg la funcion que el tiene que ejecutar cuando este eliminando el contexto de la app
def init_app(app):
    app.teardown_appcontext(close_db)
    # configuramos esto llendo al archivo __init__.py