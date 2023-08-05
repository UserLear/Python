from pathlib import Path, os
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












        







