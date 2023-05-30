#this program says hello and asks for my name (este es un comentario)
print("hola mundo") #funcion integrada imprimir le dice a python que muestre en pantalla
print("cual es tu nombre")
myName = input() #funcion entrada que espera que el usuaro escriba en el teclado y lo asigna a una variable
print("es un placer conocerte, " + myName) #concatenar 
print("la longitud de tu nombre es:")
print(len(myName)) #funcion len() mide el tamaño del iterable
print("¿cual es tu edad?")
myEdad = input()
print("usted tendra " + str(int(myEdad) + 1) + " en un año.") #funcion str() convierte un tipo a cadena
