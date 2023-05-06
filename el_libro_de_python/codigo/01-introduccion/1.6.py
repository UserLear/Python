#.......condicionales: if, elif, else
lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print("No me gusta, Java no mola")
else:
    print("Ningún otro lenguaje supera a Python")

# Salida: Estoy de acuerdo, Python es el mejor

#.......bucles: while, for, break, continue
x = 0
while x < 3:
    print(x)
    x += 1

# Salida: 0, 1, 2

for i in range(3):
    print(i)

# Salida: 0, 1, 2

for i in range(3):
    if i == 1:
        continue
    print(i)

# Salida: 0, 2

#.......booleans: False, True, None
x = (5 == 1)
print(x)
# Salida: False

x = True
if x:
    print("Python!")
    
# Salida: Python!

def mi_funcion():
    pass

print(mi_funcion())
# Salida: None

#.......operadores logicos: and, or, not
print(True and False) # False
print(True or False)  # True
print(not True)       # False

