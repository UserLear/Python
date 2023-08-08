from pathlib import Path, os
#.......funcion open(), open(Path, 'w'), open(Path, 'w'),  read(), write(), readlines(), close()
#para abrir un archivo le pasa la ruta de cadena que indica el archivo que desea abrir puede ser absoluta o relativa
#funcion open() devuelve un objeto File
Path.cwd() #shell: WindowsPath('C:/Users/DELL_USER_#1/Desktop/plazti/Python/automatize_python') - devuelve el objeto del directorio donde estoy posicionado
Path.home() #shell: WindowsPath('C:/Users/DELL_USER_#1') - devuelve el objeto del directorio casa
str(Path.home()) #shell: 'C:\\Users\\DELL_USER_#1' - devuelve una cadena del directorio casa

holaNumero = open('C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt') #devuelve un objeto File 
#llamar a la variable holaNumero devuelve: <_io.TextIOWrapper name='C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt' mode='r' encoding='cp1252'>

#funcion read() - lee la cadenas que contiene el archito
holaNumero.read() #'Hola Mundo'

#funcion readlines() - devuelve una lista de valores de cadena del archivo
holaCadena = open('C:\\Users\\DELL_USER_#1\\Desktop\\cadenas.txt') 
holaCadena.read() #'la mayoria de\nlas personas\nse quejan de no\ntener el tiempo ni\nla oportunidad de \ncrecer, olvidando que \nsi fuera facil, todo\nel mundo lo haria\n'
holaCadena.readlines() #['la mayoria de,\n', 'las personas,\n', 'se quejan de no,\n', 'tener el tiempo ni,\n', 'la oportunidad de,\n', 'crecer, olvidando que,\n', 'si fuera facil, todo,\n', 'el mundo lo haria,\n']

#funcion open(Path, 'w') - modo escritura sobrescribira el archivo existente
holaNumero = open('C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt', 'w')
holaNumero.write('1234') #shell: 4
holaNumero = open('C:\\Users\\DELL_USER_#1\\Desktop\\numero.txt') #devuelve el objeto File
holaNumero.read() #shell: '1234' 

#funcion open(Path, 'a') - agregara texto al final del archivo existente
holaCadena = open('C:\\Users\\DELL_USER_#1\\Desktop\\cadenas.txt', 'a')
holaCadena.write('Este es un saludo') #shell: 17 
holaCadena = open('C:\\Users\\DELL_USER_#1\\Desktop\\cadenas.txt') #devuelve el objeto File
holaCadena.read() #shell: 'la mayoria de,\nlas personas,\nse quejan de no,\ntener el tiempo ni,\nla oportunidad de,\ncrecer, olvidando que,\nsi fuera facil, todo,\nel mundo lo haria,\nEste es un saludo'
holaCadena = open('C:\\Users\\DELL_USER_#1\\Desktop\\cadenas.txt') #devuelve el objeto File - es necesario llamar de nuevo para la funcion readline()
holaCadena.readlines() #shell: ['la mayoria de,\n', 'las personas,\n', 'se quejan de no,\n', 'tener el tiempo ni,\n', 'la oportunidad de,\n', 'crecer, olvidando que,\n', 'si fuera facil, todo,\n', 'el mundo lo haria,\n', 'Este es un saludo']






