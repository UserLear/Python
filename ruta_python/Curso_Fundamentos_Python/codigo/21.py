#programa: explica la manipulacion de cadenas
print("Acontinuacion te presentamos un programa que te explicara la manipulacion de cadenas.")
print("Acontinuacion selecciona el numero del tema que te llama la atencion.")
while True:
    print('''1. Uso de apostrofe  o caracter de escape dentro de cadenas.
2. buscar un caracter o cadena dentro de un sting.
3. ''')
    numero = input("Introduce el numero: \n")
    if numero == "q":
        print("Fue un gusto contribuir a su arendizaje, hasta pronto.")
        break
    elif numero == "1":     
        print("Elige: 1 para aprender del apostrofe o 2 para aprender del caracter de escape.")
        opcion = input("Introduce el numero: ")
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
        else: 
            print("El caracter de escape (\\) se utiliza para introducir caracteres especiales en la cadena.")
            cadena_prueba1 = "Esta cadena es de prueba"
            cadena_prueba2 = "experimenta con ella"
            print("""1. \\: se pasa doble para que """)
            caracter_escape = input("Introduce el caracter: ")

            print("1. \\: ")
        
    elif numero == "2":
        print("Utilizaremos la palabra reservada 'in' para buscar un caracter dentro de una cadena.")
        

         
