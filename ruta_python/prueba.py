import time
while True:
    print('''Pulsa 'q' para salir.
1. Uso de apostrofe (') o caracter de escape (\\) dentro de cadenas.
2. Indexacion. 
. buscar un caracter o cadena dentro de un sting.
. \n''')
    time.sleep(0.001)
    numero = input("Introduce el numero: \n")
    if numero == "q":
        print("Fue un gusto contribuir a su arendizaje, hasta pronto.\n")
        break
    elif numero == "1":     
        print("""\nElige: 
1. para aprender del apostrofe (\'). 
2. para aprender del caracter de escape (\\). \n""")
        opcion = input("Introduce el numero: \n")
        if opcion == '1':
            print("""\nDefinicion:
El apostrofe se utiliza en el idioma ingles para realizar contracciones utilizando el verbo To Be.
Para esto debes recordar que existen dos formas que crear cadenas, una es utilizando comillas simple (') otra es utilizando comilla doble (").
              1. comilla simple (\'): consiste en crear una cadena con comilla doble (\") e introducir la comilla simple (\"I\'m Moises\").
              2. commilla doble (\"): consiste en crear una cadena con comilla si (\'Le decian el \"Holandez\"\').
               \n""")
    



























