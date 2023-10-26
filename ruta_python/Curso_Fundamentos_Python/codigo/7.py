#TIPOS DE DATOS
#string
my_name = "Moises"
my_name = 'Moises'
print('my_name ==>',my_name) #my_name ==> Moises

#para distinguir el tipo de variable
print(type(my_name)) #<class 'str'>

#int
my_age = 32
print(my_age) #32
print(type(my_age)) #<class 'int'>

#boolean puede sr true o false solamente, ambos comienzan con letra mayuscula
is_single = True
print(is_single) #True
print(type(is_single)) #<class 'bool'>

#input
#preguntar la edad
my_age = input("¿cual es tu edad?: ") #input devuelve simpre un string
print(my_age) #32
print(type(my_age)) #<class 'str'>
