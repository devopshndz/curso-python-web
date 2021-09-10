# para utilizar los módulos que creemos o descarguemos debemos utilizar la palabra reservada import
# seguido del nombre del archivo

import Modulo as Xs
# con esto importamos el modulo y ahora podemos acceder directamente a todas las funciones y 
# variables que hayamos creado en el archivo

print(Xs.mascotas)
# esta acción hara que pidamos imprimir del Modulo previamente crado la lista llamada mascotas
# al usar modulos en python lo que hacemos es que no se reutilice código ya escrito y guardado 
# en un archivo, directamente se importa el archivo con la palabra reservada import y se puede tomar 
# y usar todas sus variables, funciones y demas cosas que estén en la posicion mas arriba de dicho 
# modulo 

Xs.saludo('Grecia')
# estamos utilizando la funcion de saludo que creamos dentor del archivo Modulo

### Renombrar el nombre del modulo
# le asignamos al nombre del modulo un as seguido con el nuevo nombre, esto no cambiará el nombre en 
# si pero si creará una referencia a dicho modulo y será más facil de utilizar
# import Modulo as Xs       Xs será el nuevo nombre de modulo a utilizar