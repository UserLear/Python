#programa: explica la manipulacion de cadenas
print("\nAcontinuacion te presentamos un programa que te explicara la manipulacion de cadenas.")
print("Acontinuacion selecciona el numero del tema que deseas aprender.\n")
while True:
    print('''Pulsa 'q' o '' para salir.
1. Uso de apostrofe (') o caracter de escape (\\) dentro de cadenas.
2. Indexacion de cadena. 
3. Slicing de cadenas.
4. Operador "in" y "not in": buscar un caracter o subcadena dentro de otra cadena.
5. Metodos.
6. Obtener codigo ASCII.\n''')
    numero = input("Introduce el numero del tema:\n")
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
La indexacion consiste en acceder a los elementos de una cadena utilizando un indice (numero) de izquierda a derecha, cada elemento que compone 
una cadena tiene un numero asignado comenzando del cero (0) hasta el ultimo elemento, como mejor uso de la indexacion se inicializa una variable 
con la cadena que vamos a manipular, la sintaxis es: "variable[indice]".
Caracteristicas:
        1. Podemos utilizar indices negativos para acceder a la cadena de derecha a izquierda.
        2. Genera "Error" si ingresamos un indice mayor a la longitud de cadena, por tanto midamos la cadena
           para determinar su longitud y evitar errores con la funcion len().
        3. Los espacios en blanco tambien tienen su indice asignado.
                Ejemplo:\n""")
        cadena = "manipulacion"
        indice = 2
        print("\tPara indices enteros no negativos (0, 1, 2, 3, ...)")
        print(f"\t\tLa cadena que vamos a manipular es: \"{cadena}\"")
        print(f"\t\tLa longitud de la cadena es: \"{len(cadena)}\"")
        print(f"\t\tEl indice que vamos a buscar es: \"{indice}\"\n")
        indice1 = cadena[indice]
        print(f"\tOuput: \"{indice1}\"\n")
        indicen = -2
        print("\tPara indices enteros negativos (-1, -2, -3, ...)")
        print(f"\t\tLa cadena que vamos a manipular es: \"{cadena}\"")
        print(f"\t\tLa longitud de la cadena es: \"{len(cadena)}\"")
        print(f"\t\tEl indice que vamos a buscar es: \"{indicen}\"\n")
        indice1 = cadena[indicen]
        print(f"\tOuput: \"{indice1}\"\n")
        print("\t\tEs momento que tu lo intentes.")
        while True:
            print("\t\tIngresa \"q\" para salir")
            cadena = input("\t\tIngresa la cadena: ")
            indice = input("\t\tIntroduce un numero: ")
            if cadena == "q" or cadena == "":
                break
            conver_indice = int(indice)
            print(f"\n\tOuput: \"{cadena[conver_indice]}\"\n")
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
                  4. [:] => sin indices.
                  5. [a:b:c] => saltos. 
                  6. [::c] => iteracion inversa.""") #pendiente agregar 5, 6
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
Los "metodos" son funciones que se utilizan ya sea para verificar si una cadena cumple con ciertas caracteristicas "Metodos: booleans" o 
para modificar una cadena y obtener algo nuevo "Metodos: modificacion de cadena".\n""")
        while True:
            print("""\t\tSelecciona el subtema:
                  Ingresa "q" o "" para salir.
                  1. Funcion dir().
                  2. Metodos: booleans.
                  3. Metodos: modificacion de cadenas.""")
            opcion = input("\t\tIntroduce un numero: ")
            if opcion == "q" or opcion == "":
                break
            elif opcion == "1":
                print("""Definicion:
La funcion "dir()" devuelve todos los metodos que se pueden utilizar sobre una cadena, la sintaxis es: "dir(cadena)".
                Ejemplo:\n""")
                cadena = ""
                print(f"\t\tBasta con pasar una cadena vacia ("") para ver los metodos disponibles.")
                metodos = dir(cadena)
                print(f"\t\t{metodos}")
            elif opcion == "2":
                print("""Definicion:
