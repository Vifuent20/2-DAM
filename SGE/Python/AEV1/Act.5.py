print('PROGRAMA ADIVINAR NUMERO CON RANDINT()')
print(' ')
import random

min = int(input('Dime el primer numero del rango '))
max = int(input('Dimer el ultimo numero del rango '))
x = random.randint(min,max)

print('Adivina el numero aleatorio entre ', min, 'y ', max)
num = 0

while num != x:
    num = int(input('Dime el numero que crees que es '))
    if num == x:
        print('Acertaste')
    else:
        print('Has Fallado')

    if num < x:
        print('El numero es demasiado pequeño')
    if num > x:
        print('El numero es demasiado grande')

