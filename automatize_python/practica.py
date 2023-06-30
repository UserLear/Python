#ingresa = input("Ingresa un numero: ") 
"""while True:
    convertir = int(ingresa)
    def collatz(numero):
        if numero % 2 == 0:
            print(numero)
            valor = numero // 2
            return valor
        elif numero % 2 == 1:
            print(numero)
            valor = 3 * numero + 1
            return valor
    llamada = collatz(convertir)
    if llamada == 1:
        break"""

"""while True:
    introducir = input("Ingresa algo: ")
    convert = int(introducir)
    result = 0
    while result > 1:
        def collatz(numero):
            if numero % 2 == 0:
                print(numero)
                valor = numero // 2
                return valor
            elif numero % 2 == 1:
                print(numero)
                valor = 3 * numero + 1
                return valor
        result = collatz(convert)"""

#prueba bucle while con def
"""def resta(n):
    return n - 1

valor = input()
peticion = int(valor)

while True: 
    modificado = resta(peticion)
    guardado = 0
    while guardado > 1:
        guardado = modificado
        rest = resta(guardado)"""


def multiplica(n):
    return n*2

def multiOpcion(n):
    if n == 2:
        print("la variable tomo el valor dos")
    else:
        print("la variable es cualquier numero menos dos")

#variable introducida y modificada
valor = input()
convert = int(valor)
valor1 = 0
valor1 = convert

while valor1 != 1:
    print(valor1)
    valor1 -= 1 #si no existe el modificador de variable se repite infinitamente
    multiOpcion(valor1)

#buscar un modificador de variable dentro de while
def collatz(numero):
    if numero % 2 == 0:
        print(numero)
        valor = numero // 2
        return valor
    elif numero % 2 == 1:
        print(numero)
        valor = 3 * numero + 1
        return valor





    











    
    
    
        








