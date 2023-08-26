from pathlib import Path, os, shelve
#LECTURA Y ESCRITURA DE ARCHIVOS
#.......uso Path
#para unir carpetas como un directorio
Path('spam', 'bacon', 'eggs')
#shell: WindowsPath('spam/bacon/eggs')
str(Path('spam', 'bacon', 'eggs'))
#shell: 'spam\\bacon\\eggs'

#.......uso de for
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
        print(Path(r'C:\Users\Al', filename))
#C:\Users\Al\accounts.txt
#C:\Users\Al\details.csv
#C:\Users\Al\invite.docx

#.......uso operador / para unir rutas
Path('spam') / 'bacon' / 'eggs'
#shell: WindowsPath('spam/bacon/eggs')
str(Path('spam') / 'bacon' / 'eggs')
#shell: 'spam\\bacon\\eggs'

Path('spam') / Path('bacon/eggs')
#shell: WindowsPath('spam/bacon/eggs')
str(Path('spam') / Path('bacon/eggs'))
#shell: 'spam\\bacon\\eggs'

Path('spam') / Path('bacon', 'eggs')
#shell: WindowsPath('spam/bacon/eggs')
str(Path('spam') / Path('bacon', 'eggs'))
#shell: 'spam\\bacon\\eggs'

#.......directorio de trabajo actual
Path.cwd()
#shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python')
str(Path.cwd())
#shell: 'C:\\Users\\DELL_USER_#1\\Desktop'

#.......para cambiar de directorio: os.chdir()
Path.cwd()
#shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python')
str(Path.cwd()) #llamamos a la funcion str(Path.cwd()) para obtener una cadena de nuestra ubicacion y pasar una parte a path.chdir()
#shell: 'C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python'

os.chdir('C:\\Users\\DELL_USER_#1\\Desktop\\plazti') 
Path.cwd() 
#shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti')
#python: <bound method Path.cwd of <class 'pathlib.Path'>>

os.chdir(Path.cwd() / Path('platzi/python'))
#FileNotFoundError: [WinError 3] El sistema no puede encontrar la ruta especificada: 'C:\\Users\\DELL_USER_#1\\Desktop\\platzi\\python'

#.......obtener un objeto Path llamando Path.home()
Path.home()
#shell: WindowsPath('C:/Users/DELL_USER_#1')
str(Path.home())
#shell: 'C:\\Users\\DELL_USER_#1'

#.......creacion de nuevas carpetas con os.makedirs(), mkadir()
os.makedirs('C:\\Users\\DELL_USER_#1\\desktop\\delicious\\walnut\\waffles')
#

Path(r'C:\Users\DELL_USER_#1\Desktop\ejemplo2').mkdir()
#shell: WindowsPath('C:\Users\DELL_USER_#1\Desktop\ejemplo2')

#.......manejo de rutas absolutas y relativas
Path.cwd() #shell: WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
#verifica si una ruta es absoluta
Path.cwd().is_absolute() #shell: True
Path('spam/bacon/eggs').is_absolute() #shell: False

#para convertir una ruta relativa en absoluta
Path.cwd() / Path('spam/bacon/eggs') #shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/spam/bacon/eggs')

#devolver una cadena de la ruta absoluta
os.path.abspath('spam/bacon/eggs') #shell: 'C:\\Users\\DELL_USER_#1\\Desktop\\spam\\bacon\\eggs'

#devolver True si el argumento es ruta absoluta y False si es relativa
os.path.isabs('spam/bacon/eggs') #shell: False
os.path.isabs('C:\\Users\\DELL_USER_#1\\Desktop\\spam\\bacon\\eggs') #shell: True
os.path.isabs('C:/Users/Al/AppData/Local/Programs/Python/Python37') #shell: True

#devuelve una cadena de ruta relativa desde la  ruta de inicio hasta la ruta, si no se proporciona la ruta de inicio el directorio de trabajo actual se utiliza como de inicio
#os.path.relpath(path, start)
os.path.abspath('.') #shell: 'C:\\Users\\DELL_USER_#1\\Desktop'
os.path.abspath('.\\automatize_python') #shell: 'C:\\Users\\DELL_USER_#1\\Desktop\\automatize_python'
os.path.isabs('.') #shell: False
os.path.isabs(os.path.abspath('.')) #shell: True

os.path.relpath('C:\\Windows', 'C:\\') #shell: 'Windows'
os.path.relpath('C:\\Windows', 'C:\\spam \\huevos') #shell: '..\\..\\Windows'

#.......obtener las partes de una ruta de archivo como cadenas
#C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/cap6.py
#ancla y unidad: C:/
Path('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/cap6.py').anchor
#shell: 'C:\\'

#padre (carpeta que contiene el archivo): Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python
Path('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/cap6.py').parent
#shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python')

