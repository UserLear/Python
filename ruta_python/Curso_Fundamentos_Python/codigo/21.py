#programa: explica la manipulacion de cadenas
print("\nAcontinuacion te presentamos un programa que te explicara la manipulacion de cadenas.")
print("Acontinuacion selecciona el numero del tema que deseas aprender.\n")
while True:
    print('''Pulsa 'q' o '' para salir.
1. Uso de apostrofe (') o caracter de escape (\\) dentro de cadenas.
2. Indexacion. 
3. Slicing (particion de cadenas).
4. Operador "in" y "not in": buscar un caracter o subcadena dentro de otra cadena.
5. Metodos: booleans
6. Metodos: modificacion de cadena\n''')
    numero = input("Introduce el numero: \n")
    if numero == "q" or numero == "":
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
        elif opcion == "2": 
            print("""\nDefinicion:
El caracter de escape (\\) se utiliza para introducir caracteres especiales en la cadena.\n""")
            print("""1. \\: para introducir una diagonal invertida, introduce doble diagonal invertida en la cadena.
                    Ejemplo:
                    creamos la cadena: \"Hola Marcos \\\ Hola Luis\" al imprimirla devolvera => Hola Marcos \\ Hola Luis.
2. \"\" o \'\': para encerrar entre comillas una palabra.
                    Ejemplo:
                    creamos la cadena: \"Marcos te dicen el \\\"Casanoba\\\"\" al imprimirla devolvera => Marcos te dicen el \"Casanoba\"
3. \\t: para añadir espacios variables entre cadena.
                    Ejemplo: 
                    creamos la cadena: \"A Nicolas le gusta\\t saltar\" al imprimirla devolvera => A Nicolas le gusta        saltar
                    creamos la cadena: \"A Nicolas le gusta\\t\\t saltar\" al imprimirla devolvera => A Nicolas le gusta                  saltar
4. \\n: para pasar la cadena a una nueva linea.
                    Ejemplo:2
                    creamos la cadena: \"La mayoria de personas\\nson conflictivas\" al imprimirla devolvera => La mayoria de personas 
                                                                                                             son conflictivas
5. r: cuerdas en bruto.
                    Ejemplo:
                    creamos la cadena: r\"Nosotros podemos\\ trabajar juntos\" al imprimirla devolvera => Nosotros podemos\\ trabajar juntos
                  \n""")
            
    elif numero == "2":
        print("""Definicion:
La indexacion consiste en acceder a los elementos de una cadena utilizando un indice (numero).""")
        print("""Cada elemento que compone una cadena tiene un numero asignado comenzando del cero (0) hasta el ultimo elemento. 
Un mejor uso de la indexacion consistiria en asignar primero una cadena a una variable para luego usar esa variable con indexacion.\n
                Ejemplo:""")
        palabra = input("\t\tCreamos la variable llamada \"palabra\" y guardamos la siguiente cadena: ")
        print(f"""\n\t\tLa sintaxis para acceder a cada elemento de la variable llamada \"palabra\" es palabra[indice] (llamada notacion corchete), 
                Ejemplo:
                Si quieres acceder al elemento cero que es \"{palabra[0]}\" en la cadena basta con escribir \"palabra[0]\" \n""")
        print(f"\t\tAhora practica con otros indices de la cadena \"{palabra}\"")
        while True:
            print("\t\tIngresa \"q\" para salir")
            print(f"\t\tLa longitud de la cadena \"{palabra}\" es de \"0\" a \"{(len(palabra)-1)}\" prueba entre esos numeros.")
            indice = input("\t\tIntroduce un numero: ")
            if indice == "q":
                break
            conver_indice = int(indice)
            if palabra[conver_indice] == " ":
                print(f"\n\t\tToma en cuenta que los espacios en blanco tambien tiene un indice asignado que en este caso seria {conver_indice}\n")
                continue
            print(f"\t\tLa sintaxis seria: \"palabra[{conver_indice}]\" y te devolvera el elemento en esa posicion que seria: \"{palabra[conver_indice]}\"\n")
    elif numero == "3":
        print("""Definicion: 
Slicing consiste en partir una cadena y devolver la seccion requerida, utilizando los indices.""")
        print("""Para este tema crearemos una variable llamada "palabra" a la cual le asignaremos un valor de cadena  y
manipularla con slicing.\n""")
        while True:
            print("""\t\tSelecciona el subtema, donde "a" y "b" son numeros enteros:
                  Ingresa "q" o "" para salir.
                  1. [a:b] => rango.
                  2. [a:] => indice de inicio definido.
                  3. [:b] => indice final definido.
                  4. [:] => sin indices.""")
            opcion = input("\t\tIntroduce un numero: ")
            if opcion == "q" or "":
                break
            if opcion == "1":
                print("""Definicion:
El "rango" consiste en utilizar ambos extremos ("a", "b") de los parentesis [a:b] para devolver la cadena que se 
encuentra entre esos valores, el primer numero "a" del rango es considerado, el segundo es ignorado "b".\n
                Ejemplo:""")
                palabra = input("\t\tIntroduce la cadena: ")
                print(f"\t\tLa cadena \"{palabra}\" mide de \"0\" a \"{len(palabra)-1}\".")
                print(f"\t\tSi quieres toda la cadena \"{palabra}\" deberas introducir entre los parentesis [0:{len(palabra)}].\n")
                print(f"\t\tBueno es hora que tu lo intentes:")
                while True:
                    print("\t\tIngresa \"q\" o \"\" para salir.")
                    numero1 = input("\t\tIntroduce \"a\": ")
                    if numero1 == "q" or numero1 == "":
                        break
                    conver_numero1 = int(numero1)
                    numero2 = input("\t\tIntroduce \"b\": ")
                    conver_numero2 = int(numero2)
                    print(f"\t\tLa sintaxis seria: \"palabra[{numero1}:{numero2}]\" y te devolvera los elementos entre ese rango: {palabra[conver_numero1:conver_numero2]}\n")
            elif opcion == "2":
                print("""Definicion:
El "indice de inicio definido" significa que solo definimos de donde comenzara la seleccion y tomara a partir de 
ese indice todos los demas hasta el final de la cadena.\n
                Ejemplo:""")
                palabra = input("\t\tIntroduce la cadena: ")
                print(f"\t\tLa cadena \"{palabra}\" mide de \"0\" a \"{len(palabra)-1}\".")
                print(f"\t\tSi quieres iniciar la cadena \"{palabra}\" a partir de un indice especifico deberas introducir el primer indice [\"a\":].\n")
                print(f"\t\tBueno es hora que tu lo intentes:")
                while True:
                    print("\t\tIngresa \"q\" o \"\" para salir.")
                    numero1 = input("\t\tIntroduce \"a\": ")
                    if numero1 == "q" or numero1 == "":
                        break
                    conver_numero1 = int(numero1)
                    print(f"\t\tLa sintaxis seria: \"palabra[{numero1}:]\" y te devolvera los elementos entre el indice \"a\" y el ultimo elemento de la cadena: {palabra[conver_numero1:]}\n")
            elif opcion == "3":
                print("""Definicion:
El "indice final definido" consiste en determinar el punto donde terminara la seleccion de los elementos de una
cadena comenzando desde el indice "0" hasta el indice "b" definido por nosotros.\n
                Ejemplo:""")
                palabra = input("\t\tIntroduce la cadena: ")
                print(f"\t\tLa cadena \"{palabra}\" mide de \"0\" a \"{len(palabra)-1}\".")
                print(f"\t\tSi quieres devolver la cadena \"{palabra}\" iniciando de \"0\" y que termine hasta \"b\" introduce entre parentesis: [:\"b\"].\n")
                print(f"\t\tBueno es hora que tu lo intentes:")
                while True:
                    print("\t\tIngresa \"q\" o \"\" para salir.")
                    numero1 = input("\t\tIntroduce \"b\": ")
                    if numero1 == "q" or numero1 == "":
                        break
                    conver_numero1 = int(numero1)
                    print(f"\t\tLa sintaxis seria: \"palabra[:{numero1}]\" y te devolvera los elementos entre el indice \"0\" y el indice \"b\" de la cadena: {palabra[:conver_numero1]}\n")
            elif opcion == "4":
                print("""Definicion:
"Sin indices" devuelve la cadena entera sin preocuparse cual es el inicio o final de la cadena.\n
                Ejemplo:""")
                palabra = input("\t\tIntroduce la cadena: ")
                print(f"\t\tLa cadena \"{palabra}\" mide de \"0\" a \"{len(palabra)-1}\".")
                print(f"\t\tSi quieres devolver la cadena \"{palabra}\" iniciando de \"0\" y que termine hasta \"{len(palabra)-1}\" introduce entre parentesis: [:].")
                print(f"\t\tLa sintaxis seria: \"palabra[:]\" y te devolvera los elementos entre el indice \"0\" y el indice \"{len(palabra)-1}\" de la cadena: {palabra[:]}\n")
            else:
                print("\t\tDebes introducir un numero valido de subtema.\n")
                if True:
                    continue
    elif numero == "4":
        print("""Definicion:
El operador "in" y "not in" se utilizan para verificar si una cadena contiene una sub-cadena o caracter en si misma y 
devuelve un valor boolean (True, False), si la encuentra o no, "in" devuelve "True" si existe o "False" sino, "not in" 
devuelve el valor inverso a "in" si la encuentra, si existe devuelve "False" sino devuelve "True".""")
        print("""Para este tema crearemos una variable llamada "palabra" a la cual le asignaremos un valor de cadena  y
manipularla con "in" o "not in".\n""")
        while True:
            print("""\t\tSelecciona el subtema:
                  Ingresa "q" o "" para salir.
                  1. in => verificacion (esta en).
                  2. not in => negacion (no esta en).""")
            opcion = input("\t\tIntroduce un numero: ")
            if opcion == "q" or "":
                break
            if opcion == "1":
                print("""Definicion:
El operador "in" lo utilizamos para verificar la existencia de una sub-cadena dentro de otra cadena y nos devolvera "True" 
si la encuentra o "False" si no.\n
                Ejemplo:""")
                palabra = input("\t\tIntroduce la cadena: ")
                print(f"\t\tUna vez inicializada la variable \"palabra\" trabajaremos con la cadena \"{palabra}\"")
                print(f"\t\tSi quieres verificar si \"{palabra[0:2]}\" esta en la cadena \"{palabra}\" la sintaxis es: \"{palabra[0:2]}\" in palabra")
                print(f"\t\tBueno es hora que tu lo intentes:\n")
                while True:
                    print("\t\tIngresa \"q\" o \"\" para salir.")
                    subcadena = input(f"\t\tIntroduce la subcadena que buscas en \"{palabra}\": ")
                    if subcadena == "q" or subcadena == "":
                        break
                    verificacion = subcadena in palabra
                    if verificacion == True:
                        print(f"\t\tComo puedes ver \"{subcadena}\" si esta contenida en \"{palabra}\" por tanto devuelve: True\n")
                    elif verificacion == False:
                        print(f"\t\tComo puedes ver \"{subcadena}\" no esta contenida en \"{palabra}\" por tanto devuelve: False\n")
            if opcion == "2":
                print("""Definicion:
El operador "not in" hace una verificacion inversa de la existencia de un caracter o segmento dentro de otra cadena y devolvera
"True" si no se encuentra o "False" si esta contenida, es como decir "X caracter no esta en Y palabra" si esta devolvera "False"
si no devolvera "True".\n
                      Ejemplo:""")
                palabra = input("\t\tIntroduce la cadena: ")
                print(f"\t\tUna vez inicializada la variable \"palabra\" trabajaremos con la cadena \"{palabra}\"")
                print(f"\t\tSi quieres verificar si \"{palabra[0:2]}\" esta en la cadena {palabra} la sintaxis es: \"{palabra[0:2]}\" not in palabra")
                print(f"\t\tBueno es hora que tu lo intentes:\n")
                while True:
                    print("\t\tIngresa \"q\" o \"\" para salir.")
                    subcadena = input(f"\t\tIntroduce la subcadena que buscas en \"{palabra}\": ")
                    if subcadena == "q" or subcadena == "":
                        break
                    verificacion = subcadena not in palabra
                    if verificacion == True:
                        print(f"")
                        print(f"\t\tComo puedes ver \"{subcadena}\" si esta contenida en \"{palabra}\" por tanto devuelve: True\n")
                    elif verificacion == False:
                        print(f"\t\tComo puedes ver \"{subcadena}\" no esta contenida en \"{palabra}\" por tanto devuelve: False\n")
    elif numero == "5":
        print("""Definicion:
Los "metodos booleans" son metodos que devuelven tipos de datos booleans.
Para estos metodos utilizaremos listas para evaluar y ver su funcionamiento.""")
        while True:
            print("""\n\t\tSelecciona el subtema:
                  Ingresa "q" o "" para salir.
                  1. isupper.
                  2. islower.
                  3. isalpha.
                  4. isalnum
                  5. \n""")
            opcion = input("\t\tIntroduce un numero: ")
            if opcion == "q" or opcion == "":
                break
            if opcion == "1":
                print("""Definicion:
El metodo "isupper" devuelve "True" si la cadena pasada tiene al menos un caracter literal mayuscula y devuelve "False"
si contiene al menos un caracter literal en minuscula o si esta conformado en totalidad de caracteres no literales.
                Ejemplo:\n""")
                lista_prueba = ["Moises", "MOISES", "moises", "moises1", "MOISES1", "12345", "M78654", "9874L", "AYALa", "", " ", "/"] 
                print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                for i in lista_prueba:
                    print(f"\t\tmetodo isupper(): {i}: {i.isupper()}")
            elif opcion == "2":
                print("""Definicion:
El metodo "islower" devuelve "True" si la cadena pasada no contiene ningun caracter literal en mayuscula y devuelve "False"
si contiene al menos un caracter literal en mayuscula o si esta conformado en totalidad de caracteres no literales.
                Ejemplo:\n""")
                lista_prueba = ["Moises", "MOISES", "moises", "moises1", "MOISES1", "12345", "m78654", "ayalA", "AYALa"] 
                print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                for i in lista_prueba:
                    print(f"\t\tmetodo islower(): {i}: {i.islower()}")
            elif opcion == "3":
                print("""Definicion:
El metodo "isalpha" devuelve "True" si la cadena se compone solo de caracteres literales y devuelve "False" en caso contrario.
                Ejemplo:\n""")
                lista_prueba = ["Moises", "MOISES", "moises", "moises1", "Moises1", "12345", "ayalA", "AYALa", "MOISES "] 
                print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                for i in lista_prueba:
                    print(f"\t\tmetodo isalpha(): {i}: {i.isalpha()}")
            elif opcion == "4":
                print("""Definicion:
El metodo "isalnum" devuelve "True" si la cadena esta compuesta de caracteres solo de caracteres literales o si incluye
caracteres numericos, cualquier otro caracter diferente a estos devuelve "False".
                Ejemplo:\n""")
                lista_prueba = ["Moises", "MOISES", "moises", "moises1", "Moises1", "12345", " ", "MOISES ", "/"] 
                print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                for i in lista_prueba:
                    print(f"\t\tmetodo isalnum(): {i}: {i.isalnum()}")
            
            
                
                



                
                



                
                
                


                

        
        
        

         
