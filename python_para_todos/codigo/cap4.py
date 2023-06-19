#4.1......llamadas a funciones
print(type(32))

#4.2......funciones internas
print(max([2, 8, 4, 25, 12]))
print(min("hace un tiempo que espero"))
print(max("hace un tiempo que espero"))
print(len('la palabra'))

#4.3......funciones de conversion de tipos
print(int("34"))
print(float(5))
print(str(45))

#4.4.....funciones matematicas
import math
print(dir(math))
print(math)

int_senal = 25
int_ruido = 10
relacion = int_senal / int_ruido
decibelios = 10 * math.log10(relacion)
print(decibelios)
radianes = 0.7
altura = math.sin(radianes)
print(altura)

grados = 45
radianes = grados / 360.0 * 2 * math.pi
resul = math.sin(radianes)
print(resul)

#4.5......nuemeros aleatorios
import random
print(dir(random))

for i in range(10):
    x = random.random()
    print(x) #genera 10 numero de entre 0.0 y 1.0

print(random.randint(5,10))
print(random.randint(5,10))

t = [1, 2, 3]
print(random.choice(t))
print(random.choice(t))

#4.6......andiendo funciones nuevas
def muestra_estribillo():
    print('Soy un leñador, qué alegría.')
    print('Duermo toda la noche y trabajo todo el día.')

def repite_estribillo():
    muestra_estribillo()
    muestra_estribillo()

#4.7......definicion y usos
#4.8......flujo de ejecucion
#4.9......parametros y argumentos
def muestra_dos_veces(bruce):
    print(bruce)
    print(bruce)

muestra_dos_veces("hola")
muestra_dos_veces('Spam '*4)
muestra_dos_veces(math.cos(math.pi))
michael = 'Eric, la medio-abeja.'
muestra_dos_veces(michael)

#4.10......funciones productivas y funciones esteriles
#4.11......porque funciones
#4.12......depuracion