#nombre (compuesto por nombre y extension): practica.py
Path('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/practica.py').name
#shell: 'practica.py'
Path('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/practica.py').stem
#shell: 'practica'
Path('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/practica.py').suffix
#shell: '.py'
Path('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/practica.py').drive
#shell: 'C:'

Path.cwd() #'C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python'
Path.cwd().parents[0] #shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python')
Path.cwd().parents[1] #shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti')
Path.cwd().parents[2] #shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop')
Path.cwd().parents[3] #shell: WindowsPath('C:/Users/DELL_USER_#1')
Path.cwd().parents[4] #shell: WindowsPath('C:/Users')
Path.cwd().parents[5] #shell: WindowsPath('C:/')
Path.cwd().parents[6] #shell: IndexError(idx)

os.path.basename('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\practica.py')
#shell: 'practica.py'
os.path.dirname('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\practica.py')
#shell: 'C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python'

#para obtener el nombre de directorio y en nombre base de una ruta juntos en una tupla
os.path.split('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\practica.py')
#shell: ('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python', 'practica.py')

#para devolver una lista de todas las partes de una ruta como cadena
cadena = 'C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\practica.py'
cadena.split(os.sep)
#shell: ['C:', 'Users', 'DELL_USER_#1', 'Desktop', 'plazti', 'Python', 'automatize_python', 'practica.py']

#.......busqueda de tamaños de archivos en bytes y contenidos de carpetas
os.path.getsize('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\practica.py')
#shell: 62
os.path.getsize('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python')
#shell: 4096

#devolvera una lista de cadenas de nombres de archivos
os.listdir('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python')
#['codigo', 'practica.py', 'proyectos.py', 'proyepython.py', 'prueba']

suma = 0
for individual in os.listdir('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python'):
    suma =+ os.path.getsize('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python')
#shell: 4096 

#.......modificacion de una lista de archivos mediante patrones globales
#para enumerar el contenido de una carpeta deacuerdo a un patron global
p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python')
p.glob('*') #shell: <generator object Path.glob at 0x000001314521C9E0>

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python')
list(p.glob('*'))
#shell: [WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/practica.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/proyectos.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/proyepython.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/prueba')]

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python')
list(p.glob('*.py'))
#shell: [WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/practica.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/proyectos.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/proyepython.py')]

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo')
list(p.glob('cap?.py'))
#shell: [WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap1.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap2.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap3.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap4.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap5.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap6.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap7.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap8.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap9.py')]

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo')
list(p.glob('?ap?.py'))
#shell: [WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap1.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap2.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap3.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap4.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap5.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap6.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap7.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap8.py'), WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python/codigo/cap9.py')]

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo')
for var in p.glob('*.py'):
    print(var)
'''
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap1.py
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap2.py
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap3.py
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap4.py
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap5.py
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap6.py
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap7.py
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap8.py
C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\codigo\cap9.py
'''
#.......comprobacion de validez de ruta
p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo\\cap7.py')
p.exists() #shell: True - verifica si la ruta existe

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo\\cap7.py')
p.is_file() #shell: True - verifica si el archivo existe

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo\\cap7.py')
p.is_dir() #shell: False - verifica si es un puro directorio

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo')
p.is_dir() #shell: True - verifica si es un puro directorio

#se debe crear un archivo de texto plano (bloc de notas .txt) para utilizar el modulo Path, nos instalamos en el directorio donde se ubica el archivo
#idenficicamos nuestro directorio actual
Path().cwd() #WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python')

#cambiamos de directorio para buscar el archivo
os.chdir('C:/Users/DELL_USER_#1/Desktop')
Path().cwd() #WindowsPath('C:/Users/DELL_USER_#1/Desktop')

#una vez creado el documento (.txt) con bloc de notas trazamos la ruta al archivo
p = Path('numero.txt') 
os.path.abspath(p) #shell: 'C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt'
os.path.basename('C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt') #shell: 'numero.txt'

#metodo: read_text() - para leer el archivo
p.read_text() #'13'

#metodo: write_text() - para sobreescribir o crear un nuevo archivo
p.write_text('Hola Mundo') #shell: 10 - devuelve el numero de caracteres añadidos en el documento
p.read_text() #'Hola Mundo'

#.......funcion open(), open(Path, 'w'), open(Path, 'a'), read(), write(), readlines(), close()
#para abrir un archivo le pasa la ruta de cadena que indica el archivo que desea abrir puede ser absoluta o relativa
#funcion open() devuelve un objeto File
Path.cwd() #shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python') - devuelve el objeto del directorio donde estoy posicionado
Path.home() #shell: WindowsPath('C:/Users/DELL_USER_#1') - devuelve el objeto del directorio casa
str(Path.home()) #shell: 'C:\\Users\\DELL_USER_#1' - devuelve una cadena del directorio casa
os.path.abspath('Desktop/numero.txt') #shell: 'C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt'
holaNumero = open(os.path.abspath('Desktop/numero.txt'))
holaNumero = open(Path.home() / 'Desktop/numero.txt') #shell: llamar a la variable devuelve - <_io.TextIOWrapper name='C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt' mode='r' encoding='cp1252'>

