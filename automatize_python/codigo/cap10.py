from pathlib import Path
import shutil, os
#ORGANIZANDO ARCHIVOS
#1.......copiar archivos y carpetas
#al buscar en el directorio Path.home() en el disco
p = Path.home() #WindowsPath('C:/Users/DELL_USER_#1')
#para hacer una copia del archivo: el primer argumento es la cadena directorio donde se ubica el archivo + el nombre del archivo, la segunda cadena si la carpeta no existe
#el modulo utiliza la cadena nombre como el nuevo nombre del documento y lo crea como archivo sin formato.
shutil.copy(p/'saludo.txt', p/'nueva_carpeta') 
#shell: WindowsPath('C:/Users/DELL_USER_#1/nueva_carpeta')
shutil.copy(p/'saludo.txt', p/'practica_automatize_python') #se crea un archivo que al abrirlo contiene los datos copiados
#shell: WindowsPath('C:/Users/DELL_USER_#1/practica_automatize_python')
shutil.copy(p/'saludo.txt', p/'desktop/practica_automatize_python') 
#si la carpeta existe se hace una copia del directorio (WindowsPath('C:/Users/DELL_USER_#1')) al directorio 'C:\\Users\\DELL_USER_#1\\desktop\\practica_automatize_python\\saludo.txt' - si ya existe un documento con el mismo nombre solo se sobreescribe
#shell: 'C:\\Users\\DELL_USER_#1\\desktop\\practica_automatize_python\\saludo.txt'

shutil.copy(p/'saludo.txt', p/'desktop/practica_automatize_python/mihistoria.txt') #se hizo una segunda copia cambiando el nombre del documento - si ya existe un documento con el mismo nombre solo se sobreescribe
#shell: WindowsPath('C:/Users/DELL_USER_#1/desktop/practica_automatize_python/mihistoria.txt')

#la carpeta 'varios_archivos' que contiene varios archivos se ubica en el directorio (WindowsPath('C:/Users/DELL_USER_#1')) al utilizar la funcion se copio todo al directorio 'C:\\Users\\DELL_USER_#1\\desktop\\practica_automatize_python' 
shutil.copytree(p/'varios_archivos', p/'desktop/carpe_copytree') #se crea una carpeta nueva - no puede utilizar una carpeta que ya esta creada
#shell: WindowsPath('C:/Users/DELL_USER_#1/desktop/carpe_copytree')

#2.......mover y cambiar el nombre de archivos y carpetas
#mover carpetas o archivos con objetos Path
#ejemplo: en desktop se ubica la carpeta ejemplos la vamos a mover a practica_automatize_python
p = Path.home() #shell: WindowsPath('C:/Users/DELL_USER_#1')
#mover una carpeta 
shutil.move(p/'desktop/ejemplos', p/'desktop/practica_automatize_python') #devolvera una cadena de la ruta donde movimos el archivo o carpeta - shell: 'C:\\Users\\DELL_USER_#1\\desktop\\practica_automatize_python\\ejemplos' 

#mover carpetas o archivos con cadenas de rutas
#ejemplo: creo un documento .txt en 'C:/Users/DELL_USER_#1/desktop/practica_automatize_python/ejemplos' para moverlo a una carpeta
shutil.move(Path('C:/Users/DELL_USER_#1/desktop/practica_automatize_python/ejemplos/documento_prueba.txt'), Path('C:/Users/DELL_USER_#1/desktop')) #shell: 'C:\\Users\\DELL_USER_#1\\desktop\\documento_prueba.txt'

#3.......eliminar archivo y carpetas permanentemente
#para eliminar un archivo o carpeta vacia
#ejemplo eliminar archivo: en desktop existe un archivo documento_prueba.txt que eliminaremos
os.unlink(p/'desktop/documento_prueba.txt') #funciono

#ejemplo elimiar carpeta: en desktop/practica_automatize_python existe carpeta 'nueva carpeta' para eliminar
os.rmdir(p/'desktop/practica_automatize_python/nueva carpeta') #funciono

#ejemplo eliminar carpeta con archivos: en desktop/practica_automatize_python exite carpeta 'ejemplos' para eliminar carpeta e4
shutil.rmtree(p/'desktop/practica_automatize_python/ejemplos/e4') #funciono
