#TIPO DE DATO STRING
name = "Moises"
last_name = "Ayala"
print(name) #Moises
print(last_name) #Ayala

#concatenacion
full_name = name + last_name
print(full_name) #MoisesAyala

#agregar espacio entre strings
full_name = name + " " + last_name
print(full_name) #Moises Ayala

#uso del aprostrofe
quote1 = "I'm Moises"
quote2 = 'I"M Moises'
print(quote1) #I'm Moises 
print(quote2) #I"M Moises  

#concatenar: manipulacion de formatos string con plantilla
template = "hola, mi nombre es " + name + " y mi apellio es " + last_name
print(template) #hola, mi nombre es Moisesy mi apellio es Ayala

#concatenar: con funcion format
template = "hola, mi nombre es {} y mi apellio es {}".format(name, last_name)
print(template)

#concatenar: con funcion f
template = f"hola, mi nombre es {name} y mi apellio es {last_name}"
print(template)

#concatenar: %s
template = "hola, mi nombre es %s y mi apellio es %s" %(name, last_name)
print(template)

#EJEMPLO ACUMULADO 7 + 8
print("Hola extraño introduce tus datos")
nombre = input("Introduce tu nombre: \n")
print("Hola {} es un gusto conocerte como te apellidas".format(nombre))
apellido = input("Introduce tu apellido: \n")
print(f"Oh! {apellido} vaya tienes un apellido interesante {nombre} ahora dinos que edad tienes")
edad = input("Introduce tu edad: \n")
nueva_edad = str(int(edad)+1)
print("Que maravilla %s aprenderas a programar en tus %s años cuanto tengas %s años ya lo habras logrado" %(nombre, edad, nueva_edad))
