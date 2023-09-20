#! Python3
# mclip.py - A multi-clipboard program.

TEXT = {'aceptar': """Sí estoy de acuerdo. Eso suena bien para mi.""",
        'ocupado': """Lo siento, ¿podemos hacer esto más adelante esta semana o la próxima""",
        'venta': """¿Considerarías hacer esto como una donación mensual?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Uso: python portaPapeles.py [palabra clave] -copiar texto de frase')
    sys.exit()

keyphrase = sys.argv[1]    #La primera línea de comando arg es la frase clave

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Texto de ' + keyphrase + ' copiado al portapapeles.')
else:
    print ('No hay texto para ' + keyphrase)