#.......definicion de funcion
def hola():
    print('Hola!')
    print('Hola!!!')
    print('Hola.')

#.......llamada de la funcion
hola()

#.......funciones con parametros
def hola(nombre):
    print('Hola, ' + nombre)

print(hola('Alice'))
print(hola('Bob'))

#.......valor de retorno + declaracion de retorno
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Es cierto'
    elif answerNumber == 2:
        return 'Decididamente es así'
    elif answerNumber == 3:
        return 'Sí'
    elif answerNumber == 4:
        return 'Responder nebuloso inténtalo de nuevo'
    elif answerNumber == 5:
        return 'Preguntar de nuevo más tarde'
    elif answerNumber == 6:
        return 'Concéntrate y preguntar de nuevo'
    elif answerNumber == 7:
        return 'Mi respuesta es no'
    elif answerNumber == 8:
        return 'Perspectiva no tan buena'
    elif answerNumber == 9:
        return 'Muy dudoso'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

print(getAnswer(random.randint(1, 9)))

#.......argumentos de palabras clave y la funcion print()
print('Hello', end='')
print('World')
#HelloWorld

print('cats', 'dogs', 'mice', sep=',')
#cats,dogs,mice

#.......pila de llamadas
def a():
    print('a() comienza')
    b()
    d()
    print('a() regresa')

def b():
    print('b() comienza')
    c()
    print ('b() regresa')

def c():
    print('c() comienza')
    print('c() regresa')

def d():
    print('d() comienza')
    print('d () devuelve')

a()

#a() starts
#b() starts
#c() starts
#c() returns
#b() returns
#d() starts
#d() returns
#a() returns

#.......alcance local y global
valor = 2 #ambito global

def aumento(a):
    return valor + a #ambito local

print(aumento(3)) #5
print(valor) #2


