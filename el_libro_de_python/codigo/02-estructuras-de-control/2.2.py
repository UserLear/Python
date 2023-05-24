#bucle for
for i in range(0, 5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4

for i in "Python":
    print(i)

# Salida:
# P
# y
# t
# h
# o
# n

#4.......identificar un iterable
from collections import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))  #True
print(isinstance(cadena, Iterable)) #True
print(isinstance(numero, Iterable)) #False

#5.......crear un iterador
lista = [5, 6, 3, 2]
it = iter(lista)
print(it)       #<list_iterator object at 0x106243828> expresa que es un iterador
print(type(it)) #<class 'list_iterator'> de la clase list_iterator

#6.......acceder al iterador
lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
#     [5, 6, 3, 2]
#      ^
#      |
#     it
print(next(it))
#     [5, 6, 3, 2]
#         ^
#         |
#        it
print(next(it))
#     [5, 6, 3, 2]
#            ^
#            |
#           it

#8.......iteradores independientes
lista = [5, 6, 7]
it1 = iter(lista)
it2 = iter(lista)
print(next(it1)) #5
print(next(it1)) #6
print(next(it1)) #7
print(next(it2)) #5

#9.......for anidado
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista: #si iteramos un solo for
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]

for i in lista:
    for j in i:
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3

#ejemplo
#iterar al reves
texto = "Python"
for i in texto[::-1]:
    print(i) #n,o,h,t,y,P 

#iterar saltandose elementos
texto = "Python"
for i in texto[::2]:
    print(i) #P,t,o








