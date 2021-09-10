### escribiendo archivos

# si queremos escribir en este archivo de chancho, debemos utilizar los permisos.
# 'a'
d = open('Python/7- Gestion de archivos/chancho.txt', 'a')

d.write('\nAgregaremos una nueva linea a nuestro archivo') 
# debemos colocar \n para salto de linea ya que se agg el texto al final pero no hacia abajo.

d.close()

x = open('Python/7- Gestion de archivos/chancho.txt')
print(x.read())

# NOTA IMPORTANTE!
# despues de hacer todo lo que hicimos arriba, si cambiamos el permiso de 'a' -> 'w' nos va a permitir 
# escrbir en el archivo, pero, 'w' modifica (elimina) el contenido del archivo y escribiría lo del
# d.write, al imprimir, solo se imprime lo escrito en el d.write, por eso hay que tener mucho cuidado 
# con los permisos que le demos a los archvos.

# primero leer y luego hacer modificaciones, siempre.