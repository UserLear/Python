#CONTROL DE FLUJO
#.......operadores de comparacion o relacionales
a = 1
b = 2
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

#.......operadores logicos o booleanos binarios
print(a != b and a <= b) #True
print(b < a or b < 10) #True
print(not(a < b)) #False
print(not not(a < b)) #True

#.......declaracion if
name = "moises"
if name == "moises":
    print("hola " + name)

#.......declaracion else
name = input("ingresa tu nombre: \n")
if name == "Moises":
    print("Hola " + name + ", tu nombre mide " + str(len(name)) + " letras")
else: 
    print("No te conozco, pero tu nombre mide " + str(len(name)) + " letras")

#.......declaracion elif
nombre = input("Cual es tu nombre: \n")
print("Hola " + nombre + ", para acceder a nuestro contenido dependera de tu edad")
edad = input("Introduce ahora tu edad: \n")
if int(edad) > 0 and int(edad) < 15: 
    print("Ummm!, lo siento no tengo nada para menores de 15 años")
elif int(edad) >= 16 and int(edad) <= 30:
    print("Te mostraremos opciones de carrera y de negocios que pueden interesarte")
else: 
    print("Tu pasas de los 30, para ti tenemos un mundo oportunidades")

#......declaracion while
nombre = ""
while nombre != "Moises":
    nombre = input("Debes ingresar con tu usuario: \n")
    print("Ese no es tu nombre de usuario")

#.......uso de break
while True:
       print('Escriba su nombre.')
       name = input()
       if name == 'su nombre':
           break
print('¡Gracias!')










