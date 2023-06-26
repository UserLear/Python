import random, sys

print("PIEDRA, PAPEL, TIJERA")

while True:
    ganadas = 0
    perdidas = 0
    empatadas = 0
    maquina = random.choice(["r", 'p', 's'])
    print('Ingrese su jugada: Piedra(r), Papel(p), Tijera(s) o Salir(q).')
    marcador = 'Ganadas: '+str(ganadas)+', perdidas: '+str(perdidas)+', empatadas: '+ str(empatadas)
    jugada = input()
    if jugada == 'r' and maquina == 'r':
        print('Piedra vrs Piedra')
        print("Empate!")
        empatadas =+ 1
        print(marcador)
    elif jugada == 'r' and maquina == 'p':
        print('Piedra vrs Papel')
        print('Perdiste!')
        perdidas =+ 1
        print(marcador)
    elif jugada == 'r' and maquina == 's':
        print('Piedra vrs Tijera')
        print('Ganaste!')
        ganadas =+ 1
        print(marcador)
    elif jugada == 'p' and maquina == 'p':
        print('Papel vrs Papel')
        print('Empate!')
        empatadas =+ 1
        print(marcador)
    elif jugada == 'p' and maquina == 'r':
        print('Papel vrs Piedra')
        print('Ganaste!')
        ganadas =+ 1
        print(marcador)
    elif jugada == 'p' and maquina == 's':
        print('Papel vrs Tijera')
        print('Perdiste!')
        perdidas =+ 1
        print(marcador)
    elif jugada == 's' and maquina == 's':
        print('Tijera vrs Tijera')
        print('Empate!')
        empatadas =+ 1
        print(marcador)
    elif jugada == 's' and maquina == "p":
        print('Tijeras vrs Papel')
        print('Ganaste!')
        ganadas =+ 1
        print(marcador)
    elif jugada == 's' and maquina == 'r':
        print('Tijera vrs Piedra')
        print('Perdiste!')
        perdidas =+ 1
        print(marcador)
    elif jugada == 'q':
        sys.exit()
    else:
        print('Debes introducir una de las letras.')






