import re
regex1 = re.compile(r'(\D){1,}')
resul = regex1.search('caracteres: " # a A : 3')
print(resul.group())

