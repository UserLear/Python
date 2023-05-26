#RANGE EN PYTHON
#.......forma normal
for i in (0, 1, 2, 3, 4, 5):
    print(i) #0, 1, 2, 3, 4, 5

#.......uso de range
for i in range(6):
    print(i) #0, 1, 2, 3, 4, 5

#.......uso de inicio y fin
for i in range(3, 9):
    print(i) #3, 4, 5, 6, 7, 8

#.......uso de inicio, fin y salto
for i in range(5, 20, 2):
    print(i) #5,7,9,11,13,15,17,1

#.......secuencia inversa
for i in range (5, 0, -1):
    print(i) #5,4,3,2,1