#BOOLEANS
#sale de la programacion binaria de 0 o 1
is_single = True
print(type(is_single)) #<class 'bool'>

#cambiar el valor de la variable
is_single = False
print(type(is_single)) #<class 'bool'>

#invertir los valores booleans de las variables utilizando el operador not
print(not True) #False
print(not False) #True
is_single = not is_single
print(is_single) #True

#proyecto 7 + 8 + 9 + 10: calculo de una tasa impositiva
def impuesto_sr(salario):
    if salario >= 0.01 and salario <= 19919.96:
        return "Exento"
    elif salario >= 19919.17 and salario <= 28624.99:
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 199039.48
        impuesto = monto_gravable * 0.15
        monto = round(impuesto, 2)
        return monto
    elif salario >= 28625.00 and salario <= 62151.15:
        monto_impuesto_15 = 303499.9 - 199039.48 
        impuesto_15 = monto_impuesto_15 * 0.15
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 303499.91
        impuesto = monto_gravable * 0.20
        monto = round(impuesto + impuesto_15, 2)
        return monto
    else: 
        monto_impuesto_15 = 303499.9 - 199039.48 
        impuesto_15 = monto_impuesto_15 * 0.15
        monto_impuesto_20 = 705813.76 - 303499.91
        impuesto_20 = monto_impuesto_20 * 0.20
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 705813.77
        impuesto = monto_gravable * 0.25
        monto = round(impuesto + impuesto_15 + impuesto_20, 2)
        return monto

while True:
    try:
        salario = input("Introduce tu salario para el calculo: \n")
        if salario == "":
            break
        conver_salario = int(salario)
        impuesto = impuesto_sr(conver_salario)
        print(f"Lo que debes pagar de impuesto impositivo correspondiente a su salario de {conver_salario} es de {impuesto}" )
    except:
        print("Lo siento la formula solo trabaja sobre numeros enteros positivos")


