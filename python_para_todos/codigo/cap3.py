#EJECUCION CONDICIONAL pdf pg 39
#3.1.......expresiones booleanas
x = 4
y = 5
print(x == y) #False
print(x != y) #True
print(x < y) #True
print(x <= y) #True
print(x > y) #False
print(x >= y) #False
print(x is y) #False
print(x is not y) #True

#3.2.......operadores logicos
x1 = 6
y1 = 7
print(x1 >= 0 and x1 <= 10) #True
print((x1*2)%2 == 0 or (y1*3)%2 == 0) #True 
print(not(x1 == y1)) #True

#3.3.......ejecucion condicional
x2 = 5

if x2 <= 10:
    print("este numero es menor que 11")

if x2 > 0:
    pass #esto permite terminar luego

#3.4.......ejecucion alternativa
if x2%2 == 0:
    print("es un numero par")
else:
    print("no es un numero par")

#3.5......condicionales endadenados
if x < y:
    print('x es menor que y')
elif x > y:
    print('x es mayor que y')
else:
    print('x e y son iguales')

#3.6......condicionales anidados
if x == y:
    print('x e y son iguales')
else:
    if x < y:
        print('x es menor que y')
    else:
        print('x es mayor que y')

#3.7.....captura de excepciones usando try y except
ent = input('Introduzca la Temperatura Fahrenheit:')
try:
    fahr = float(ent)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Por favor, introduzca un número')


#3.8......evaluacion en cortocircuito de expresiones logicas
x = 6
y = 2
x >= 2 and (x/y) > 2 #True
x = 1
y = 0
x >= 2 and (x/y) > 2 #False
x = 6
y = 0
x >= 2 and (x/y) > 2
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#ZeroDivisionError: division by zero

#3.9.....depuracion
import math
int_senal = 9
int_ruido = 10
relacion = int_senal / int_ruido
decibelios = 10 * math.log10(relacion)
print(decibelios)

#Traceback (most recent call last):
#File "snr.py", line 5, in ?
#decibelios = 10 * math.log10(relacion)
#OverflowError: math range error







