#Empaquetar y desempaquetar argumentos en Python
# A Python program to demonstrate need
# of packing and unpacking
# A sample function that takes 4 arguments
# and prints them.
def fun(a, b, c, d):
    print(a, b, c, d)
# Driver Code
my_list = [1, 2, 3, 4]
# This doesn't work
fun(my_list)
#salida: TypeError: fun() toma exactamente 4 argumentos (1 dado)


# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)
# Driver Code
my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)
#salida: (1, 2, 3, 4)