Los "metodos booleans" son metodos que devuelven tipos de datos booleans.
Para estos metodos utilizaremos listas para evaluar y ver su funcionamiento.""")
                while True:
                    print("""\n\t\tSelecciona el subtema:
                        Ingresa "q" o "" para salir.
                        1. isupper().
                        2. islower().
                        3. isalpha().
                        4. isalnum().
                        5. isdecimal().
                        6. isspace().
                        7. istitle().
                        8. startswith().
                        9. endswith().\n""")
                    opcion = input("\t\tIntroduce un numero: ")
                    if opcion == "q" or opcion == "":
                        break
                    if opcion == "1":
                        print("""Definicion:
El metodo "isupper()" devuelve "True" si la cadena pasada tiene al menos un caracter literal mayuscula y devuelve "False"
si contiene al menos un caracter literal en minuscula o si esta conformado en totalidad de caracteres no literales.
                Ejemplo:\n""")
                        lista_prueba = ["Moises", "MOISES", "moises", "moises1", "MOISES1", "12345", "M78654", "9874L", "AYALa", "", " ", "/"] 
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo isupper(): {i}: {i.isupper()}")
                    elif opcion == "2":
                        print("""Definicion:
El metodo "islower()" devuelve "True" si la cadena pasada no contiene ningun caracter literal en mayuscula y devuelve "False"
si contiene al menos un caracter literal en mayuscula o si esta conformado en totalidad de caracteres no literales.
                Ejemplo:\n""")
                        ista_prueba = ["Moises", "MOISES", "moises", "moises1", "MOISES1", "12345", "m78654", "ayalA", "AYALa"] 
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo islower(): {i}: {i.islower()}")
                    elif opcion == "3":
                        print("""Definicion:
El metodo "isalpha()" devuelve "True" si la cadena se compone solo de caracteres literales y devuelve "False" en caso contrario.
                Ejemplo:\n""")
                        lista_prueba = ["Moises", "MOISES", "moises", "moises1", "Moises1", "12345", "ayalA", "AYALa", "MOISES "] 
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo isalpha(): {i}: {i.isalpha()}")
                    elif opcion == "4":
                        print("""Definicion:
El metodo "isalnum()" devuelve "True" si la cadena esta compuesta de caracteres solo de caracteres literales o si incluye
caracteres numericos, cualquier otro caracter diferente a estos devuelve "False".
                Ejemplo:\n""")
                        lista_prueba = ["Moises", "MOISES", "moises", "moises1", "Moises1", "12345", " ", "MOISES ", "/"] 
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo isalnum(): {i}: {i.isalnum()}")
                    elif opcion == "5":
                        print("""Definicion:
El metodo "isdecimal()" devuelve "True" solo cuando la cadena esta compuesta por caracteres numericos, devuelve "False" en caso
contrario.
                Ejemplo:\n""")
                        lista_prueba = ["Moises", "MOISES", "moises", "moises1", "Moises1", "12345", " ", "MOISES ", "/"] 
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo isdecimal(): {i}: {i.isdecimal()}")
                    elif opcion == "6":
                        print("""Definicion:
El metodo "isspace()" devuelve "True" solo cuando la cadena esta compuesta por espacio o caracter de escape de nueva linea, en
caso contrario devuelve "False".
                Ejemplo:\n""")
                        lista_prueba = ["Moises", "MOISES", "moises", "moises1", "Moises1", "12345", " ", "MOISES ", "/", "\n"] 
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo isspace(): {i}: {i.isspace()}")
                    elif opcion == "7":
                        print("""Definicion:
El metodo "istitle()" devuelve "True" cuando la cadena comienza con un literal en mayuscula sin importar los demas elementos, 
caso contrario devolvera "False".
                Ejemplo:\n""")
                        lista_prueba = ["Moises", "MOISES", "moises", "moises1", "Moises1", "12345", " ", "MOISES ", "/", "\n", "M34567", "J43/"] 
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo istitle(): {i}: {i.istitle()}")
                    elif opcion == "8":
                        print("""Definicion:
