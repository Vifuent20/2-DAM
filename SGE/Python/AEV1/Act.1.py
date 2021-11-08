print('PROGRAMA QUE SACA LOS PARES ENTRE UN RANGO DE NUMEROS')
print(' ')
num1 = int(input('Dame el primer numero del rango '))
num2 = int(input('Dame el ultimo numero del rango '))
print(' ')
print('Los pares que hay entre ellos son: ')
if num1 > num2:
	while num1 > num2:
		if num2 % 2 == 0:
			print(num2)
		num2 = num2 + 1


if num1 < num2:
	while num1 < num2:
		if num1 % 2 == 0:
			print(num1)
		num1 = num1 + 1

