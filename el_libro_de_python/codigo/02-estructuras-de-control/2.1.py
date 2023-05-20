#CONDICIONAL IF
a = 4
b = 2
if b != 0: 
    print(a/b)

#con mas de una instruccion en el bloque de codigo
if b != 0:
    c = a/b
    d = c + 1
    print(d)

#1.......identacion
if b != 0:
    c = a/b
    print("Dentro if")
print("Fuera if")
#todo lo que este identado pertenece al boque de codigo de if

#2.......operador de comparacion > mayor que
if b > 0:
    print(a/b)

#3.......condicion combinada
a = 10
if a > 5 and a < 15:
    print("Mayor que 5 y menos que 15")

#4.......bloque vacio tirara error
#if a > 5:

#5.......pasar pass al bloque
if a > 5:
    pass

#CONDICIONAL ELSE + ELIF
#6......else
x = 5
if x == 5:
    print("Es 5")
else:
    print("No es 5")

#7.......elif
x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")

#OPERADOR TERNARIO
x = 5
print("Es 5" if x == 5 else "No es 5")
#Es 5


