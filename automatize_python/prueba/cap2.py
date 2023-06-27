import random
#.......practica while
while True:
    print("¿Quién eres?")
    nombre = input()
    if nombre != "Joe":
        print("Tu no eres la persona que esperaba, lo siento no puedes ingresar")
        continue
    print("Hola Joe, ingresa tu contraseña (es un pez que se infla)")
    while True:
        contraseña = input()
        if contraseña == "pezglobo":
            print("Acceso permitido: Joe")
            break
        print("Lo siento Joe, contraseña incorrecta vuelve a intentar")

    break
print("Ahora Joe puedes ingresar a nuestos datos")

#.......practica for
print("Estoy pensando en un numero entre 1 y 20")
maquina = random.randint(1, 20)

try:
    for i in range(7):
        oportunidades = 7 - i
        sobrantes = i + 1
        print("Adivina, tienes " + str(oportunidades) + ' oportinidades.')
        numero = input()
        if int(numero) < maquina:
            print("'Uf!, andas abajo")
        elif int(numero) > maquina:
            print('Uf!, andas muy arriba')
        else:
            print('Felicidades!, lo has logrado en '+ str(sobrantes) + ' intentos.')
            print("Te sobraron " + str(7 - sobrantes) + ' oportunidades')
            break
except:
    print('Error, debes ingresar un numero.')

#for itera alreves
def reves(a):
    for i in a[::-1]:
        print(i)
 
reves("Otorrinolaringologo") #ogologniralonirrotO

#for itera saltos
def reves(a):
    for i in a[::2]:
        print(i)

reves("Otorrinolaringologo") #Oornlrnooo

#