El metodo "startswith()" devuelve "True" al verificar que una cadena comienza de forma totalmente identica con el valor que pasamos, caso
contrario devuelve "False".
                Ejemplo:\n""")
                        cadena = "Era una epoca muy dificil."
                        lista_prueba = ["E", "Era", "ra", "una", "era", "dificil", "Era una epoca muy dificil"]
                        print(f"\t\tLa cadena de comparacion seria: \"{cadena}\"")
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo startswith(): {i}: {cadena.startswith(i)}")
                    elif opcion == "9":
                        print("""Definicion:
El metodo "endswith()" devuelve "True" al verificar que una cadena termina de forma totalmente identica con el valor que le pasamos, caso
contrario devuelve "False".
                Ejemplo:\n""")
                        cadena = "Esta historia comenzo en 1991."
                        lista_prueba = ["Esta", "en", ".", "1991.", "Esta historia comenzo en 1991.", "1."]
                        print(f"\t\tLa cadena de comparacion seria: \"{cadena}\"")
                        print(f"\t\tPara este metodo utilizaremos la lista: {lista_prueba}")
                        for i in lista_prueba:
                            print(f"\t\tmetodo endswith(): {i}: {cadena.endswith(i)}")
            elif opcion == "3":
                print("""Definicion:
Los "metodos de modificacion" son metodos que modifican las cadenas.
Para estos metodos utilizaremos listas para evaluar y ver su funcionamiento.""")
                while True:
                    print("""\n\t\tSelecciona el subtema:
                        Ingresa "q" o "" para salir.
                        1. join().
                        2. split().
                        3. split(): con doble parametro
                        4. partition().
                        5. rjust().
                        6. ljust().
                        7. center().
                        8. strip().
                        9. rstrip().
                        10. lstrip().\n""")
                    opcion = input("\t\tIntroduce un numero: ")
                    if opcion == "q" or opcion == "":
                        break 
                    if opcion == "1":
                        print("""Definicion:
El metodo "join()" se utiliza para incrustar un caracter en los espacios en blanco de una cadena y asi devolver
una nueva cadena, la sintaxis es: "caracter.join(cadena)", devuelve una cadena.
Caracteristicas:
        1. El caracter se añade desde el primer elemento al lado derecho y ternina al lado izquierdo del ultimo 
           elemento.
        2. El caracter se añade a ambos lados de los elementos que estan entre los extremos.
        3. El caracter ignora los espacios en blanco.
                Ejemplo:\n""")
                        cadena = "Moises Emanuel Ayala Mejia"
                        caracter = ["!", "#", "$", "%"]
                        print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                        print(f"\t\tLos caracteres que utilizaremos son: {caracter}\n")
                        for k in caracter:
                           join = k.join(cadena)
                           print(f"\tOuput: {join}\n")
                        print("\t\tEs momento que lo intentes.")
                        while True:
                           print("\t\tIngresa \"q\" p \"\" para salir.")
                           cadena = input("\t\tIntroduce la cadena: ")
                           if cadena == "q" or cadena == "":
                              break
                           caracter = input("\t\tIntoduce el caracter: ")
                           print(f"\t\tLa cadena es: \"{cadena}\" y el caracter es: \"{caracter}\"\n")
                           join = caracter.join(cadena)
                           print(f"\tOuput: {join}\n")
                    if opcion == "2":
                        print("""Definicion:
