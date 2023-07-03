import random
#LISTAS
#.......valor de lista
[1, 2, 3, 4, 6]
["hola", "como", "esta"]

n = [ 'n', 4, "r", 8, True, False, None]
s = [] 

#.......indices
n[1] # 4
n[4] # True

animales = ['murcielago', 'rata', 'elefante', 'gato', 'perro']
print("Hola" + animales[2]) # Hola elefante
print('Hola al' + animales[3] + " le gusta comer " + animales[1]) #Hola al gato le gusta comer rata

#.......lista de listas
listas = [['gato', 'murcielago'], [10, 20, 30, 40]]
print(listas[0][1]) #murcielago

#.......indices negativos
animales = ['murcielago', 'rata', 'elefante', 'gato', 'perro']
print(animales[-1]) #perro

#.......obtener lista con sectores
animales = ['murcielago', 'rata', 'elefante', 'gato', 'perro']
print(animales[1:4]) #['rata', 'elefante', 'gato', 'perro']
print(animales[:2]) #['murcielago', 'rata', 'elefante]
print(animales[3:]) #['gato', 'perro']
print(animales[:]) #['murcielago', 'rata', 'elefante', 'gato', 'perro']

#.......longitud de lista
animales = ['murcielago', 'rata', 'elefante', 'gato', 'perro']
print(len(animales)) #5

#.......cambio de valores en una lista
animales = ['murcielago', 'rata', 'elefante', 'gato', 'perro']
animales[1] = "hipopotamo"
print(animales) #murcielago, hipopotamo, elefante, gato, perro

#.......concatenacion de listas y replicacion de listas
numero = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd', 'e']
conca = numero + letras
replica = numero * 2

#.......eliminacion de valores
letras = ['a', 'b', 'c', 'd', 'e']
print(letras[2]) #c
del letras[2]
print(letras[2]) #d

#.......eliminaicon de variable
m = 3
print(m) #3
del m
print(m) #error not defined

#.......anadir a lista vacia
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

#.......uso de for en listas
for i in [0, 1, 2, 3]:
    print(i)
#1
#2
#3
#4

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#Index 0 in supplies is: pens
#Index 1 in supplies is: staplers
#Index 2 in supplies is: flamethrowers
#Index 3 in supplies is: binders

#.......operadores in y not in
animales = ['murcielago', 'rata', 'elefante', 'gato', 'perro']
anima = "hipopotamo" in animales 
print(anima) #True
anima = 'hipopotamo' not in animales
print(anima) #False

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets: #True
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.') 

#.......asignacion multiple
gato = ['gordo', 'gris', 'ruidoso']
tamano, color, disposición = gato
print(tamano) #gordo

#.......funcion enumerate() en lugar de len()
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
     print('Index ' + str(index) + ' in supplies is: ' + item)

#Index 0 in supplies is: pens
#Index 1 in supplies is: staplers
#Index 2 in supplies is: flamethrowers
#Index 3 in supplies is: binders

#.......funciones random.choice() + random.shuffle()
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
random.choice(supplies) #devuelve cualquier valor de supplies

random.shuffle(supplies) #reordena los elementos de una lista en su lugar

#.......operadores de asignacion aumentada
n = 42
n += 2
print(n) #44

n += 1
print(n) #41

n *= 2
print(n) #82

n /= 2
print(n) #41

n %= 3
print(n) #2

saludo = 'hola'
saludo += 'Moises' 
print(saludo) #holaMoises-concatenacion

saludo *= 2
print(saludo) #holaMoisesholaMoises-replicacion

#.......metodos
numeros = [1, 2, 3, 4]
print(numeros.index(3)) #2

numeros1 = [1, 2, 3, 1, 2, 3]
print(numeros1.index(1)) #0

letras = ['a', 'b', 'c']
letras.append("d")
print(letras) # ['a', 'b', 'c', 'd'] - agrega al final de la lista

letras.insert(2, 'z')
print(letras) #['a', 'b', 'z', 'c', 'd']

letras.remove("b")
print(letras) #['a', 'z', 'c', 'd']

numeros1.remove(1)
print(numeros1) #[2, 3, 1, 2, 3] - elimina el primero que encuentre

























