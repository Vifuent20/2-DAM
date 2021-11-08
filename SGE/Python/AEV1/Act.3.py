print('PROGRAMA IMPRIME TRIANGULO CON ASTERICOS')
print(' ')
n = int(input('Dime la anchura del triangulo '))

for i in range(1,n+1):
    for j in range(i):
        print('*', end='')
    print()


for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
