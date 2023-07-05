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
print(conca) #[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
replica = numero * 2
print(replica) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

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

ordenar = [-10, 8, 3, -1, 0, 4, -3]
ordenar.sort() 
print(ordenar) # [-10, -3, -1, 0, 3, 4, 8] - ordena los valores

ordenarInverso = [-10, 8, 3, -1, 0, 4, -3]
ordenarInverso.sort(reverse=True)
print(ordenarInverso) # [8, 4, 3, 0, -1, -3, -10] - ordena de forma inversa

ordenAlfabetico = ['a', 'z', 'A', 'Z']
ordenAlfabetico.sort(key=str.lower)
print(ordenAlfabetico) #['a', 'A', 'z', 'Z'] - ordena alfabeticamente

invertirOrden = ['gato', 'perro', 'alce']
invertirOrden.reverse()
print(invertirOrden) #['alce', 'perro', 'gato'] - hace un orden inverso 

#.......lista en varias lineas
nume = [1, 2, 3, 
        4, 5, 6, 
        7, 8, 9]

#.......programita
import random
nivelOrdinal = ['Muy bajo', 'Bajo', 'Moderado', 'Normal', 'Poco alto', 'Alto', 'Mul alto', 'Preocupante']
posicion = random.randint(0, len(nivelOrdinal)-1)
valor = nivelOrdinal[posicion]
print('El nivel '+ str(posicion) + ' significa que usted esta ' + valor)

#.......tipos datos de secuencia-lista
especialidad = 'patologia'
print(especialidad[2]) #t
print(especialidad[-2]) #g
print(especialidad[2:6]) #tolo
print('lo' in especialidad) #True

#.......tuplas
tupl = (1, True, 'Hola')
tupl1 = (3,)

#.......referencia
numero = [1, "t", True]
numero1 = numero
numero1[1] = 'G'
print(numero1) #[1, 'G', True]
print(numero) #[1, 'G', True]

#.......identidad y funcion id()
print(id("hola")) #333921341232

nombre = "Moises"
print(id(nombre)) #263968435712
nombre += 'Ayala'
print(nombre) #MoisesAyala
print(id(nombre)) #774031047344 - al modificar la cadena cambia su id

lista = ['hola', 'como', 'esta']
print(id(lista)) #313363288576
lista.append('usted')
print(id(lista)) #313363288576 - modifica a la lista en su lugar por ser mutable

lista1 = lista
print(lista1) #['hola', 'como', 'esta', 'usted']
lista1 = ['lunes', 'martes', 'miercoles']
print(lista) #['hola', 'como', 'esta', 'usted']
print(id(lista)) #313363288576
print(lista1) #['lunes', 'martes', 'miercoles']
print(id(lista1)) #477304643008

#.......pasando referencia
def saludo(a):
    a.append('hola')

oracion = ['como', 'esta', 'usted']
saludo(oracion)
print(oracion) #['como', 'esta', 'usted', 'hola']








































