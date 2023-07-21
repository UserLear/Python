import re
regex1 = re.compile(r'\S+') #cualquier caracter que no sea espacio, tabulacion o nueva linea
resul = regex1.findall(':"|`!@#$%^*() _-+=><#$\{\}1234:3]caracter________\n ') 
print(resul) #[':"|`!@#$%^*()', '_-+=><#$\\{\\}1234:3]caracter________']

