#ALCANCE DE LAS VARIABLES
#.......alcance local
def myfun():
    a = 0  # Variables locales
    a += 1
    print("myfun a = ", a)

def myfun2():
    a = [1, 2, 3] # Variables locales
    a = [i + 1 for i in a]
    print("myfun2  a = ", a)

a = 'Hello Python'  # Donde a es una variable global
myfun()
myfun2()
print("Fuera de la función a =", a)

#Resultado de salida:
#myfun a =  1
#myfun2  a =  [2, 3, 4]
#Fuera de la función a =  Hello Python

#.......alcance anidado
# 1. Función de anidación:
def myfun(i):
    a = [1, 2, 3] # a está en un ámbito anidado
    def add():
        a.append(i)
        return a
    return add
test = myfun(4)
print(test())
#Resultado de salida:[1, 2, 3, 4]

# 2. La clase contiene múltiples funciones
class test:
    b = 1
    def __init__(self):
        self.a = 0
    def myfun2(self):
        self.a += 1
        print("a = ", self.a)
        self.b += 1
        print("b = ", self.b)
test = test()
test.myfun2()

#Resultado de salida:
#a =  1
#b =  2

#.......alcance global
# No se pueden cambiar enteros, cadenas, etc.
a = 1  # a es una variable global

def myfun():
    a = 2  # Variables locales
    a += 1
    print("En la función a =", a)

myfun()
print("Fuera de la función a =", a)

#Resultado de salida:
#En la función a =  3
#Fuera de la función a =  1

# Listas, tuplas, etc. se pueden cambiar
a = [1, 2, 3]
b = {'Idioma': 98, "matemáticas": 101}

def myfun():
    a.append(4)
    b.update({"Inglés": 103})
    print("En la función a =", a)
    print("En la función b =", b)


myfun()
print("Fuera de la función a =", a)
print("Función externa b =", b)

#Resultado de salida:
#En la función a =  [1, 2, 3, 4]
#En la función b =  {'Idioma': 98, 'matemáticas': 101, 'Inglés': 103}
#Fuera de la función a =  [1, 2, 3, 4]
#Función exterior b =  {'Idioma': 98, 'matemáticas': 101, 'Inglés': 103}

# Use palabras clave globales para hacer referencia a variables globales
a = 1

def myfun():
    global a  # Use global antes de usar un
    a += 1
    print("En la función a =", a)

myfun()
print("Fuera de la función a =", a)

#Resultado de salida:
#En la función a =  2
#Fuera de la función a =  2