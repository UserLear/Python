import pyinputplus as pyip
#https://pyinputplus.readthedocs.io/en/latest/
#VALIDACION DE ENTRADA
#.......funcion inputNum
response = pyip.inputNum() 
#pasada: cinco
#devuelve: 'cinco' is not a number
response1 = pyip.inputNum() 
#pasada: 5 
#devuelve: 5
print(type(response1)) #<class 'int'>
response2 = pyip.inputNum()
#pasada: 5.1 
#devuelve: 5.1
print(type(response2)) #<class 'float'>

#.......funcion min= (minimo), max= (maximo), greaterThan= (mayor que), lessThan= (menor que)
response = pyip.inputNum('Enter num: ', min=4)
#entrada: 3, salida: Number must be at minimum 4. (el numero debe ser como minimo 4)
response = pyip.inputNum('Enter num: ', greaterThan=4)
#entrada: 4, salida: Number must be greater than 4. (el numero debe ser mayor que 4)
response = pyip.inputNum('>', min=4, lessThan=6)
#entrada: 6, salida: .Number must be less than 6. (el numero debe ser menor que 6), entrada: 3, salida: Number must be at minimum 4 (el numero debe ser como minimo 4).
response = pyip.inputNum('Enter num: ', max=4)
#entrada: 6, salida: Number must be at maximum 4. (numero debe ser como maximo 4)

#.......entrada en blanco
response = pyip.inputNum(blank=True)
#""

#.......limites de intento, limite de tiempo
response = pyip.inputNum(limit=2)
#f
#'f' is not a number.
#g
#'g' is not a number.
#error
response = pyip.inputNum(timeout=10)
#pasados los 10 segundos devuelve un error

response = pyip.inputNum(limit=2, default='N/A')
print(response) #N/A
response2 = pyip.inputNum(limit=2, default='null')
print(response2) #null
#asigna un valor predeterminado 

#.......blockRegexes, allowRegexes
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
#entradas permitidas

respuesta = pyip.inputNum(blockRegexes=[r'[02468]$'])
#no acepta numeros pares

response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],blockRegexes=[r'cat'])
#cat
#This response is invalid.
#catastrophe
#This response is invalid.
#category
#lista de permitidos anula a lista de anulados

#.......inputCustom() validacion personalizada
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers) # Return an int form of numbers.

response = pyip.inputCustom(addsUpToTen) # No parentheses after
#123
#The digits must add up to 10, not 6.
#1235
#The digits must add up to 10, not 11.
#1234

