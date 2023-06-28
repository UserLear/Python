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


