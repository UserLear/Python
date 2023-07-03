import time, sys
#.......valor de retorno + declaracion de retorno
len("hola") # 4 : valor de retorno

def largoPalabra(a):
    largo = len(a)
    return largo

largoPalabra("generacion") # 10

#......zig zag

try:
    while True:
        caracter = "*" * 8
        espacio = " "
        for i in range(6):
            espacios1 = i * espacio
            cadena1 = espacios1 + caracter
            print(cadena1)
            time.sleep(0.1)
        for n in range(6):
            i -= 1
            espacios2 = i * espacio
            cadena2 = espacios2 + caracter
            print(cadena2)
            time.sleep(0.1)
except:
    sys.exit()

"""crear una variable y asignarle valor usando la funcion input() y guardar ese valor en otra variable para poder ser modificada
"""
print("Parte 1:")
ingreso = input("Ingresa un numero mayor que 5: \n") #imprime el numero al ser ingresado
conver = int(ingreso)
asigna = 0
asigna = conver

print(asigna) #imprime el valor asignado por la funcion input()
asigna -= 2
print(asigna) #imprime la variable modificada

"""crear una declaracion while que modifique a una variable creada
"""
print("Parte 2:")
ingreso = input("Ingresa un numero mayor que 5: \n") #imprime el numero al ser ingresado
conver = int(ingreso)
asigna = 0
asigna = conver

while asigna > 0:
    print(asigna)
    asigna -= 1

"""crear una funcion para que sea modificada por la declaracion while
"""
def suma(n):
    return n + 1

ingreso = input("Ingresa un numero mayor que 5: \n") #imprime el numero al ser ingresado
conver = int(ingreso)
asigna = 0
asigna = conver

while asigna < 100:
    asigna = suma(asigna)
    print(asigna)

"""crea una funcion con condicionales para modificar una variable
"""
def suma(n):
    if n >= 10 and n <= 40:
        n += 1
        return n
    elif n > 40 and n <= 80:
        n += 3
        return n
    else:
        n += 5
        return n

ingreso = input("Ingresa un numero mayor que 5: \n") #imprime el numero al ser ingresado
conver = int(ingreso)
asigna = 0
asigna = conver

while asigna < 100:
    asigna = suma(asigna)
    print(asigna)

#.......proyecto
#.......proyecto
try:
    def collatz(number):
        if number % 2 == 0:
            number = number // 2
            return number
        elif number % 2 == 1:
            number = 3 * number + 1
            return number
    
    
    ingreso = input("Ingresa un numero: \n")
    conver = int(ingreso)
    asigna = 0
    asigna = conver
    
    while True:
        asigna = collatz(asigna)
        print(asigna)
        if asigna == 1:
            break
except:
    print("Error debes intoducir un numero.")


