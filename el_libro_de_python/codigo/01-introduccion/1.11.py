#Empaquetar y desempaquetar argumentos en Python
# A Python program to demonstrate need
# of packing and unpacking
# A sample function that takes 4 arguments
# and prints them.
def fun(a, b, c, d):
    print(a, b, c, d)
# Driver Code
my_list = [1, 2, 3, 4]
# This doesn't work
fun(my_list)
#salida: TypeError: fun() toma exactamente 4 argumentos (1 dado)


# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)
# Driver Code
my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)
#salida: (1, 2, 3, 4)

# Unpacking strings
a, b, c = '123'
print(a)
#'1'
print(b)
#'2'
print(c)
#'3'
# Unpacking lists
a, b, c = [1, 2, 3]
print(a)
#1
print(b)
#2
print(c)
#3
# Unpacking generators
gen = (i ** 2 for i in range(3))
a, b, c = gen
print(a)
#0
print(b)
#1
print(c)
#4
# Unpacking dictionaries (keys, values, and items)
my_dict = {'one': 1, 'two':2, 'three': 3}

a, b, c = my_dict  # Unpack keys
print(a)
#'one'
print(b)
#'two'
print(c)
#'three'

a, b, c = my_dict.values()  # Unpack values
print(a)
#1
print(b)
#2
print(c)
#3

a, b, c = my_dict.items()  # Unpacking key-value pairs
print(a)
#('one', 1)
print(b)
#('two', 2)
print(c)
#('three', 3)

#.......empaquetado con * el lado izquierdo debe ser una tupla o list
*a, = 1, 2
print(a)
#[1, 2]

#.......expresion fija
a, *b = 1, 2, 3
print(a)
#1
print(b)
#[2, 3]

#.......expresion fija 
*a, b = 1, 2, 3
print(a)
#[1, 2]
print(b)
#3

*a, b, c = 1, 2, 3
print(a)
#[1]
print(b)
#2
print(c)
#3

*a, b, c, d = 1, 2, 3
print(a)
#[]
print(b)
#1
print(c)
#2
print(d)
#3

#objeto generador + rango
gen = (2 ** x for x in range(10))
print(gen)
#generator object <genexpr> at 0x7f44613ebcf0>
*g, = gen
print(g)
#[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
ran = range(10)
*r, = ran
print(r)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#.......asignacion en paralelo
#asignacion comun
employee = ["John Doe", "40", "Software Engineer"]
name = employee[0]
age = employee[1]
job = employee[2]
print(name)
#'John Doe'
print(age)
#'40'
print(job)
#'Software Engineer'

#asignacion por empaquetado
name, age, job = ["John Doe", "40", "Software Engineer"]
print(name)
#'John Doe'
print(age)
#40
print(job)
#'Software Engineer'

#.......intercambio de valores entre variables
#forma normal
a = 100
b = 200
temp = a
a = b
b = temp
print(a)
#200
print(b)
#100

#desempaquetado
a = 100
b = 200
a, b = b, a
print(a)
#200
print(b)
#100

#.......recopilacion de valores multiples con *
#forma normal
seq = [1, 2, 3, 4]
first, body, last = seq[0], seq[1:3], seq[-1]
print(first, body, last)
#(1, [2, 3], 4)
print(first)
#1
print(body)
#[2, 3]
print(last)
#4

#desempaquetando
seq = [1, 2, 3, 4]
first, *body, last = seq
print(first, body, last)
#(1, [2, 3], 4)
print(first)
#1
print(body)
#[2, 3]
print(last)
#4

*head, a, b = range(5)
print(head, a, b)
#([0, 1, 2], 3, 4)
a, *body, b = range(5)
print(a, body, b)
#(0, [1, 2, 3], 4)
a, b, *tail = range(5)
print(a, b, tail)
#(0, 1, [2, 3, 4])

#.......eliminar valores innecesarios con *
a, b, *_ = 1, 2, 0, 0, 0, 0
print(a)
#1
print(b)
#2
print(_)
#[0, 0, 0, 0]

#ejemplo
import sys
print(sys.version_info)
#sys.version_info(major=3, minor=8, micro=1, releaselevel='final', serial=0)
mayor, minor, micro, *_ = sys.version_info
print(mayor, minor, micro)
#(3, 8, 1)

#8.......devolucion de tuplas en funciones
def powers(number):
    return number, number ** 2, number ** 3

# Packing returned values in a tuple
result = powers(2)
result
#(2, 4, 8)

# Unpacking returned values to multiple variables
number, square, cube = powers(2)
print(number)
#2
print(square)
#4
print(cube)
#8
*_, cube = powers(2)
print(cube)
#8

#9.......funcion de iterables con el operador *
my_tuple = (1, 2, 3)
print((0, *my_tuple, 4))
#(0, 1, 2, 3, 4)
my_list = [1, 2, 3]
print([0, *my_list, 4])
#[0, 1, 2, 3, 4]
my_set = {1, 2, 3}
print({0, *my_set, 4})
#{0, 1, 2, 3, 4}
print([*my_set, *my_list, *my_tuple, *range(1, 4)])
#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
my_str = "123"
print([*my_set, *my_list, *my_tuple, *range(1, 4), *my_str])
#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, '1', '2', '3']

#10....... desempaquetar diccionarios con el operador **
numbers = {"one": 1, "two": 2, "three": 3}
letters = {"a": "A", "b": "B", "c": "C"}
combination = {**numbers, **letters}
print(combination)
#{'one': 1, 'two': 2, 'three': 3, 'a': 'A', 'b': 'B', 'c': 'C'}






















