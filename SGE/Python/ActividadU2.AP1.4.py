#Actividad U2 AP1.4

x = input('Dame un numero')
y = input('Dame otro numero')





if x > y:
	Div = float(x) % float (y)
	if Div == 0:
		print("Es Multiplo")
	else :
		print("No es Multiplo")
	
if x < y:
	Div2 = float(y) % float(x)
	if Div2 == 0:
		print("Es Multiplo")
	else :
		print("No es Multiplo")
