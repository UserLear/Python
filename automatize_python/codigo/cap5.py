import pprint
#DICCIONARIOS Y DATOS DE ESTRUCTURACION
#.......diccionarios
miGato = {'tamaño': 'gordo', 'color': 'gris', 'disposición': 'fuerte'}
tamaño = miGato['tamaño'] 
print('Mi gato esta muy ' + tamaño) #Mi gato esta muy gordo

spam = {12345: 'Combinación de equipaje', 42: 'La respuesta'} #valores enteros por clave

#.......diccionarios poderosos
birthdays = {'Jose': '24 abril', 'Paola': '12 noviembre', 'Noel': '29 marzo'}
while True:
    print('Ingresa tu nombre: (En blanco para salir)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' cumple anos ' + name)
    else:
        print('No tengo informacion del cumpleanos de ' + name)
        print('Cuando cumples anos')
        bday = input()
        birthdays[name] = bday
        print('Cumple anos anadido a la base de datos')

#.......orden de insercion
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
list(eggs) #['name', 'species', 'age']
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
list(ham) #['species', 'age', 'name']


spam = {}
spam['first key'] = 'value'
spam['second key'] = 'value'
spam['third key'] = 'value'
list(spam) #['first key', 'third key', 'second key']

#.......metodos keys(), values(), items()
descripcionFisica = {'altura': '1.78 mts', 'edad': '32 anos', 'peso': '180 lbs'}
for i in descripcionFisica.values():
    print(i) 
#1.78 mts
#32 anos
#180 lbs

for x in descripcionFisica.keys():
    print(x)
#altura
#edad
#peso

for n, t in descripcionFisica.items():
    print(n, t)
#altura 1.78 mts
#edad 32 anos
#peso 180 lbs

print(descripcionFisica.keys()) #dict_keys(['altura', 'edad', 'peso']) - tupla
print(list(descripcionFisica.keys())) #['altura', 'edad', 'peso'] -convertir en lista

spam = {'color': 'red', 'edad': 42}
for k, v in spam.items():
    print('Clave: ' + k + ' Valor: ' + str(v)) #Clave: red Valor: 42

#.......comprobar si existe una clave o valor en diccionario
spam = {'color': 'red', 'edad': 42}
color = 'color' in spam.key() #verdadero
edad = 42 in spam.value() # verdadero
color1 = 'color' in spam #verdadero

#.......metodo get()
picnicItems = {'manzanas': 5, 'tazas': 2}
print('Traigo ' + str(picnicItems.get('tazas', 0)) + ' tazas.') #Traigo 2 tazas
print('Traigo ' + str(picnicItems.get('huevos', 0)) + ' huevos.') #Traigo 0 huevos

#.......metodo setdefault()
spam = {'nombre': 'Pooka', 'edad': 5}
spam.setdefault('color', 'negro') #'negro'

spam = {'color': 'negro' , 'edad': 5, 'nombre': 'Pooka'}
spam.setdefault('color', 'blanco') #'negro'
spam = {'color': 'negro', 'edad': 5, 'nombre': 'Pooka'}

#programa cuenta numero de ocurrencias
mensaje = 'Era un día brillante y frío de abril, y los relojes daban las trece.'
cuenta = {}

for carácter in mensaje:
    cuenta.setdefault(carácter, 0)
    cuenta[carácter] = cuenta[carácter] + 1

print(cuenta) 
'''{'E': 1, 'r': 6, 'a': 7, ' ': 13, 'u': 1, 'n': 3, 'd': 3, 'í': 2, 'b': 3, 'i': 2, 'l': 6, 't': 2, 'e': 6, 'y': 2, 'f': 1,
'o': 3, ',': 1, 's': 3, 'j': 1, 'c': 1, '.': 1}'''

#.......bonita impresion
mensaje = 'Era un día brillante y frío de abril, y los relojes daban las trece.'
cuenta = {}

for carácter in mensaje:
    cuenta.setdefault(carácter, 0)
    cuenta[carácter] = cuenta[carácter] + 1

pprint.pprint(cuenta)
'''
{' ': 13,
 ',': 1,
 '.': 1,
 'E': 1,
 'a': 7,
 'b': 3,
 'c': 1,
 'd': 3,
 'e': 6,
 'f': 1,
 'i': 2,
 'j': 1,
 'l': 6,
 'n': 3,
 'o': 3,
 'r': 6,
 's': 3,
 't': 2,
 'u': 1,
 'y': 2,
 'í': 2}
'''
#.......uso de estucturas de datos para el mundo real
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

#.......diccionarios anidados
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))