El metodo "split()" se utiliza para identificar un caracter dentro de una cadena al identificarlo lo elimina y 
devuelve una lista, la sintaxis es: "cadena.split(caracter)".
                Ejemplo:\n""")
                        cadena = "Moises-Emanuel-Ayala-Mejia"
                        caracter = "-"
                        print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                        print(f"\t\tEl caracter que eliminariamos es: \"{caracter}\"\n")
                        lista = cadena.split(caracter)
                        print(f"\tOuput: {lista}\n")
                        print("\t\tEs momento que lo intentes.")
                        while True:
                           print("\t\tIngresa \"q\" p \"\" para salir.")
                           cadena = input("\t\tIntroduce la cadena: ")
                           if cadena == "q" or cadena == "":
                               break
                           caracter = input("\t\tIntoduce el caracter: ")
                           print(f"\t\tLa cadena es: \"{cadena}\" y el caracter a eliminar es: \"{caracter}\"\n")
                           split = cadena.split(caracter)
                           print(f"\t\t{split}\n")
                    if opcion == "3":
                        print("""Definicion:
El metodo "split() con doble parametro" se utiliza para identificar un caracter dentro de una cadena y el otro
parametro debe ser un numero que sera la cantidad de esos caracteres que se eliminaran, la sintaxis es: 
"cadena.split(caracter, numero)."
Caracteristicas:
        1. Puedes pasar solo el parametro caracter y eliminara todos los caracteres que esten en la cadena. 
        2. Devolvera "Error" si el numero que introduces es mayor que los caracteres existentes.
        3. Devolvera "Error" si el caracter que introduces no existe. 
                Ejemplo:\n""")
                        cadena = "Moises-Emanuel-Ayala-Mejia-03-05-1991"
                        caracter = "-"
                        veces = 4
                        print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                        print(f"\t\tEl caracter a eliminar es: \"{caracter}\"")
                        print(f"\t\tEl numero de veces a eliminar es: \"{veces}\"\n")
                        lista = cadena.split(caracter,4)
                        print(f"\tOuput: {lista}\n")
                        print("\t\tEs momento que lo intentes.")
                        while True:
                            print("\t\tIngresa \"q\" p \"\" para salir.")
                            cadena = input("\t\tIntroduce la cadena: ")
                            if cadena == "q" or cadena == "":
                               break
                            caracter = input("\t\tIntoduce el caracter: ")
                            numero = input("\t\tIntoduce el numero: ")
                            conver_numero = int(numero)
                            print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                            print(f"\t\tEl caracter a eliminar es: \"{caracter}\"")
                            print(f"\t\tEl numero de veces a eliminar es: \"{conver_numero}\".")
                            split = cadena.split(caracter,conver_numero)
                            print(f"\t\t{split}\n") 
                    elif opcion == "4":
                       print("""Definicion:
El metodo "partition" es utilizado para dividir la candena en tres secciones tomando como centro la palabra que se le
pase como entrada, la sintaxis de este metodo es: "cadena.partition(caracter)", este metodo devolvera una lista.
Caracteristicas:
        1. Este metodo hara la division a partir del primer caracter identico que encuentre en la cadena, evaluando 
           de izquierda a derecha.
        2. El caracter que introduzcas aparecera en el centro de la lista.
        3. Si introduces el primer caracter de la cadena como primer elemento de la lista aparecera un espacio en blanco.
                Ejemplo:\n""")      
                       cadena = "Este texto es de prueba."
                       caracter = "e"
                       print(f"\t\tLa cadena que dividiremos es: \"{cadena}\"")
                       print(f"\t\tEl caracter que buscaremos es: \"{caracter}\"\n")
                       lista = cadena.partition(caracter)
                       print(f"\tOuput: {lista}\n")
                       print("\t\tEs momento que lo intentes.")
                       while True:
                          print("\t\tIngresa \"q\" p \"\" para salir.")
                          cadena = input("\t\tIntroduce la cadena: ")
                          if cadena == "q" or cadena == "":
                             break
                          caracter = input("\t\tIntoduce el caracter: ")
                          print(f"\t\tLa cadena que dividiremos es: \"{cadena}\"")
                          print(f"\t\tEl caracter que buscaremos es: \"{caracter}\"\n")
                          split = cadena.partition(caracter)
                          print(f"\tOuput: {split}\n")
                    elif opcion == "5":
                       print("""Definicion:
