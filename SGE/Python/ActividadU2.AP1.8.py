#Actividad U2 AP1.8

print('Dime la edad de tu gato')
edad  = int(input())
edadIn = edad
edadRes = 0
joven1 = 0
joven2 = 0

if edadIn >= 1:
	joven1 = edadRes + 15
	edad = edad - 1
if edadIn >= 2:
	joven2 = edadRes + 10
	edad = edad - 1
	
edadRes = (edad * 4)+ joven1 + joven2 


print("La edad de tu gato es", edadRes)
	

