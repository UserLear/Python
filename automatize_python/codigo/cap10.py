from pathlib import Path
import shutil, os, send2trash, zipfile
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

send2trash.send2trash('ar_prueba_send2trash.txt') #para que este funcione correctamente debe estar ubicado en el directorio del documento
send2trash.send2trash(p/'Desktop/ar_prueba_send2trash.txt') #devuelve error

#5.......caminando por un arbol de directorios
p = Path.home()
for folderName, subfolders, filenames in os.walk(p/'desktop/practica_automatize_python'):
    print('La carpeta actual es ' + folderName)

    for subfolder in subfolders:
        print('Subcarpeta de ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('Archivo dentro ' + folderName + ': '+ filename)

    print('')

#6.......comprimir archivos con el modulo zipfile
p = Path.home()
#al crear los archivos zip existe una diferencia entre crearlo con la carpeta que contiene todos los archivos o crearlo directamente con los archivos
#ejemplo 1: se crea con la carpeta que contiene todos los archivos
ejemplozip1 = zipfile.ZipFile(p/'desktop/practica_automatize_python1.zip') #el archivo se debe crear antes para poder crear un objeto zip - creamos un objeto zip para poder utilizar los metodos
ejemplozip1.namelist() #un objeto ZipFile tiene un metodo namelist() - shell: ['practica_automatize_python/', 'practica_automatize_python/ejemplos/', 'practica_automatize_python/ejemplos/e1/', 'practica_automatize_python/ejemplos/e2/', 'practica_automatize_python/ejemplos/e2/cito1.jpg', 'practica_automatize_python/ejemplos/e2/citologia.jpg', 'practica_automatize_python/ejemplos/e3/', 'practica_automatize_python/ejemplos/e3/mclip.py', 'practica_automatize_python/ejemplos/e3/pip', 'practica_automatize_python/mihistoria.txt', 'practica_automatize_python/saludo.txt']

#pasamos al metodo getinfo() el objeto ZipFile para que nos devuelvan un objeto ZipInfo y asi usar otros metodos, genera informacion solo de un solo archivo del archivo
informacionzip1 = ejemplozip1.getinfo('practica_automatize_python/saludo.txt') #se debe pasar el valor igual a como sale en la lista superior 
informacionzip1.file_size #shell: 34 - funcion print(): <ZipInfo filename='practica_automatize_python/saludo.txt' compress_type=deflate external_attr=0x20 file_size=34 compress_size=36>

#si pasamos al metodo getinfo() una carpeta nos devuelve un error
informacionzip2 = ejemplozip1.getinfo('practica_automatize_python') #le pasamos el nombre de la carpeta - shell: no hay ningun elemento llamado 'practica_automatize_python2.zip' en el archivo

#si pasamos al metodo getinfo() una carpeta con la diagonal que identifica una carpeta
informacionzip3 = ejemplozip1.getinfo('practica_automatize_python/') 
informacionzip3.file_size #no devuelve el tamaño de carpetas - shell: 0 

#ejemplo 2: se crea seleccionando los archivos y creando el archivo zip
ejemplozip2 = zipfile.ZipFile(p/"desktop/practica_automatize_python2.zip") #el archivo se debe crear antes para poder crear un objeto zip - creamos un objeto zip para poder utilizar los metodos
ejemplozip2.namelist() #un objeto ZipFile tiene un metodo namelist() - shell: ['saludo.txt', 'ejemplos/', 'ejemplos/e1/', 'ejemplos/e2/', 'ejemplos/e2/cito1.jpg', 'ejemplos/e2/citologia.jpg', 'ejemplos/e3/', 'ejemplos/e3/mclip.py', 'ejemplos/e3/pip', 'mihistoria.txt']

#pasamos al metodo getinfo() el objeto ZipFile para que nos devuelvan un objeto ZipInfo y asi usar otros metodos, genera informacion solo de un solo archivo del archivo
informacionzip4 = ejemplozip2.getinfo('saludo.txt') #se debe pasar el valor igual a como sale en la lista superior 
informacionzip4.file_size #shell: 34 - funcion print(): <ZipInfo filename='practica_automatize_python/saludo.txt' compress_type=deflate external_attr=0x20 file_size=34 compress_size=36>

#si pasamos al metodo getinfo() una carpeta nos devuelve un error
informacionzip5 = ejemplozip2.getinfo('ejemplo') #shell: no hay ningun elemento llamado 'ejemplo' en el archivo

#si pasamos al metodo getinfo() una carpeta con la diagonal que identifica una carpeta
informacionzip6 = ejemplozip2.getinfo('ejemplos/')
informacionzip6.file_size #no devuelve el tamaño de carpetas - shell: 0 

#si comprimimos el archivo saludo.tx
informacionzip4.compress_size #shell: 36

#7.......extraer archivos zip
p = Path.home()
extraccion = zipfile.ZipFile(p/'desktop/practica_automatize_python2.zip')
extraccion.extractall('carpeta extraccion') #extrae en el direccotiro de trabajo actual, la cadena pasa a extractall() es la carpeta donde se descomprimiran los documentos
extraccion.close()

extraccion.extract('saludo.txt') #para extraer un archivo especifico - shell: 'C:\\Users\\DELL_USER_#1\\saludo.txt'
extraccion.extract('saludo.txt', 'C:\\Users\\DELL_USER_#1\\desktop\\saludo') #el segundo argumento es el direcctorio de donde queremos que el archivo se descargue

#8.......crear y agregar archivos zip
p = Path.home()
extraccion = zipfile.ZipFile(p/'desktop/nuevozip.zip', 'w') #nuevozip.zip representa el nombre del documento zip que se creara
extraccion.write('saludo.txt', compress_type=zipfile.ZIP_DEFLATED) #este busca el archivo en el direcctorio de trabajo actual, borrara el documento zip si contiene algunos archivos y agregara el nuevo
extraccion.close() #hay que cerrar el documento para poder abrirlo

#para añadir un nuevo archivo al documento zip
extraccion = zipfile.ZipFile(p/'desktop/nuevozip.zip', 'a') #para añadir al zip que ya existe
extraccion.write('saludo - copia.txt', compress_type=zipfile.ZIP_DEFLATED)
extraccion.close() #hay que cerrar el documento para poder abrirlo