El metodo "rjust()" puede tomar 2 parametros de entrada, el primero un numero que representara las veces que se repetira
un caracter y como segundo parametro el caracter en si que se añadira a la cadena el numero de veces señaladas, esto del 
lado izquierdo de la cadena, este metodo devolvera una cadena, la sintaxis es: "cadena.rjust(numero,caracter)".
Caracteristicas:
        1. Si le pasa solo el parametro numero tomara por defecto el caracter espacio en blanco para añadirlo a la cadena.
        2. El numero determinara el tamaño total de la cadena (caracteres de la cadena + caracteres añadidos).
        3. Si el numero es menor que el tamaño de la cadena se devolvera la cadena misma.
                Ejemplo:\n""")
                       cadena = "Hola"
                       conta_cadena = len(cadena)
                       caracter = "-"
                       numero = 7
                       print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                       print(f"\t\tLa longitud de la cadena es: \"{len(cadena)}\"")
                       print(f"\t\tEl numero que pasaremos es: \"{numero}\" y el numero de veces que se añadira el caracter es: \"{numero-conta_cadena}\"")
                       print(f"\t\tEl caracter que añadiremos es: \"{caracter}\"\n")
                       cadena1 = cadena.rjust(numero,caracter)
                       print(f"\tOuput: {cadena1}\n")
                       print("\t\tEs momento que lo intentes.")
                       while True:
                          print("\t\tIngresa \"q\" p \"\" para salir.")
                          cadena = input("\t\tIntroduce la cadena: ")
                          conta_cadena = len(cadena)
                          if cadena == "q" or cadena == "":
                            break
                          numero = input("\t\tIntoduce el numero: ")
                          conver_numero = int(numero)
                          caracter = input("\t\tIntoduce el caracter: ")
                          print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                          print(f"\t\tEl numero de veces que se repetira el caracter es \"numero-len(cadena)\" => \"{numero}\"-\"{conta_cadena}\"=> \"{conver_numero - conta_cadena}\"")
                          print(f"\t\tEl caracter que añadiremos es: \"{caracter}\"\n")
                          cadena1 = cadena.rjust(conver_numero,caracter)
                          print(f"\tOuput: {cadena1}\n")
                    elif opcion == "6":
                       print("""Definicion:
El metodo "ljust()" puede tomar 2 parametros de entrada, el primero un numero que representara las veces que se repetira
un caracter y como segundo parametro el caracter en si que se añadira a la cadena el numero de veces señaladas, esto del 
lado derecho de la cadena, este metodo devolvera una cadena, la sintaxis es: "cadena.ljust(numero,caracter)".
Caracteristicas:
        1. Si le pasa solo el parametro numero tomara por defecto el caracter espacio en blanco para añadirlo a la cadena.
        2. El numero determinara el tamaño total de la cadena (caracteres de la cadena + caracteres añadidos).
        3. Si el numero es menor que el tamaño de la cadena se devolvera la cadena misma.
                Ejemplo:\n""")
                       cadena = "Salmon"
                       conta_cadena = len(cadena)
                       caracter = "*"
                       numero = 7
                       print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                       print(f"\t\tEl numero de veces que se repetira el caracter es \"numero-len(cadena)\" => \"{numero}\"-\"{conta_cadena}\"=> \"{numero - conta_cadena}\"")
                       print(f"\t\tEl caracter que añadiremos es: \"{caracter}\"\n")
                       cadena1 = cadena.ljust(numero,caracter)
                       print(f"\tOuput: {cadena1}\n")
                       print("\t\tEs momento que lo intentes.")
                       while True:
                          print("\t\tIngresa \"q\" p \"\" para salir.")
                          cadena = input("\t\tIntroduce la cadena: ")
                          conta_cadena = len(cadena)
                          if cadena == "q" or cadena == "":
                             break
                          numero = input("\t\tIntoduce el numero: ")
                          conver_numero = int(numero)
                          caracter = input("\t\tIntoduce el caracter: ")
                          print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                          print(f"\t\tEl numero de veces que se repetira el caracter es \"numero-len(cadena)\" => \"{numero}\"-\"{conta_cadena}\"=> \"{conver_numero - conta_cadena}\"")
                          print(f"\t\tEl caracter que añadiremos es: \"{caracter}\"\n")
                          cadena1 = cadena.ljust(conver_numero,caracter)
                          print(f"\tOuput: {cadena1}\n")
                    elif opcion == "7":
                       print("""Definicion:
