import random, sys
#.......practica while
while True:
    print("¿Quién eres?")
    nombre = input()
    if nombre != "Joe":
        print("Tu no eres la persona que esperaba, lo siento no puedes ingresar")
        continue
    print("Hola Joe, ingresa tu contraseña (es un pez que se infla)")
    while True:
        contraseña = input()
        if contraseña == "pezglobo":
            print("Acceso permitido: Joe")
            break
        print("Lo siento Joe, contraseña incorrecta vuelve a intentar")

    break
print("Ahora Joe puedes ingresar a nuestos datos")

#.......practica for
print("Estoy pensando en un numero entre 1 y 20")
maquina = random.randint(1, 20)

try:
    for i in range(7):
        oportunidades = 7 - i
        sobrantes = i + 1
        print("Adivina, tienes " + str(oportunidades) + ' oportinidades.')
        numero = input()
        if int(numero) < maquina:
            print("'Uf!, andas abajo")
        elif int(numero) > maquina:
            print('Uf!, andas muy arriba')
        else:
            print('Felicidades!, lo has logrado en '+ str(sobrantes) + ' intentos.')
            print("Te sobraron " + str(7 - sobrantes) + ' oportunidades')
            break
except:
    print('Error, debes ingresar un numero.')

#.......practica while
print("PIEDRA, PAPEL, TIJERA")

ganadas = 0
perdidas = 0
empatadas = 0

while True:
    maquina = random.choice(["r", 'p', 's'])
    print('Ingrese su jugada: Piedra(r), Papel(p), Tijera(s) o Salir(q).')
    print('marcador: Ganadas: '+str(ganadas)+', perdidas: '+str(perdidas)+', empatadas: '+ str(empatadas))
    jugada = input()
    if jugada == 'r' and maquina == 'r':
        print('Piedra vrs Piedra')
        print("Empate!")
        empatadas += 1
    elif jugada == 'r' and maquina == 'p':
        print('Piedra vrs Papel')
        print('Perdiste!')
        perdidas += 1
    elif jugada == 'r' and maquina == 's':
        print('Piedra vrs Tijera')
        print('Ganaste!')
        ganadas += 1
    elif jugada == 'p' and maquina == 'p':
        print('Papel vrs Papel')
        print('Empate!')
        empatadas += 1
    elif jugada == 'p' and maquina == 'r':
        print('Papel vrs Piedra')
        print('Ganaste!')
        ganadas += 1
    elif jugada == 'p' and maquina == 's':
        print('Papel vrs Tijera')
        print('Perdiste!')
        perdidas += 1
    elif jugada == 's' and maquina == 's':
        print('Tijera vrs Tijera')
        print('Empate!')
        empatadas += 1
    elif jugada == 's' and maquina == "p":
        print('Tijeras vrs Papel')
        print('Ganaste!')
        ganadas += 1
    elif jugada == 's' and maquina == 'r':
        print('Tijera vrs Piedra')
        print('Perdiste!')
        perdidas += 1
    elif jugada == 'q':
        sys.exit()
    else:
        print('Debes introducir una de las letras.')
