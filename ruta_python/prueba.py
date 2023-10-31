#EJEMPLO 7 + 8 + 9 + 10
#calculo de una tasa impositiva
def impuesto_sr(salario):
    if salario >= 0.01 and salario <= 19919.96:
        return "Exento"
    elif salario >= 19919.17 and salario <= 28624.99:
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 19919.17
        impuesto = monto_gravable * 0.15
        return impuesto
    elif salario >= 28625.00 and salario <= 62151.15:
        monto_impuesto_15 = 303499.9 - 199039.48 
        impuesto_15 = monto_impuesto_15 * 0.15
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 28625.00
        impuesto = monto_gravable * 0.20
        return impuesto + impuesto_15
    else: 
        monto_impuesto_15 = 303499.9 - 199039.48 
        impuesto_15 = monto_impuesto_15 * 0.15
        monto_impuesto_20 = 705813.76 - 303499.91
        impuesto_20 = monto_impuesto_20 * 0.20
        renta_anual = salario * 12
        renta_neta_gravable = renta_anual - 40000
        monto_gravable = renta_neta_gravable - 62151.16
        impuesto = monto_gravable * 0.25
        return impuesto + impuesto_15 + impuesto_20

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






















