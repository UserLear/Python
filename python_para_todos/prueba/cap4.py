#4.2
tamanoNombre = input("Ingresa tu nombre: \n")

print(max(tamanoNombre))
print(len(tamanoNombre))
print(min(tamanoNombre))

#4.3
convert = input("ingresa algo y veremos que pasa: \n")
try:
    print(int(convert * 2))
except: 
    print("no ingresaste un int sino un str")
print(str(convert) + "hola")
try:
    print(float(convert))
except:
    print("no ingresaste un float si no un str")

#4.6
def tipo():
    print(type(2))

tipo() #<class "int">



