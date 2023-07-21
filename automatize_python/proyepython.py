#4.......retorna el tipo
"""En este desafío encontrarás una función llamada solution que recibe un parámetro llamado valor. Debes encontrar el tipo de dato del parámetro valor y retornarlo desde la función solution.
Recuerda que el parámetro valor será distinto por cada distinta forma en que ejecutemos la función solution."""
#usando return dentro de la funcion
def found_type(value):
   return type(value)

print(found_type(1)) #<class 'int'>
print(found_type("Dieguillo")) #<class 'str'> 
print(found_type(True)) #<class 'bool'>

#usando print dentro de la funcion
def found_type1(value):
   print(type(value))

found_type1(1) #<class 'int'>
found_type1("Dieguillo") #<class 'str'>
found_type1(True) #<class 'bool'>

#usando condicionales dentro de la funcion
def found_type2(value):
    if type(value) == int:
        print("number")
    elif type(value) == str:
        print("string")
    elif type(value) == bool:
        print("boolean")

found_type2(1) #number
found_type2("Dieguillo") #string  
found_type2(True) #boolean 

#solucion platzi
def found_type(value):
   return type(value)

print(found_type(1)) #<class 'int'>
print(found_type("Dieguillo")) #<class 'str'>
print(found_type(True)) #<class 'bool'>

#6.......calcula la propina
"""En este desafío tendrás que calcular la propina que deben dejar los clientes de un restaurante en función de su consumo.
La función calculate_tip recibirá dos parámetros, bill_amount que representa el costo total de lo que se haya consumido y tip_percentage que representa el porcentaje de propina a dejar. Ambos valores serán de tipo float y siempre serán positivos, incluyendo el 0. La función deberá devolver el valor de la propina como un número.
Recuerda que para redondear a dos decimales tendrás que hacer uso de round(numero, cantidad de decimales)"""
def calculate_tip(bill_amount):
    if bill_amount >= 0 and bill_amount <= 100.99:
        porcentaje = float(10/100)
        monto = float(bill_amount)
        propina = monto * porcentaje
        return round(propina, 2)
    elif bill_amount >= 101 and bill_amount <= 1500.99:
        porcentaje = float(20/100)
        monto = float(bill_amount)
        propina = monto * porcentaje
        return round(propina, 2)
    elif bill_amount >= 1501:
        porcentaje = float(25/100)
        monto = float(bill_amount)
        propina = monto * porcentaje
        return round(propina, 2)
    else:
        return "Lo siento los numeros deben ser mayores o iguales a cero"

print(calculate_tip(100)) #10.0
print(calculate_tip(1524.33)) #381.08
print(calculate_tip(-2)) #Lo siento los numeros deben ser mayores o iguales a cero

#solucion platzi
def calculate_tip(bill_amount, tipPercentage):
   return round( ((bill_amount * tipPercentage)/ 100),2 )

print(calculate_tip(100, 10)) #10
print(calculate_tip(1524.33, 25)) #381.08

#8.......averigua si un año es bisiesto
"""En este desafío de Python, debes crear la lógica de la función is_leap_year, que determina si un año es bisiesto o no. Un año es bisiesto si cumple con las siguientes condiciones:
Es divisible por 4, pero no por 100.
Si es divisible por 100 debe serlo por 400 también.
La función is_leap_year recibe un único parámetro: el año a evaluar. Debe devolver True si el año es bisiesto o False en caso contrario.
Toma en cuenta que la función debe ser capaz de manejar valores no enteros o negativos."""
def is_leap_year(year):
    if year < 0 or type(year) == float:
        return "false"
    elif (year%4 == 0 and year%100 != 0) or (year%100 == 0 and year%400 ==0):
        return "true"
    else:
        return "false"

print(is_leap_year(2000))
print(is_leap_year(-2024))
print(is_leap_year(1984.25))
print(is_leap_year(400))
print(is_leap_year(2012))
print(is_leap_year(2016))
print(is_leap_year(2020))
print(is_leap_year(1582))
print(is_leap_year(1584))
print(is_leap_year(2032))
print(is_leap_year(2035))

#solucion platzi
def is_leap_year(year):
    # tu código aquí 👈
    if year > 0:
        if(year % 4 == 0) and (year % 100 != 0):
            return True
        elif (year % 100 == 0) and (year % 400 == 0):
            return True
        else:
            return False
    else:
        return False


result = is_leap_year(-2004)
print(result)

#10.......dibuja un triangulo usando bucles
"""En este desafío, debes dibujar un triángulo equilatero usando bucles.
Recibirás dos parámetros: size y character, que definen el número de filas que tendrá y el carácter con el que se debe construir el triángulo, respectivamente. Además, el triángulo debe estar alineado al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.
Recuerda que para hacer el salto de línea debes usar "\n", no olvides removerla de la última parte, debes retornar todo esto en una variable."""
def print_triangle(size, character):
    for i in range(size):
        i += 1
        print(size*" " + character*i + size*" ")
        size -= 1
    
print_triangle(10, "*")

#solucion platzi
def print_triangle(size, character):
    triangle = ''
    for i in range(size):
        triangle += " " * (size - i - 1)
        triangle += character  + character * (2 * i)
        if i != size - 1:
            triangle += "\n"
    return triangle

