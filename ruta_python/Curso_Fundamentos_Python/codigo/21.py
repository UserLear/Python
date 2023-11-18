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
        print("\n Elige: 1. para aprender del apostrofe, 2. para aprender del caracter de escape. \n")
        opcion = input("Introduce el numero: \n")
        if opcion == '1':
            print("""El apostrofe se utiliza en el idioma ingles para realizar contracciones utilizando el verbo To Be, \n
              Por ejemplo: 
              I am: I'm 
              You are: You're 
              He is: He's 
              She is: She's 
              You are: You're 
              We are: We're 
              They are: They're \n""")
        elif opcion == "2": 
            def entrada():
                caracter_escape = input("Introduce siempre la \\ mas el caracter deseado: \n")
                return  caracter_escape
            print("\n El caracter de escape (\\) se utiliza para introducir caracteres especiales en la cadena.\n")
            cadena_prueba1 = "Esta cadena es de prueba"
            cadena_prueba2 = "experimenta con ella \n"
            print("""1. \\: para introducir una diagonal invertida.
2. \n""")
            seleccion = input("Selecciona el numero del tema para ver como funiona: \n")
            if seleccion == "1":
                caracter = entrada()
                print(cadena_prueba1 + caracter + " " + cadena_prueba2)


        
    elif numero == "2":
        print("Utilizaremos la palabra reservada 'in' para buscar un caracter dentro de una cadena.")
        

         
