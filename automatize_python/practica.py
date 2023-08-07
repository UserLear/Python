from pathlib import Path, os
#.......comprobacion de validez de ruta
p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo\\cap7.py')
p.exists() #shell: True

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo\\cap7.py')
p.is_file() #shell: True

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo\\cap7.py')
p.is_dir() #shell: False

p = Path('C:\\Users\\DELL_USER_#1\\Desktop\\plazti\\Python\\automatize_python\\codigo')
p.is_dir() #shell: True





