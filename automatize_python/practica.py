import re
#.......coincidencia de lineas nuevas con el caracter de punto
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group() 
#'Serve the public trust.'

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# 'Serve the public trust.\nProtect the innocent.\nUphold the law.'







