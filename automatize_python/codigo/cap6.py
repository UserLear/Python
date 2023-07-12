#CUERDAS DE MANIPULACION
#1.......cita dentro de cadena
oracion = 'That is Alice is cat.'
cita = "That is Alice's cat."

#2.......caracter de escape si usa ' y " dentro de cadena
spam = 'Say hi to Bob\'s mother.'
print(spam) #Say hi to Bob's mother
spam1 = 'Say hi to \"Bob\" is mother.'
print(spam1) #Say hi to "Bob" mother
spam2 = 'Say hi to Bob\t is mother.'
print(spam2) #Say hi to Bob   is mother.
spam3 = 'Say hi to Bob\n is mother.'
print(spam2) #Say hi to Bob
                 #is mother.
spam4 = 'Say hi to Bob\\ is mother.'
print(spam4) #Say hi to Bob\ is mother.

#3.......cuerdas en bruto
spam5 = r'Say hi to Bob\\ is mother.'
print(spam5) #Say hi to Bob\\ is mother.

#4.......cadenas multilinea con comillas triples
print("""
Aparentemente la molestia se debio a un mal
entendido de su parte, ya que no se toco ese
tema pero usted lo saco a relucir
""")

#5.......indexacion y corte de cadenas
letras = 'Hola mi buen amigo'
print(letras[1]) #o
print(letras[1:6]) #ola m

#6.......operadores in y not in
letras = 'Hola mi buen amigo'
print("Hola" in letras) #True

print("" in letras) #True

#7.......poner cadenas dentro de otras cadenas
nombre ='Moises'
edad = 32
print('Mi nombre es %s: tengo %s años' %(nombre, edad)) #Mi nombre es Moises. tengo 32 años

print(f'Mi nombre es {nombre}. tengo {edad} años') #Mi nombre es Moises. tengo 32 años

#8.......metodos: upper(), lower(), isupper(), islower()
nombre = 'MOIses'
print(nombre.lower()) #moises

print(nombre.upper()) #MOISES

print(nombre.isupper()) #False
mayuscula = nombre.upper()
print(mayuscula.isupper()) #True

print(nombre.islower()) #False
minuscula = nombre.lower()
print(minuscula.islower()) #True

#mini programa
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

#9.......los metodos isX()
#metodo isalpha
lista1 = ['Moises', 'Moises ', 'Moises3']
for i in lista1:
    metodo = i.isalpha()
    print('isalpha: '+ i +': '+ str(metodo))
#isalpha: Moises: True
#isalpha: Moises : False
#isalpha: Moises3: False

#metodo isalnum
lista2 = ['Juancho33', 'Juancho','1234']
for i in lista2:
    metodo = i.isalnum()
    print('isalnum: '+ i +': '+ str(metodo))
#isalnum: Juancho33: True
#isalnum: Juancho: True
#isalnum: 1234: True

#metodo isdecimal
lista3 = ['12345', '123a567', '1,2,3,4']
for i in lista3:
    metodo = i.isdecimal()
    print('isdecimal: '+ i +': '+ str(metodo))
#isdecimal: 12345: True
#isdecimal: 123a567: False
#isdecimal: 1,2,3,4: False

#metodo isspace
lista4 = [' ', '\n', '/', 'a', 'n2', '3']
for i in lista4:
    metodo = i.isspace()
    print('isspace: '+ i +': '+ str(metodo))
#isspace:  : True
#isspace:
#: True
#isspace: /: False
#isspace: a: False
#isspace: n2: False
#isspace: 3: False

#metodo istitle
lista5 = ['Hola', 'pedro', 'lUis', 'JacoBo']
for i in lista5:
    metodo = i.istitle()
    print('istitle: '+ i +': '+ str(metodo))
#istitle: Hola: True
#istitle: pedro: False
#istitle: lUis: False
#istitle: JacoBo: False

#10.......metodo startswith() y endswith()
iniciaCon = 'Hola muchachos'
lista1 = ['h', 'H', 'Hola', 'muchachos', 'Hola muchachos']
for i in lista1:
    valor = iniciaCon.startswith(i)
    print(f'startwith: {i}: {valor}')
#startwith: H: True
#startwith: Hola: True      
#startwith: muchachos: False
#startwith: Hola muchachos: True

terminaCon = 'Esta historia comienza en 1991'
lista2 = ['comienza en 1991', 'en', '1991', 'En 1991', "Esta historia comienza en 1991"]
for i in lista2:
    valor = terminaCon.endswith(i)
    print('endswith: %s: %s' %(i, valor))
#endswith: en: False
#endswith: 1991: True
#endswith: En 1991: False
#endswith: Esta historia comienza en 1991: True











