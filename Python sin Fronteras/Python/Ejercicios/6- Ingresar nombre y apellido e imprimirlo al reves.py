# Ingresar nombre y apellido e imprimirlo al reves.
nombre = input("Escriba el nombre: ")
apellido = input("Escriba el apellido: ")
# concatenamos y damos vuelta
NombreCompleto = nombre + ' ' + apellido¡
# utilizamos funcion que dará vuelta al nombre completo:
print(NombreCompleto[::-1])
# los :: se utilizan con algo llamado slice, sirve en este caso para voltear un string