import re
regex1 = re.compile(r'\w+') #imprime caracteres en linea y que sean del mismo tipo
resul = regex1.search(':{}"#$ 1234 : 3 ] caracter') 
print(resul)

