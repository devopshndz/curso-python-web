# PIP es una herramienta que nos permite gestionar los paquetes que tenemos instalados en python.
# este gestor nos va a permitir a nosotros instalar modulos, podremos ver el listado de los modulos 
# que tenemos instalados y poder eliminar modulos.

# como no sabemos ni los nombres de los paquetes debemos buscarlos en internet, hay una pagina que 
# tiene una gran cantidad de paquetes y es https://pypi.org/
# en dicha pagina estan los paquetes creados por la comunidad y que podemos instalar y utilizar.
# cuando encontremos un paquete a utilizar nos mostrará en la página como importarlo y utilizarlo 
# por tal motivo debemos prestar atencion a que nos dice.
# luego de saber que paquete tenemos que utilizar, se debe ingresar a la terminal y escribir:
# $ pip3 intall nombreDelPAquete
# para este caso utilizaremos camelcase: pip3 install camelcase

#Basic Usage
#===========
#.. code:: python
#from camelcase import CamelCase
#c = CamelCase()
#s = 'this is a sentence that needs CamelCasing!'
#print c.hump(s)
# This is a Sentence That Needs CamelCasing!

from camelcase import CamelCase
c = CamelCase() # instancia de CamelCase
s = 'esta oración necesita CamelCase'
CamelCased = c.hump(s) # asignamos a la variable CamelCased
print(CamelCased)

# este es un ejemplo de como utilizar modulos de la comunidad, la misma comunidad proporciona como 
# utilizar los codigos de estos, estas explicaciones se encuentran en la pagina del proyecto (pypi.org)

# para ver la lista de paquete que tenemos con pip3 debemos escribir en terminal $ pip3 list
# para eliminar un paquete simplemente se debe escribir en la terminal $ pip3 unistall nombrePaquete

