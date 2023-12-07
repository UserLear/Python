"""
En este desafío, se te proporcionará un diccionario llamado person que contiene información sobre una persona. Tu reto es realizar las siguientes operaciones en orden:

Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
Eliminar el elemento del diccionario con la llave "age".
Imprimir una lista con las llaves del diccionario.
Imprimir una lista con los valores del diccionario.
Ejemplo:

Input:
person = {
    "name": "Nicolas",
    "lastName": "Molina",
    "age": 29}

Output:
["name", "lastName", "twitter"]
["Felipe", "Molina", "@nicobytes"]

Recuerda que debes realizar las operaciones en el orden indicado y utilizar las funciones y métodos de los diccionarios de Python apropiados para cada tarea.
"""
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29 }
print(person) #{'name': 'Nicolas', 'lastName': 'Molina', 'age': 29}

#agregar el elemento "twitter" con calor "@nicobytes"
person["twitter"] = "@nicobytes"
print(person) #{'name': 'Nicolas', 'lastName': 'Molina', 'age': 29, 'twitter': '@nicobytes'}

#actualizar el valor de la clave "name" con el valor "felipe"
person["name"] = "felipe"
print(person) #{'name': 'felipe', 'lastName': 'Molina', 'age': 29, 'twitter': '@nicobytes'} 

#eliminar el elemento del diccionario con la llave "age"
del person["age"]
print(person) #{'name': 'felipe', 'lastName': 'Molina', 'twitter': '@nicobytes'}

#imprimir una lista con las llaves del diccionario
llaves = person.keys() 
print(llaves) #dict_keys(['name', 'lastName', 'twitter'])

#imprimir lista de claves del diccionario
print(person.values()) #dict_values(['felipe', 'Molina', '@nicobytes'])



