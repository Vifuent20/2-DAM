print('PROGRAMA INTERCAMBIA VALORES')
print(' ')

x = int(input('Dime el primer numero '))
y = int(input('Dime el segundo numero '))
print(' ')
print('Calculo Intercambio de valores')
print('x =', x, '+', y)
print('y =', x, '-', y)
print('x =', x, '-', y)
x = x+y
y = x-y
x = x-y

print('El primer numero es ', x)
print('El segundo numero es ', y)