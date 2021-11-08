#Actividad U2 AP1.5

print('Pulse 1 para calcular la area del Triangulo. Pulse 2 para calcular la area del Circulo')

forma = int(input())

if forma ==1:
	baseT = input('Dime la base')
	alturaT = input('Dime la altura')
	baseB = float(baseT) / 2
	AreaT = float(baseB) * float(alturaT)
	print("El area de tu triangulo es", AreaT)				
if forma ==2:
	Pi = 3.141592
	radio = input('Dime el radio')
	radioC = float(radio) * float(radio)
	AreaC = float(radioC) * float(Pi)
	print("El area de tu triangulo es", AreaC)
	
	
