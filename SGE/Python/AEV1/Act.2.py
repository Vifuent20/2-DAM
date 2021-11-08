print('PROGRAMA VERIFICACIÓN CONTRASEÑA')
print(' ')
contraseña = input('Dime tu contraseña ')
intentos =5

while intentos != 0:
	nuevaContraseña = input('Repite tu contraseña ')
	if contraseña == nuevaContraseña:
		intentos = 0
		print('Las contraseñas coinciden ')

	else:
		intentos = intentos -1
		print('Error quedan ', intentos, ' intentos')
