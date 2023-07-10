#CUERDAS DE MANIPULACION
#.......cita dentro de cadena
oracion = 'That is Alice is cat.'
cita = "That is Alice's cat."

#.......caracter de escape si usa ' y " dentro de cadena
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

#.......cuerdas en bruto
spam5 = r'Say hi to Bob\\ is mother.'
print(spam5) #Say hi to Bob\\ is mother.

#.......cadenas multilinea con comillas triples
print("""
Aparentemente la molestia se debio a un mal
entendido de su parte, ya que no se toco ese
tema pero usted lo saco a relucir
""")

#.......indexacion y corte de cadenas
letras = 'Hola mi buen amigo'
print(letras[1]) #o
print(letras[1:6]) #ola m

#.......operadores in y not in
letras = 'Hola mi buen amigo'
print("Hola" in letras) #True

print("" in letras) #True

#.......poner cadenas dentro de otras cadenas





