from pathlib import Path, os
#LECTURA Y ESCRITURA DE ARCHIVOS
#.......uso Path
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

#.......uso operador / para unit rutas
print(Path('spam') / 'bacon' / 'eggs')
#WindowsPath('spam/bacon/eggs')
print(Path('spam') / Path('bacon/eggs'))
#WindowsPath('spam/bacon/eggs')
print(Path('spam') / Path('bacon', 'eggs'))
#WindowsPath('spam/bacon/eggs')

#.......directorio de trabajo actual
print(Path.cwd()) #directorio actual
#shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python')
os.chdir("C:\\Users\\DELL_USER_#1\\Desktop\\plazti") #para cambiar de directorio
print(Path.cwd) #shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti')
#<bound method Path.cwd of <class 'pathlib.Path'>>

#.......obtener un objeto Path llamando Path.home()
Path.home()
#shell: WindowsPath('C:/Users/DELL_USER_#1')

#.......creacion de nuevas carpetas con os.makedirs(), mkadir()
os.makedirs('C:\\Users\\DELL_USER_#1C:\\desktop\\delicious\\walnut\\waffles')
#acceso denegado

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
p.exists() #shell: True

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo\\cap7.py')
p.is_file() #shell: True

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo\\cap7.py')
p.is_dir() #shell: False

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo')
p.is_dir() #shell: True

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


