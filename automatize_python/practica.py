<<<<<<< HEAD
import re
regex1 = re.compile(r'\S+') #cualquier caracter que no sea espacio, tabulacion o nueva linea
resul = regex1.findall(':"|`!@#$%^*() _-+=><#$\{\}1234:3]caracter________\n ') 
print(resul) #[':"|`!@#$%^*()', '_-+=><#$\\{\\}1234:3]caracter________']
=======
while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break

print(f'Your age is {age}.')

"""When you run this program, the output could look like this:

Enter your age:
five
Please use numeric digits.
Enter your age:
-2
Please enter a positive number.
Enter your age:
30
Your age is 30."""






>>>>>>> refs/remotes/origin/main

