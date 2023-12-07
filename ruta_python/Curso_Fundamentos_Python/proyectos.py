import random
#1. concatenar datos a una plantilla: presentacion, 
#2. piedra papel o tijera
#3. zig zag
#4. generacion de un presupuesto
#5. calcular el dia de nacimiento de una persona
#6. calcular un promedio: notas, ventas
#7. calculo de temperatura farenheit o celcius
#8. convertidor de sistema de medidas
#9. convertidor de numeros en letras
#10. calcular la tasa impositiva de pago de impuesto para personas naturales
#11. calculo de la balanza de comprobacion (contabilidad)
#12. programa convertidor de tipos que explique el uso de cada tipo de dato

#1. creacion de plantillas literales
print("Hola extraño introduce tus datos")
nombre = input("Introduce tu nombre: \n")
print("Hola {} es un gusto conocerte como te apellidas".format(nombre))
apellido = input("Introduce tu apellido: \n")
print(f"Oh! {apellido} vaya tienes un apellido interesante {nombre} ahora dinos que edad tienes")
edad = input("Introduce tu edad: \n")
nueva_edad = str(int(edad)+1)
print("Que maravilla %s aprenderas a programar en tus %s años cuanto tengas %s años ya lo habras logrado" %(nombre, edad, nueva_edad))

#6. programa que calcula el promedio de ventas 
def conj_ingresos(*arg):
    ventas_totales = 0
    for i in arg:
        ventas_totales += i
    valores = len(arg)
    promedio_ventas = ventas_totales / valores
    return promedio_ventas
        
ventas = conj_ingresos(45000, 20000, 13000, 25000)
print(ventas)

suma = 0
valores = 0
while True:
    valor = input("Introduce el ingreso: ")
    try:
        valores += 1
        convertir = int(valor)
        suma += convertir
    except:
        if valor == "c":
            valores -=1
            promedio = suma / valores
            print(promedio)
            break

#6. crear un registro para ventas y gastos que permita calcular ganancias
ventas = {}
gastos = {}
ganancias = {}


#10. calculo de una tasa impositiva en relacion a un salario mensual
def impuesto_sr(salario):
    if salario >= 0.01 and salario <= 19919.96:
        return "Exento"
    elif salario >= 19919.17 and salario <= 28624.99:
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 199039.48
        impuesto = monto_gravable * 0.15
        monto = round(impuesto, 2)
        return monto
    elif salario >= 28625.00 and salario <= 62151.15:
        monto_impuesto_15 = 303499.9 - 199039.48 
        impuesto_15 = monto_impuesto_15 * 0.15
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 303499.91
        impuesto = monto_gravable * 0.20
        monto = round(impuesto + impuesto_15, 2)
        return monto
    else: 
        monto_impuesto_15 = 303499.9 - 199039.48 
        impuesto_15 = monto_impuesto_15 * 0.15
        monto_impuesto_20 = 705813.76 - 303499.91
        impuesto_20 = monto_impuesto_20 * 0.20
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 705813.77
        impuesto = monto_gravable * 0.25
        monto = round(impuesto + impuesto_15 + impuesto_20, 2)
        return monto

while True:
    try:
        salario = input("Introduce tu salario para el calculo: \n")
        if salario == "":
            break
        conver_salario = int(salario)
        impuesto = impuesto_sr(conver_salario)
        print(f"Lo que debes pagar de impuesto impositivo correspondiente a su salario de {conver_salario} es de {impuesto}" )
    except:
        print("Lo siento la formula solo trabaja sobre numeros enteros positivos")

