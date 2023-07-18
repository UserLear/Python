import re
#COINCIDENCIA DE PATRONES CON EXPRESIONES REGULARES
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
     chunk = message[i:i+12]
     if isPhoneNumber(chunk):
         print('Phone number found: ' + chunk)
print('Done')

#.......objeto Regex
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #creamos un objeto regex
mo = phoneNumRegex.search('Mi número es 415- 555-4242.') #objeto regex tiene el metod search que devuelve un objeto match
print('Número de teléfono encontrado: ' + mo.group()) #el objeto match tiene el metod group que devolvera el texto coincidente
#Número de teléfono encontrado: 415-555-4242

#.......agrupacion con parentesis
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Mi número es 415- 555-4242.') #objeto regex tiene el metod search que devuelve un objeto match
mo.group(1) #'415'
mo.group(2) #'555-4242'
mo.group(0) #'415-555-4242'
mo.group() #'415-555-4242'
mo.groups() #('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode) #415
print(mainNumber) #555-4242

#.......parentesis
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1) #'(415)'
mo.group(2) #'555-4242'

#.......tuberia (coincidencia entre muchas expresiones)
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batma and Tina Fey')
print(mo1.group()) #'Batman'
print(mo1.groups()) #()
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group()) #'Tina Fey'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batimóvil perdió una rueda')
mo.group() #'Batimóvil'
mo.grupo(1) #'móvil'

#.......emparejamiento con signo de interrogacion
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group() #'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group() #'Batwoman'

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('Mi número es 415-555-4242')
mo1.group() #'415-555-4242'

mo2 = phoneRegex.search('Mi número es 555-4242')
mo2.group() #'555-4242'

#.......coincidencia de cero o mas con la estrella
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group() #'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group() #'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group() #'Batwowowowoman'

#.......coincidencia de uno o mas con el plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group() #'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group() #'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None #True

#.......coincidencia de repeticiones con llaves
haRegex = re.compile(r'(Ha){3}')
haRegex1 = re.compile(r'(ha){3,5}')
haRegex2 = re.compile(r'(ha){3,}')
haRegex3 = re.compile(r'(ha){,5}')
haRegex4 = re.compile(r'(ha){3,5}?')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex1.search('hahahahaha')
mo3 = haRegex2.search('hahahahahahahaha')
mo4 = haRegex3.search('haha')
mo5 = haRegex4.search('hahahahaha')
print(mo1.group()) #HaHaHa
print(mo2.group()) #hahahahaha   
print(mo3.group()) #hahahahahahahaha
print(mo4.group()) #haha
print(mo5.group()) #hahaha

#.......metodo findall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') #['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') #[('415', '555', '9999'), ('212', '555', '0000')]

#.......clases de personajes
regex1 = re.compile(r'(\D){1,}')
resul = regex1.search('caracteres: " # a A : 3')
print(resul.group())








