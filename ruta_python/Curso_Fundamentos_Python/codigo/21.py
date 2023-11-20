#programa: explica la manipulacion de cadenas
print("Acontinuacion te presentamos un programa que te explicara la manipulacion de cadenas.")
print("Acontinuacion selecciona el numero del tema que te llama la atencion.\n")
while True:
    print('''Para salir introduce 'q'.
1. Uso de apostrofe (') o caracter (\) de escape dentro de cadenas.
2. buscar un caracter o cadena dentro de un sting.
3. \n''')
    numero = input("Introduce el numero: \n")
    if numero == "q":
        print("Fue un gusto contribuir a su arendizaje, hasta pronto.")
        break
    elif numero == "1":     
        print("""\nElige: 
1. para aprender del apostrofe, 
2. para aprender del caracter de escape. \n""")
        opcion = input("Introduce el numero: \n")
        if opcion == '1':
            print("""\nEl apostrofe se utiliza en el idioma ingles para realizar contracciones utilizando el verbo To Be.
Para esto debes recordar que existen dos formas que crear cadenas, una es utilizando comillas simple (') otra es utilizando comilla doble (")
              1. comilla simple (\'): comunmente la utilizamos en el idioma ingles para hacer una contracciones (\"I\'m Moises\").
              2. commilla doble (\"): comunmente la utilizamos para resaltar un termino entre comillas (\'Le decian el \"Holandez\" \').
               \n""")
        elif opcion == "2": 
            print("\n El caracter de escape (\\) se utiliza para introducir caracteres especiales en la cadena.\n")
            print("""1. \\: para introducir una diagonal invertida, introduce doble diagonal invertida en la cadena.
                    Ejemplo: Hola Marcos \\ Hola Luis.
2. \n""")


        
    elif numero == "2":
        print("Utilizaremos la palabra reservada 'in' para buscar un caracter dentro de una cadena.")
        

         
