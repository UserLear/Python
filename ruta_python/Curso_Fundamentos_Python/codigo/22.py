#programa: explica la manipulacion de listas
print("\nAcontinuacion te presentamos un programa que te explicara la manipulacion de listas.")
print("Acontinuacion selecciona el numero del tema que deseas aprender.\n")
while True:
    print('''Pulsa 'q' o '' para salir.
1. Explicacion del tipo de dato lista.
2. Indexacion de lista.
3. Concatenacion de elementos.
4. Indices negativos.
5. Slicing de listas.
6. Longitud de lista.          
7. Cambio de valores de lista.
8. Eliminacion de elementos de la lista.
9. Eliminacion de variable.
10. Añadir elementos a lista.
11. Bucle for en lista.
12. operadores in y not in.
13. asignacion multiple
14. funcion enumerate().
15. funciones random.choice() + random.shuffle().
16. Operadores de asignacion aumentada.
17. metodos.
18. tuplas.
19. referencia.
20. identidad y funcion id().
21. funcion copy(), deepcopy().      
          \n''')
    numero = input("Introduce el numero del tema:\n")
    if numero == "q" or numero == "":
        print("Fue un gusto contribuir a su arendizaje, hasta pronto.\n")
        break
