import random

#.......practica while
while True:
    print("¿Quién eres?")
    nombre = input()
    if nombre != "Joe":
        print("Tu no eres la persona que esperaba, lo siento no puedes ingresar")
        continue
    print("Hola Joe, ingresa tu contraseña (es un pez)")
    while True:
        contraseña = input()
        if contraseña == "pezglobo":
            print("Acceso permitido: Joe")
            break
        print("Lo siento Joe, contraseña incorrecta vuelve a intentar")

    break
print("Ahora Joe puedes ingresar a nuestos datos")

#.......practica for
