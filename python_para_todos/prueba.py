#Ejercicio 0
#programa que calcula el ingreso de un trabajador por hora
"""horas = input("Introduzca las horas: ")
tarifaHoras = 1.5

pagoTotal = int(horas) * tarifaHoras
print("Tu ingreso laboral es: Lps " + str(pagoTotal))
"""
#Ejercicio 1
#programa que calcula el ingreso de un trabajador de una empresa que tiene un horario de trabajo y horas extra
horas = input("Introduzca las horas: ")
tarifaNormal = 1.0
tarifaExtra = 1.5
numero = int(horas)
if numero > 0 and numero <= 40:
    pagoTotal = numero * tarifaNormal
    print("Tus " + str(numero) + " trabajadas corresponden a $ " + str(pagoTotal))
else: 
    horasNormales = 40 * tarifaNormal
    horasExtra = (numero - 40) * tarifaExtra
    pagoTotal = horasNormales + horasExtra
    print("Tus " + str(numero) + " trabajadas corresponden a $ " + str(pagoTotal))



