from pathlib import Path
import openpyxl
#para usar este modulo ya debe existir el documento de exel, y le pasamos la ruta de su ubicacion a la funcion
p = Path.home()/'desktop'
wb = openpyxl.load_workbook(p/'ejemplo.xlsx')
h1 = wb['Hoja1']
h2= h1['B3'] 

#11......obtener filas y columnas de las hojas
#este funciona en forma de zig zag accediendo a cada celda de izquierda a derecha y de arriba para abajo
print(tuple(h1['A1':'C3'])) #((<Cell 'Hoja1'.A1>, <Cell 'Hoja1'.B1>, <Cell 'Hoja1'.C1>), (<Cell 'Hoja1'.A2>, <Cell 'Hoja1'.B2>, <Cell 'Hoja1'.C2>), (<Cell 'Hoja1'.A3>, <Cell 'Hoja1'.B3>, <Cell 'Hoja1'.C3>))
for columna in h1['A1':'C3']:
    for celda in columna:
        print(celda.coordinate, celda.value)
    print('fin de fila')
'''
A1 None
B1 None
C1 B
fin de fila
A2 None
B2 A
C2 None
fin de fila
A3 1
B3 2015-04-05 13:34:02
C3 manzanas
fin de fila
'''


#12......obtener las coordenadas en una fila (row) o columna (column) en particular, a cada metodo se le agrega una 's' al final (rows, columns)
#para hacer esto estos atributos row o column deben convertirse en lista antes de poder usar los corchetes y un indice con el
hoja = wb.active
cl = list(hoja.columns)[1] #obtiene las celdas de la segunda columna
print(cl) #(<Cell 'Hoja1'.B1>, <Cell 'Hoja1'.B2>, <Cell 'Hoja1'.B3>, <Cell 'Hoja1'.B4>, <Cell 'Hoja1'.B5>, <Cell 'Hoja1'.B6>, <Cell 'Hoja1'.B7>, <Cell 'Hoja1'.B8>, <Cell 'Hoja1'.B9>, <Cell 'Hoja1'.B10>, <Cell 'Hoja1'.B11>)

cl = list(hoja.columns)[0] #obtiene las celdas de la primera columna
print(cl) #(<Cell 'Hoja1'.A1>, <Cell 'Hoja1'.A2>, <Cell 'Hoja1'.A3>, <Cell 'Hoja1'.A4>, <Cell 'Hoja1'.A5>, <Cell 'Hoja1'.A6>, <Cell 'Hoja1'.A7>, <Cell 'Hoja1'.A8>, <Cell 'Hoja1'.A9>, <Cell 'Hoja1'.A10>, <Cell 'Hoja1'.A11>)

cl = list(hoja.rows)[0] #se considera hasta la ultima celda que tiene contenido incluyendo las intermedias aunque no tengan contenido
print(cl) #(<Cell 'Hoja1'.A1>, <Cell 'Hoja1'.B1>, <Cell 'Hoja1'.C1>, <Cell 'Hoja1'.D1>, <Cell 'Hoja1'.E1>, <Cell 'Hoja1'.F1>)

cl = list(hoja.rows)[0] #si consideramos una hoja vacia devuelve un error
print(cl)

#13......obtener los valores en una fila (row) o columna (column) en particular, a cada metodo se le agrega una 's' al final (rows, columns) 
for h in list(hoja.columns)[1]:
    print(h.value)
'''
None
A
2015-04-05 13:34:02
2015-04-05 03:41:23
6/04/2015 12:46:51 p.m.
2015-04-08 08:59:43
2015-04-10 02:07:00
2015-04-10 18:10:37
2015-04-10 02:40:46
None
la mayoria de las personas
'''



























