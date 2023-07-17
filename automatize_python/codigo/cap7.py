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
\












