#Actividad U2 AP1.5
print('Pulse 1 si aprobo la primera evaluacion, sino 2')
priEVa = int(input())
print('Pulse 1 si aprobo la segunda evaluacion, sino 2')
segEVa = int(input())
print('Pulse 1 si aprobo la tercera evaluacion, sino 2')
triEVa = int(input())

if priEVa == 2 and segEVa == 1 and triEVa == 1:
	print("Aprobado")
else :
	print("Suspendido")

