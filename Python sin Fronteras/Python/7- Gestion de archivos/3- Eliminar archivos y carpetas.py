### para eliminar archivos y carpetas ###
# para eliminar los archivos en python se debe utilizar un modulo del sistema operativo llamado os
import os
# os nos da metodos para eliminar archivos y carpetas que se encuentran en el ordenador.
if os.path.exists('Python/7- Gestion de archivos/chanchito.txt'):
    os.remove('Python/7- Gestion de archivos/chanchito.txt')
else:
    print("El archivo no existe")
# así eleimanos un archivo de manera exitosa.

### eliminar una carpeta
# debemos utilizar la instrucción os.rmdir()     (remove directorio)

# os.rmdir('la ruta de la carpeta')