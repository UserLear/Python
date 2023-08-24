from pathlib import Path
import shutil, os
#1.......copiar archivos y carpetas
p = Path.home() #WindowsPath('C:/Users/DELL_USER_#1')
shutil.copy(p/'saludo.txt', p/'nueva_carpeta') #se crea un archivo que al abrirlo contiene los datos copiados
#shell: WindowsPath('C:/Users/DELL_USER_#1/nueva_carpeta')
shutil.copy(p/'saludo.txt', p/'practica_automatize_python') #se crea un archivo que al abrirlo contiene los datos copiados
#shell: WindowsPath('C:/Users/DELL_USER_#1/practica_automatize_python')
shutil.copy(p/'saludo.txt', p/'desktop/practica_automatize_python') #se hizo una copia del directorio (WindowsPath('C:/Users/DELL_USER_#1')) al directorio 'C:\\Users\\DELL_USER_#1\\desktop\\practica_automatize_python\\saludo.txt' - si ya existe un documento con el mismo nombre solo se sobreescribe
#shell: 'C:\\Users\\DELL_USER_#1\\desktop\\practica_automatize_python\\saludo.txt'

shutil.copy(p/'saludo.txt', p/'desktop/practica_automatize_python/mihistoria.txt') #se hizo una segunda copia cambiando el nombre del documento - si ya existe un documento con el mismo nombre solo se sobreescribe
#shell: WindowsPath('C:/Users/DELL_USER_#1/desktop/practica_automatize_python/mihistoria.txt')

shutil.copytree(p/'varios_archivos', p/'desktop/carpe_copytree') #se crea una carpeta nueva - no puede utilizar una carpeta que ya esta creada
#shell: WindowsPath('C:/Users/DELL_USER_#1/desktop/carpe_copytree')

#2.......mover y cambiar el nombre de archivos y carpetas