holaNumero = open('C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt') #devuelve un objeto File 
#llamar a la variable holaNumero devuelve: <_io.TextIOWrapper name='C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt' mode='r' encoding='cp1252'>

#funcion read() - lee la cadenas que contiene el archito
holaNumero.read() #'Hola Mundo'

#funcion readlines() - devuelve una lista de valores de cadena del archivo de varias lineas
holaCadena = open('C:\\Users\\DELL_USER_#1\\Desktop\\cadenas.txt') 
holaCadena.read() #'la mayoria de\nlas personas\nse quejan de no\ntener el tiempo ni\nla oportunidad de \ncrecer, olvidando que \nsi fuera facil, todo\nel mundo lo haria\n'
holaCadena.readlines() #['la mayoria de,\n', 'las personas,\n', 'se quejan de no,\n', 'tener el tiempo ni,\n', 'la oportunidad de,\n', 'crecer, olvidando que,\n', 'si fuera facil, todo,\n', 'el mundo lo haria,\n']

#funcion open(Path, 'w') - modo escritura sobrescribira el archivo existente o creara uno nuevo
holaNumero = open('C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt', 'w')
holaNumero.write('1234') #shell: 4
holaNumero = open('C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt') #devuelve el objeto File
holaNumero.read() #shell: '1234' 

#funcion open(Path, 'a') - agregara texto al final del archivo existente
holaCadena = open('C:\\Users\\DELL_USER_#1\\Desktop\\cadenas.txt', 'a') #devuelve el objeto File
holaCadena.write('Este es un saludo') #shell: 17 - para poder escribir debe estar el objeto File disponible (llamarlo primero - linea arriba)
holaCadena = open('C:\\Users\\DELL_USER_#1\\Desktop\\cadenas.txt') #devuelve el objeto File
holaCadena.read() #shell: 'la mayoria de,\nlas personas,\nse quejan de no,\ntener el tiempo ni,\nla oportunidad de,\ncrecer, olvidando que,\nsi fuera facil, todo,\nel mundo lo haria,\nEste es un saludo' - para poder leerlo debe estar el objeto File disponible (llamarlo primero - linea arriba)
holaCadena = open('C:\\Users\\DELL_USER_#1\\Desktop\\cadenas.txt') #devuelve el objeto File
holaCadena.readlines() #shell: ['la mayoria de,\n', 'las personas,\n', 'se quejan de no,\n', 'tener el tiempo ni,\n', 'la oportunidad de,\n', 'crecer, olvidando que,\n', 'si fuera facil, todo,\n', 'el mundo lo haria,\n', 'Este es un saludo'] para poder leerlo debe estar el objeto File disponible (llamarlo primero - linea arriba)

#funcion write() para crear un archivo
saludo = open('saludo.txt', 'w') #shell: devuelve un objeto File
saludo.write('Hola muchach \n') #shell: 14 - write() crea un archivo para sobreescribir
saludo.close() #shell: cierra el archivo
saludo = open('saludo.txt', 'a') #shell: devuelve un objeto File
saludo.write('como esta Sr tocino') #shell: 19 - escribe al final del archivo
saludo.close() #shell: cierra el archivo
saludo = open('saludo.txt') ##shell: devuelve un objeto File
saludoLargo = saludo.read() #shell: lee el contenido de la variable saludo
saludo.close() #shell: cierra el archivo saludo
print(saludoLargo)
#Hola muchach 
#como esta Sr tocino

#.......GUARDAR VARIABLES CON MODULO SHELVE
#se ejecuta en el directorio actual
archivoEstante = shelve.open('miDato')
gatos = ['pelusa', 'dino', 'coco']
archivoEstante['misGatos'] = gatos
archivoEstante.close()
#esto crea 3 archivos con extenciones .bak, .dat, .dir

#abrir archivo de estanteria
archivoEstante = shelve.open("miDato")
type(archivoEstante) #<class 'shelve.DbfilenameShelf'>
archivoEstante['misGatos'] #['pelusa', 'dino', 'coco']
archivoEstante.close()

#acceder a valores de estante como diccionarios
archivoEstante = shelve.open('miDato')
list(archivoEstante.keys()) # ['misGatos']
list(archivoEstante.values()) #[['pelusa', 'dino', 'coco']]
archivoEstante.close()
#si se desea guardar datos de los programas de python con modulo shelve
