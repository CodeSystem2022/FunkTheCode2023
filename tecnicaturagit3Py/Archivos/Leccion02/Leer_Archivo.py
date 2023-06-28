#: las letras son: 'r', 'a', 'w', 'x'
# 'r': read / 'a': append / 'w': read/ 'x': exception
archivo = open('prueba.txt', 'r', encoding='utf8') #utf8: es un juego de caracteres que soporta los acentos
# print(archivo.read())
# la letra a abre un archivo para anexar más información y crea el archivo en el caso de que no exista
# print(archivo.read(16))
# print(archivo.read(10)) #Continuamos desde la línea anterior desde el siguiente print
# print(archivo.readline()) #Lee la línea
# print(archivo.readline())

# vamos a iterar el archivo, cada una de las líneas
# for linea in archivo:
    # print(linea): iteramos todos los elementos del archivo
# print(archivo.readlines()[11]) #accedemos al archivo como si fuera una lista

# ANEXAMOS INFORMACIÓN, COPIAMOS A OTRO
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()# cerramos el primer archivo
archivo2.close()# cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')
