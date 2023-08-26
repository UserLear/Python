from pathlib import Path
import shutil, os, send2trash
#4.......eliminaciones seguras con modulo send2trash
#ejemplo: crear un archivo, escribir, añadir mas datos en el,  y ejecutar el modulo send2trash  
p = Path.home() #llamamos el directorio casa
p1 = open(p/'desktop/ar_prueba_send2trash.txt', 'w') #paso 1: crea un nuevo archivo en desktop para probar el modulo send2trash, utilizamos la funcion open(ruta-destino/nombrearchivo-extencion, 'w') para crear un nuevo documento,
p1.write('Esta es una prueba completa de crear y eliminar') #paso 2: escribir algo en el archivo - shell: 47
p1 = open(p/'desktop/ar_prueba_send2trash.txt') #paso 3: volver a llamarlo para poder leerlo
p1.read() #paso 4: leer el contenido del archivo - shell: 'Esta es una prueba completa de crear y eliminar'

p1 = open(p/'desktop/ar_prueba_send2trash.txt', 'a') #paso 5: llamar al objeto file para añadir mas datos al final del archivo
p1.write(', esto se añadira al final del documento') #paso 6: añadir mas datos al final - shell: 40
p1 = open(p/'desktop/ar_prueba_send2trash.txt') #paso 7: volver a llamarlo para poder leerlo
p1.read() #paso 8: leer el contenido del archivo - shell: 'Esta es una prueba completa de crear y eliminar, esto se añadira al final del documento'
p1.close() #paso 9: cerramos el documento

send2trash.send2trash('ar_prueba_send2trash.txt')














