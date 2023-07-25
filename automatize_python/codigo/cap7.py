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
haRegex4 = re.compile(r'(ha){3,5}?') #coincidencia no codiciosa
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
regex1 = re.compile(r'\D+') #cualquier caracter que no sea un digito numerico del 0 al 9
resul = regex1.findall('caracteres: "" ## aa AA :: 33') 
print(resul) #['caracteres: "" ## aa AA :: ']

regex1 = re.compile(r'\w+') #imprime letra, digitos numerico o el subrayado
resul = regex1.findall(':"#$ \{\}1234 : 3 ] caracter ________') 
print(resul) #['1234', '3', 'caracter', '________']

regex1 = re.compile(r'\W+') #imprime cualquier caracter que no sea letra ni numero ni subrayado
resul = regex1.findall(':"#$ \{\}1234 : 3 ] caracter ________') 
print(resul) #[':"#$ \\{\\}', ' : ', ' ] ', ' ']

regex1 = re.compile(r'\s+') #imprime cualquier espacio, tabulacion, caracter nueva linea
resul = regex1.findall(':"|`!@#$%^*() _-+=><#$\{\}1234:3]caracter________\n ') 
print(resul) #[' ', '\n ']

regex1 = re.compile(r'\S+') #cualquier caracter que no sea espacio, tabulacion o nueva linea
resul = regex1.findall(':"|`!@#$%^*() _-+=><#$\{\}1234:3]caracter________\n ') 
print(resul) #[':"|`!@#$%^*()', '_-+=><#$\\{\\}1234:3]caracter________']

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge') #['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

#.......hacer tus propias clases
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.') #['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

vowelRegex = re.compile(r'[a-zA-Z0-9]')
mo = vowelRegex.findall('RoboCop2 eats3 baby4 food5. BABY2 FOOD .') 
print(mo)
#['R', 'o', 'b', 'o', 'C', 'o', 'p', '2', 'e', 'a', 't', 's', '3', 'b', 'a', 'b', 'y', '4', 'f', 'o', 'o', 'd', '5', 'B', 'A', 'B', 'Y', '2', 'F', 'O', 'O', 'D']

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)
#['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello, world!')
print(mo.group()) #Hello
mo1 = beginsWithHello.findall('Hello, world!')
print(mo1) #['Hello']
#<re.Match object; span=(0, 5), match='Hello'> 
mo3 = beginsWithHello.search('He said hello.') == None
print(mo3) #True

beginsWithHello = re.compile(r'\D$')
mo = beginsWithHello.search('1Hello, 3world!4!')
print(mo) #<re.Match object; span=(16, 17), match='!'>

beginsWithHello = re.compile(r'\d$')
mo = beginsWithHello.search('1Hello, 3world!4')
print(mo) #<re.Match object; span=(15, 16), match='4'>

beginsWithHello = re.compile(r'^14$')
mo = beginsWithHello.search('123454') 
print(mo) #None
mo1 = beginsWithHello.search('14') 
print(mo1) #<re.Match object; span=(0, 2), match='14'>

beginsWithHello = re.compile(r'^\d+$')
mo = beginsWithHello.search('123454') 
print(mo) #<re.Match object; span=(0, 6), match='123454'>

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890') #<re.Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None #True
wholeStringIsNum.search('12  34567890') == None #True

#.......caracter comodin
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo) #['cat', 'hat', 'sat', 'lat', 'mat']

#.......combinando todo con Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1)) #'Al'
print(mo.group(2)) #'Sweigart'
#combina con todo excepto con nueva linea de modo codicioso

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group() #'<To serve man>'
#combina de forma no codiciosa
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group() #'<To serve man> for dinner.>'

#.......coincidencia de lineas nuevas con el caracter de punto
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group() 
#'Serve the public trust.'

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

#.......coincidencia sin distincion entre mayusculas y minusculas
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
#'RoboCop
robocop.search('ROBOCOP protects the innocent.').group()
#'ROBOCOP'
robocop.search('Al, why does your programming book talk about robocop so much?').group()
#'robocop'

#.......sustitucion de cadenas con el metodo sub()
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo) #'CENSORED gave the secret documents to CENSORED.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo) #A**** told C**** that E**** knew B**** was a double agent.'

#.......gestion de expresiones regulares complejas
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

#combiando re.ignorecase, re.dotall, re.verbose
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
#https://nostarch.com/automatestuff2/












