#COMPARACION DE NUMEROS FLOTANTES
x = 3.3
y = 1.1 + 2.2
print(x) #3.3
print(y) #3.3000000000000003
print(x==y) #False

#comparacion por medio de stings
y_str = format(y,".2g")
print(y_str) #3.3 este resultado se convierte en un str
print(x==y_str) #False
print(y_str==str(x)) #True

#comparacion por medio de forma matematica
print("*"*10) 

print(y, x) #3.3000000000000003 3.3

#creamos una tolerancia
tolerance = 0.00001
print(abs(x-y)<tolerance) #True