El metodo "center()" puede tomar 2 parametros de entrada, el primero un numero que representara las veces que se repetira
un caracter y como segundo parametro el caracter en si que se añadira a la cadena el numero de veces señaladas, esto pasara 
a ambos lados de la cadena, la sintaxis es: "cadena.center(numero,caracter)".
Caracteristicas:
        1. Si le pasa solo el parametro numero tomara por defecto el caracter espacio en blanco para añadirlo a la cadena.
        2. El numero determinara el tamaño total de la cadena (caracteres de la cadena + caracteres añadidos).
        3. Si el numero es menor que el tamaño de la cadena se devolvera la cadena misma.
        4. El numero de caracteres que se añadiran a cada extremo puede ser algunas veces igual o diferente, esto dependera
           de la longitud de la cadena y del valor que quede disponible despues de restar.
                Ejemplo:\n""")
                       cadena = "Montaña"
                       conta_cadena = len(cadena)
                       caracter = "#"
                       numero = 30
                       print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                       print(f"\t\tEl numero de veces que se repetira el caracter es \"numero-len(cadena)\" => \"{numero}\"-\"{conta_cadena}\"=> \"{numero - conta_cadena}\"")
                       print(f"\t\tEl caracter que añadiremos es: \"{caracter}\"\n")
                       cadena1 = cadena.center(numero,caracter)
                       print(f"\tOuput: {cadena1}\n")
                       print("\t\tEs momento que lo intentes.")
                       while True:
                          print("\t\tIngresa \"q\" p \"\" para salir.")
                          cadena = input("\t\tIntroduce la cadena: ")
                          conta_cadena = len(cadena)
                          if cadena == "q" or cadena == "":
                             break
                          numero = input("\t\tIntoduce el numero: ")
                          conver_numero = int(numero)
                          caracter = input("\t\tIntoduce el caracter: ")
                          print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                          print(f"\t\tEl numero de veces que se repetira el caracter es \"numero-len(cadena)\" => \"{numero}\"-\"{conta_cadena}\"=> \"{conver_numero - conta_cadena}\"")
                          print(f"\t\tEl caracter que añadiremos es: \"{caracter}\"\n")
                          cadena1 = cadena.center(conver_numero,caracter)
                          print(f"\tOuput: {cadena1}\n")
                    elif opcion == "8":
                      print("""Definicion:
El metodo "strip" elimina espacios en blanco que existen a ambos extremos de la cadena, la sintaxis es: "cadena.strip()".
                Ejemplo:\n""")
                      cadena = " Esperanza    "
                      print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                      print(f"\t\tEl tamaño de esta cadena es: \"{len(cadena)}\"\n")
                      cadena1 = cadena.strip()
                      print(f"\tOuput: {cadena1}\n")
                      print(f"\t\tEl nuevo tamaño es: {len(cadena1)}")
                      print("\t\tEs momento que lo intentes.")
                      while True:
                         print("\t\tIngresa \"q\" p \"\" para salir.")
                         cadena = input("\t\tIntroduce la cadena: ")
                         if cadena == "q" or cadena == "":
                            break
                         print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                         print(f"\t\tEl tamaño de esta cadena es: \"{len(cadena)}\"\n")
                         cadena1 = cadena.strip()
                         print(f"\tOuput: {cadena1}\n")
                         print(f"\t\tEl nuevo tamaño es: {len(cadena1)}")
                    elif opcion == "9":
                       print("""Definicion:
