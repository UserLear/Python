#NUMEROS
#nuemero de vidas en un juego
lives = 3
print(type(lives)) #<class 'int'>

lives = "3"
print(type(lives)) #<class 'str'>

#representaciones con numeros
edad = 32
presupuesto = 100

#con nivel de precision decimal
temperatura = 12.12
print(type(temperatura)) #<class 'float'>

#cambiar el valor de la variable
lives = 2
print(lives) #2
lives = 1
print(lives) #1

#operaciones dentro de variables
lives = 25 - 13
print(lives) #12

#asignacion de un nuevo valor a variable
lives = lives - 1
print(lives) #11

#asignacion de un nuevo valor con otro metodo
lives -= 1
print(lives) #10

#notacion cientifica
number = 45000000000000000000000.1
print(number) #4.5e+22

number = 1.00000000000000023
print(number) #1.0000000000000002

number = 0.00000000000000000000000025
print(number) #2.5e-25

#EJEMPLO 7 + 8 + 9
#programa que calcula el promedio de ventas 
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
