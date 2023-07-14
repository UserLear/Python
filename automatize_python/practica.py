while True:
    conver = input('Introduce un str o int (blanco para salir): ')
    if conver == '':
            break
    try:
        numero = int(conver)
        def convertir1(valor):
            convert = chr(valor)
            print(f'El numero {numero} representa el literal, caracter o numero {convert}')
        convertir1(numero)
    except:
        def convertir2(valor):
            convert = (ord(valor))
            print(f'La letra o simbolo {valor} se prepresenta como el numero {convert}' )
        convertir2(conver)












