#DICCIONARIOS: INSERCION Y ACTUALIZACION
#representar a una persona
persona = {"nombre": "moises",
           "apellido": "ayala mejia",
           "lenguajes": ["python", "javascript"],
           "edad": 32}

#acceder a sus valores por medio de sus llaves
print(persona["nombre"]) #moises

#cambiar valores de las llaves
persona["nombre"] = "emanuel"
print(persona["nombre"]) #emanuel
print(persona) #{'nombre': 'emanuel', 'apellido': 'ayala mejia', 'lenguajes': ['python', 'javascript'], 'edad': 32}

persona["edad"] -= 12
print(persona["edad"])
print(persona) #{'nombre': 'emanuel', 'apellido': 'ayala mejia', 'lenguajes': ['python', 'javascript'], 'edad': 20}

#metodos: append(), del, pop(), items(), 
#append(): añade a la llave 
persona["lenguajes"].append("ingles")
print(persona["lenguajes"]) #['python', 'javascript', 'ingles']
print(persona) #{'nombre': 'emanuel', 'apellido': 'ayala mejia', 'lenguajes': ['python', 'javascript', 'ingles'], 'edad': 20}

#del: elimina la llave seleccionada
del persona["apellido"]
print(persona) #{'nombre': 'emanuel', 'lenguajes': ['python', 'javascript', 'ingles'], 'edad': 20}

#pop(): otro metodo del eliminar
persona.pop("edad")
print(persona) #{'nombre': 'emanuel', 'lenguajes': ['python', 'javascript', 'ingles']}

#items(): devuelve el elemento clave-valor => devuelve una lista de tuplas donde cada elemento es el par clave-valor
print(persona.items()) #dict_items([('nombre', 'emanuel'), ('lenguajes', ['python', 'javascript', 'ingles'])])

#keys(): devuelve las claves del diccionario => en una lista
print(persona.keys()) #dict_keys(['nombre', 'lenguajes'])

#values(): devuelve los valores del diccionario => devuelve una lista
print(persona.values()) #dict_values(['emanuel', ['python', 'javascript', 'ingles']])

