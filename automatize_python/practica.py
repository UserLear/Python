import re
#.......sustitucion de cadenas con el metodo sub()
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#'CENSORED gave the secret documents to CENSORED.'



