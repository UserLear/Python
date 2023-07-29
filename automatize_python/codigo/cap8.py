import pyinputplus as pyip
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


