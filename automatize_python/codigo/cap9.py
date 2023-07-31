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





