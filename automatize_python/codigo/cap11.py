from pathlib import Path
import traceback
#DEPURACION
#2.......obtener seguimiento como una cadena
def boxPrint(simbolo, ancho, alto):
    if len(simbolo) != 1:
        raise Exception('El simbolo debe ser una cadena de un solo caracter.')
    if ancho <= 2:
        raise Exception('El ancho debe ser mayor que 2.')
    if alto <= 2:
        raise Exception('la altura debe ser mayor que 2.')

    print(simbolo * ancho)
    for i in range(alto - 2):
        print(simbolo + (' ' * (ancho - 2)) + simbolo)
    print(simbolo * ancho)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('Ocurrio una excepcion: ' + str(err))

#2.......obtener seguimiento como una cadena
'''util para mantener el programa en ejecucion y evitar que se detenga ante el error, 
tambien permite guardar el error como cadena en un archivo de texto para verlo mas tarde, 
para esto hay que importar el modulo traceback
'''
def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()

#Traceback (most recent call last):
#  File "C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\practica.py", line 14, in <module>
#    spam()
#  File "C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\practica.py", line 9, in spam
#    bacon()
#  File "C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\practica.py", line 12, in bacon
#    raise Exception('This is the error message.')
#Exception: This is the error message.


p = Path.home()
try:
    def spam():
        bacon()
    def bacon():
        raise Exception('This is the error message.')
    spam()
except: 
    errorArchivo = open(p/'errorInfor.txt', 'w')
    errorArchivo.write(traceback.format_exc())
    errorArchivo.close()
    print('La informacion de rasteo se escribio en errorInfor.txt')

#3.......afirmaciones
#una afirmacion es una verificacion de cordura para asegurarse que su codigo no este haciendo algo obviamente incorrecto
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages #[15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
assert ages[0] <= ages[-1] 
#este codigo no hace nada puesto que la condicion es verdadera

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
ages #[73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
assert ages[0] <= ages[-1] 
#Traceback (most recent call last):
#  File "C:\Users\DELL_USER_#1\Desktop\plazti\Python\automatize_python\practica.py", line 12, in <module>
#    assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.
#AssertionError

























