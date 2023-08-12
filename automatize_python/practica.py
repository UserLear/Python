from pathlib import Path, os, shelve
#.......GUARDAR VARIABLES CON MODULO SHELVE
#se ejecuta en el directorio actual
archivoEstante = shelve.open('miDato')
gatos = ['pelusa', 'dino', 'coco']
archivoEstante['misGatos'] = gatos
archivoEstante.close()
#esto crea 3 archivos con extenciones .bak, .dat, .dir