El metodo "rstrip" elimina espacios en blanco que existen al extremo derecho de la cadena, la sintaxis es: "cadena.rtrip()".
                Ejemplo:\n""")
                       cadena = "  Bondad    "
                       print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                       print(f"\t\tEl tamaño de esta cadena es: \"{len(cadena)}\"\n")
                       cadena1 = cadena.rstrip()
                       print(f"\tOuput: {cadena1}\n")
                       print(f"\t\tEl nuevo tamaño es: {len(cadena1)}")
                       print("\t\tEs momento que lo intentes.")
                       while True:
                          print("\t\tIngresa \"q\" p \"\" para salir.")
                          cadena = input("\t\tIntroduce la cadena: ")
                          if cadena == "q" or cadena == "":
                             break
                          print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                          print(f"\t\tEl tamaño de esta cadena es: \"{len(cadena)}\"\n")
                          cadena1 = cadena.rstrip()
                          print(f"\tOuput: {cadena1}\n")
                          print(f"\t\tEl nuevo tamaño es: {len(cadena1)}")
                    elif opcion == "10":
                       print("""Definicion:
El metodo "lstrip" elimina espacios en blanco que existen al extremo izquierdo de la cadena, la sintaxis es: "cadena.ltrip()".
                Ejemplo:\n""")
                       cadena = "  Gloria    "
                       print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                       print(f"\t\tEl tamaño de esta cadena es: \"{len(cadena)}\"\n")
                       cadena1 = cadena.lstrip()
                       print(f"\tOuput: {cadena1}\n")
                       print(f"\t\tEl nuevo tamaño es: {len(cadena1)}")
                       print("\t\tEs momento que lo intentes.")
                       while True:
                          print("\t\tIngresa \"q\" p \"\" para salir.")
                          cadena = input("\t\tIntroduce la cadena: ")
                          if cadena == "q" or cadena == "":
                             break
                          print(f"\t\tLa cadena que modificaremos es: \"{cadena}\"")
                          print(f"\t\tEl tamaño de esta cadena es: \"{len(cadena)}\"\n")
                          cadena1 = cadena.lstrip()
                          print(f"\tOuput: {cadena1}\n")
                          print(f"\t\tEl nuevo tamaño es: {len(cadena1)}")
    elif numero == "6":
            print("""Definicion:
Las funciones "ord()" y "chr()" se utilizan para obtener informacion ASCII manipulando caracteres y numeros.""")
            while True:
                print("""\t\tSelecciona el subtema:
                  Ingresa "q" o "" para salir.
                  1. ord().
                  2. chr().\n""")
                opcion = input("\t\tIntroduce un numero: ")
                if opcion == "q" or opcion == "":
                    break
                elif opcion == "1":
                    print("""Definicion:
El metodo "ord()" permite obtener el numero ordinal que esta asociado a ese caracter en el codigo ASCII, la sintaxis es:
"ord(caracter)".
                Ejemplo:\n""")
                    while True:
                        print("\t\tIngresa \"q\" o \"\" para salir.")
                        cadena = input("\t\tIntroduce el caracter: ")
                        if cadena == "q" or cadena == "":
                            break
                        cadena1 = ord(cadena)
                        print(f"\n\tOuput: {cadena1}")
                        print(f"\tEl caracter \"{cadena}\" en codigo ASCII representa el entero: \" {cadena1} \"\n")
                elif opcion == "2":
                    print("""Definicion:
El metodo "chr()" permite obtener el caracter asociado con el numero en el codigo ASCII, la sintaxis es:
"chr(numero)".
                Ejemplo:\n""")
                while True:
                    print("\t\tIngresa \"q\" o \"\" para salir.")
                    cadena = input("\t\tIntroduce el numero: ")
                    if cadena == "q" or cadena == "":
                        break
                    conver_cadena = int(cadena)
                    ordinal = chr(conver_cadena)
                    print(f"\n\tOuput: {ordinal}")
                    print(f"\tEl numero \"{cadena}\" en codigo ASCII representa el caracter: \" {ordinal} \"\n")






   










            
                
                






            
                
                



                
                



                
                
            
            
                
                



                
                



                
                
                


                

        
        
        

         