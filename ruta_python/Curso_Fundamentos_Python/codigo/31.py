#LOOPS: WHILE
#while necesita una condicion que sea verdadera y un bloque que modifique esa condicion
#para que el bucle while sea un bucle finito. 
contar = 0
while contar < 5:
    contar += 1
    print(contar) 
"""
1
2
3
4
5
"""
#break: rompe el ciclo al existir una condicion especifica
sumar = 0
while sumar < 30:
    sumar += 3
    if sumar >= 25:
        break
    print(sumar)
"""
3
6
9
12
15
18
21
24
"""
#continue: al entrar al bloque de continue salta el cogido que le continua
resta = 0
while resta < 50:
    resta += 3
    if resta > 10 and resta < 40: 
        continue
    print(resta)
"""
3
6
9
42
45
48
51
"""