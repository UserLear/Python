#TRANSFORMACION DE TIPOS caracteristica de python es un tipado dinamico
name = "Nicolas"
print(type(name)) #<class 'str'>

#en python podemos cambiar el tipo de valor asignado a una variable con reasignacion
name = 12
print(type(name)) #<class 'int'>

#cambiar la misma variable a un booleano
name = True
print(type(name)) #<class 'bool'>

#python interpreta que queremos hacer al concatenar tipos de datos
print("nicolas" + "molina") #nicolasmolina
print(10 + 20) #30

#print("nicolas" + 20) esto nos dice que podemos concatenar solo tipos de datos iguales

#si queremos combinar diferentes tipos de datos debemos hacer la conversion
age = 32
print("hola juan como estas" + str(age)) #hola juan como estas32

#utilizando input: input por regla del lenguaje devuelve un str
age = input("escribe tu edad: ")
print(type(age)) #<class 'str'>
print(f"tu edad es {age} dentro de un año tendras {int(age)+1}") #tu edad es 32 dentro de un año tendras 33

