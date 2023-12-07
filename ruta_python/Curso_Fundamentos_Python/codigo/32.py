#LOOPS: FOR
#for: sirve para iterar tipos de datos iterables,
for element in range(10,20):
    print(element)
"""
10
11
12
13
14
15
16
17
18
19
"""

lista = [23, 45, 67, 89, 43]
for i in lista:
    print(i)
"""
23
45
67
89
43
"""

tupla = ("jose", "marcos", "esteban", "luis")
for i in tupla:
    print(i)
"""
jose
marcos
esteban
luis
"""

diccionario = {
    "nombre": "camisa", 
    "precio": 100,
    "descuento": 20
}
for i in diccionario:
    print(diccionario[i])
"""
camisa
100
20
"""

for key, value in diccionario.items():
    print(key, "=>", diccionario[key])
"""
nombre => camisa
precio => 100
descuento => 20
"""

for key, value in diccionario.items():
    print(key, "=>", value)
"""
nombre => camisa
precio => 100
descuento => 20
"""

personas = [
    {
        "nombre": "juan",
        "edad": 45
    },
    {
        "nombre": "pablo",
        "edad": 30
    },
    {
        "nombre": "elias",
        "edad": 25    
    }
]

for persona in personas:
    print(persona) 
"""
{'nombre': 'juan', 'edad': 45}
{'nombre': 'pablo', 'edad': 30}
{'nombre': 'elias', 'edad': 25}
"""

for persona in personas:
    print("nombre => ", persona["nombre"])
"""
nombre =>  juan
nombre =>  pablo
nombre =>  elias
"""


