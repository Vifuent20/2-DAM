print('PROGRAMA ADIVINAR NUMERO CON RANDOM()')
print(' ')
import random

min = int(input('Dime el primer numero del rango '))
max = int(input('Dimer el ultimo numero del rango '))
x = random.random()
al = min + x*100000%(max-min+1)
al = round(al,0)

print('Adivina el numero aleatorio entre', min, 'y', max)
num = 0

while num != al:
    num = int(input('Dime el numero que crees que es '))
    if num == al:
        print('Acertaste')
    else:
        print('Has Fallado')

    if num < al:
        print('El numero es demasiado pequeño')
    if num > al:
        print('El numero es demasiado grande')