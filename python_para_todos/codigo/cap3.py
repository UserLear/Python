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

#EJERCICIOS DEL CAPITULO
#Ejercicio # 0
#programa que calcula el ingreso de un trabajador por hora
horas = input("Introduzca las horas: ")
tarifaHoras = 1.5

pagoTotal = int(horas) * tarifaHoras
print("Tu ingreso laboral es: Lps " + str(pagoTotal))

#Ejercicio # 1
#programa que calcula el ingreso de un trabajador de una empresa que tiene un horario de trabajo y horas extra
horas = input("Introduzca las horas: ")
tarifaNormal = 1.0
tarifaExtra = 1.5
numero = int(horas)
if numero > 0 and numero <= 40:
    pagoTotal = numero * tarifaNormal
    print("Tus " + str(numero) + " horas trabajadas corresponden a $ " + str(pagoTotal))
else: 
    horasNormales = 40 * tarifaNormal
    horasExtra = (numero - 40) * tarifaExtra
    pagoTotal = horasNormales + horasExtra
    print("Tus " + str(numero) + " horas trabajadas corresponden a $ " + str(pagoTotal))

#Ejercicio # 2
#programa que gestiona entradas no numericas que pueden generar un error utilizando try y except
try:
    horas = input("Introduzca las horas: ")
    tarifaNormal = 1.0
    tarifaExtra = 1.5
    numero = int(horas)
    if numero > 0 and numero <= 40:
        pagoTotal = numero * tarifaNormal
        print("Tus " + str(numero) + " horas trabajadas corresponden a $ " + str(pagoTotal))
    else: 
        horasNormales = 40 * tarifaNormal
        horasExtra = (numero - 40) * tarifaExtra
        pagoTotal = horasNormales + horasExtra
        print("Tus " + str(numero) + " horas trabajadas corresponden a $ " + str(pagoTotal))
except: 
    print("Por favor introduce un numero")

#Ejercicio # 3
#programa que devuelve un nivel ordinal en relacion a una calificacion obtenida
try:
    calificacion = input("Introduce tu calificacion: ")
    convertir = float(calificacion)
    if convertir >= 0.0 and convertir < 0.6:
        print("Insuficiente")
    elif convertir >= 0.6 and convertir < 0.7:
        print("Suficiente")
    elif convertir >= 0.7 and convertir < 0.8:
        print("Bien")
    elif convertir >= 0.8 and convertir < 0.9: 
        print("Notable")
    elif convertir >= 0.9 and convertir <= 1.0:
        print("Sobresaliente")
    else: 
        print("Debe haber algun error no puedes tener menos de 0.0 o mas de 1.0")
except:
    print("debes introducir un numero entre 0.0 y 1.0")









