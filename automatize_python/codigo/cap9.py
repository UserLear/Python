from pathlib import Path
#LECTURA Y ESCRITURA DE ARCHIVOS
#.......uso Path
Path('spam', 'bacon', 'eggs')
#shell: WindowsPath('spam/bacon/eggs')
str(Path('spam', 'bacon', 'eggs'))
#shell: 'spam\\bacon\\eggs'

#.......uso de for
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
        print(Path(r'C:\Users\Al', filename))
#C:\Users\Al\accounts.txt
#C:\Users\Al\details.csv
#C:\Users\Al\invite.docx



