#CONJUNTOS
"""
Caracteristicas:
1. en un conjunto los elementos tienen algo en comun.
2. se relacionan a la teoria de conjuntos de la matematicas.
3. un conjunto se puede modificar.
4. en un conjunto no existe un orden especifico.
5. en un conjunto no existen elementos duplicados.
"""
#creacion de conjuntos con: {}, set()
set_paises = {"honduras", "estados unidos", "panama"}
print(set_paises) #{'panama', 'honduras', 'estados unidos'} segunda llamada {'honduras', 'estados unidos', 'panama'}
print(type(set_paises)) #<class 'set'>

set_capitales = set(["tegucigalpa", "washintong", "san jose"])
print(set_capitales) #{'washintong', 'tegucigalpa', 'san jose'} segunda llamada {'washintong', 'san jose', 'tegucigalpa'}

set_cadena = set("generacion")
print(set_cadena) #{'c', 'n', 'a', 'r', 'o', 'e', 'i', 'g'} segunda llamada {'e', 'g', 'n', 'c', 'a', 'i', 'r', 'o'}

#eliminacion de elementos repetidos
set_paises = {"honduras", "honduras", "estados unidos", "panama"}
print(set_paises) #{'estados unidos', 'panama', 'honduras'} segunda llamada {'honduras', 'estados unidos', 'panama'}

#orden del set
set_numeros = {1, 3, 8, 10, 15, 2, 7}
print(set_numeros) #{1, 2, 3, 7, 8, 10, 15} segunda llamada {1, 2, 3, 7, 8, 10, 15}

set_letras1 = {"a", "z", "b", "x", "f"}
set_letras2 = {"a", "b", "c", "d", "e"}
print(set_letras1) #{'x', 'a', 'b', 'f', 'z'} segunda llamada {'f', 'a', 'x', 'b', 'z'}
print(set_letras2) #{'e', 'd', 'a', 'b', 'c'} segunda llamada {'a', 'd', 'e', 'b', 'c'}

#varios tipos de datos
set_variostipos = {1, "hola", True, 12.1} 
print(set_variostipos) #{'hola', 1, 12.1}

set_cadena ={"hola"}
print(set_cadena) #{'hola'}

set_tupla = set(("hola", "como", "esta", "hola")) #transformar una tupla en conjunto
print(set_tupla) #{'esta', 'como', 'hola'}

set_lista = set([1, 3, 3, 5, 7, 9]) #transformar una lista en conjunto
print(set_lista) #{1, 3, 5, 7, 9}

nueva_lista = list(set_lista) #consiste en transformar el conjunto "set" de nuevo a una lista pero solo con los elementos validados
print(nueva_lista) #[1, 3, 5, 7, 9]



































