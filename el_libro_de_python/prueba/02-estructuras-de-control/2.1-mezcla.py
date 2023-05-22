#condicionales dentro de while
x = 0
while x < 3:
    if x == 0:
        print("ahorita vale " + str(x))
        x += 1
    elif x == 1:
        print("ahorita vale el uno " + str(x))
        x += 1
    else: 
        x += 1
        print("ahorita vale el triple " + str(x))

#while dentro de condicionales
x1 = 2
if x1%2 == 0:
    while x1 < 3:
        print("eres divisible " + str(x1))
        x1 += 1
else: 
    print("lamentablemente el numero no es divisible")

#condicionales dentro de for
for i in range(3):
    print(i)

x2 = "hola"
for i in x2:
    if i == "h":
        print("es la h de huella")
    elif i == "o":
        print("es la o de obligacion")
    elif i == "l":
        print("es la l de luna")
    else:
        print("es la a de aumento")

#for dentro de condicionales
x2 = 6
if x2 >= 0 and x2 < 3:
    for i in range(x2):
        print("se multiplica por 2 " + str(i*2))
elif x2 >= 3 and x2 < 6:
    for i in range(x2):
        print("se multiplica por 3 " + str(i*3))
else: 
    for i in range(x2):
        print("se multiplica por 4 " + str(i*4))

#











    

        









