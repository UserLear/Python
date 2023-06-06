#EJECUCION CONDICIONAL pdf pg 45
#3.1.......expresiones booleanas
x = 4
y = 5
print(x == y) #False
print(x != y) #True
print(x < y) #True
print(x <= y) #True
print(x > y) #False
print(x >= y) #False
print(x is y) #False
print(x is not y) #True

#3.2.......operadores logicos
x1 = 6
y1 = 7
print(x1 >= 0 and x1 <= 10) #True
print((x1*2)%2 == 0 or (y1*3)%2 == 0) #True 
print(not(x1 == y1)) #True

#3.3.......ejecucion condicional
x2 = 5

if x2 <= 10:
    print("este numero es menor que 11")

if x2 > 0:
    pass #esto permite terminar luego