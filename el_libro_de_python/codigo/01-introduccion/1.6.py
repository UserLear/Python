#.......condicionales: if, elif, else
lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print("No me gusta, Java no mola")
else:
    print("Ningún otro lenguaje supera a Python")

# Salida: Estoy de acuerdo, Python es el mejor

#.......bucles: while, for, break, continue
x = 0
while x < 3:
    print(x)
    x += 1

# Salida: 0, 1, 2

for i in range(3):
    print(i)

# Salida: 0, 1, 2

for i in range(3):
    if i == 1:
        continue
    print(i)

# Salida: 0, 2

#.......booleans: False, True, None
x = (5 == 1)
print(x)
# Salida: False

x = True
if x:
    print("Python!")
    
# Salida: Python!

def mi_funcion():
    pass

print(mi_funcion())
# Salida: None

#.......operadores logicos: and, or, not
print(True and False) # False
print(True or False)  # True
print(not True)       # False

#.......funciones: def, return, lambda, pass, yield
def funcion_suma(a, b):
    print("La suma es", a + b)
funcion_suma(3, 5)
# Salida: La suma es 8

def funcion_suma(a, b):
    return a + b
suma = funcion_suma(3, 5)
print("La suma es", suma)
# Salida: La suma es 8

print("La suma es", (lambda a, b: a + b)(3, 5))
# Salida: La suma es 8

def funcion_suma(a, b):
    pass

def generador():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n
for i in generador():
    print(i)
# Salida: 1, 2, 3

#.......clases: class
class MiClase:
    def __init__(self):
        print("Creando objeto de MiClase")
objeto = MiClase()
# Salida: Creando objeto de MiClase

#.......excepciones: assert, try, except, finally, raise
x = "10"
valor = None
try:
    valor = int(x)
except Exception as e:
    print("Hubo un error:", e)
finally:
    print("El valor es", valor)
# Salida: El valor es 10

#.......variables: global, nonlocal
a = 0
def suma_uno():
    global a
    a = a + 1
suma_uno()
print(a)
# Salida: 1

def funcion_a():
    x = 10
    def funcion_b():
        nonlocal x
        x = 20
        print("funcion_b", x)
    funcion_b()
    print("funcion_a", x)
funcion_a()
# Salida:
# funcion_b 20
# funcion_a 2

#.......modulos: from, import
from collections import namedtuple
#esto significa: de collections importa namedtuple

#.......pertenencia e identidad: in, is
lista = ["a", "b", "c"]
print("a" in lista)
# Salida: True

a = [1, 2]
b = [1, 2]
c = a
print(a is b) # False
print(a is c) # True

#.......eliminar variables: del
a = 10
del a
print(a)
# Salida: NameError: name 'a' is not defined

#.......gestores de contexto: with, as
with open('fichero.txt', 'r') as file:
    print(file.read())

#.......concurrencia: async, await
import asyncio
async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(10)
    print("Acaba proceso:", id_proceso)
async def main():
    await asyncio.gather(proceso(1), proceso(2), proceso(3))
asyncio.run(main())
# Salida:
# Empieza proceso: 1
# Empieza proceso: 2
# Empieza proceso: 3
# Acaba proceso: 1
# Acaba proceso: 2
# Acaba proceso: 3







