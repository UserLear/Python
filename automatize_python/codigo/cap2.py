#CONTROL DE FLUJO
#.......operadores de comparacion o relacionales
a = 1
b = 2
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

#.......operadores logicos o booleanos binarios
print(a != b and a <= b) #True
print(b < a or b < 10) #True
print(not(a < b)) #False
print(not not(a < b)) #True

#.......declaracion if
name = "moises"
if name == "moises":
    print("hola " + name)

#.......declaracion else
name = input("ingresa tu nombre: \n")
if name == "Moises":
    print("Hola " + name + ", tu nombre mide " + str(len(name)) + " letras")
else: 
    print("No te conozco, pero tu nombre mide " + str(len(name)) + " letras")

#.......declaracion elif
nombre = input("Cual es tu nombre: \n")
print("Hola " + nombre + ", para acceder a nuestro contenido dependera de tu edad")
edad = input("Introduce ahora tu edad: \n")
if int(edad) > 0 and int(edad) < 15: 
    print("Ummm!, lo siento no tengo nada para menores de 15 años")
elif int(edad) >= 16 and int(edad) <= 30:
    print("Te mostraremos opciones de carrera y de negocios que pueden interesarte")
else: 
    print("Tu pasas de los 30, para ti tenemos un mundo oportunidades")

#......declaracion while
nombre = ""
while nombre != "Moises":
    nombre = input("Debes ingresar con tu usuario: \n")
    print("Ese no es tu nombre de usuario")

#.......uso de break
while True:
       print('Escriba su nombre.')
       name = input()
       if name == 'su nombre':
           break
print('¡Gracias!')

#.......uso de continue
while True:
    print('¿Quién eres?')
    nombre = input()
    if nombre != 'Joe':
        continue
    print('Hola, Joe. ¿Cuál es la contraseña? (Es un pez.)')
    contraseña = input()
    if contraseña == 'pez espada':
        break
print('Acceso concedido.') 

#.......uso de for
print('Mi nombre es')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num
print(total)

#.......proyecto encuentra el numero correcto
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


#....proyecto piedra papel tijera
import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1










