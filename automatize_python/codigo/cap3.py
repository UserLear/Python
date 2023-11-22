import random, time, sys
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

#.......declaracion global
n = 25
def modifi():
    global n
    n = 40
    print(n)

modifi() #40
print(n) #40

m = 10
def modifi2():
    global m
    m = 20
    print(m)

print(m) #10
modifi2() #20 mientras no se llame a la funcion la variable no se actualiza
print(m) #20

#.......manejo de excepciones
def spam(divideBy):
    return 42 / divideBy
print(spam(2))
print(spam(12))
#print(spam(0)) este produce un error
print(spam(1))

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Argumento inválido.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam( 1))

#.......zig zag
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()   











