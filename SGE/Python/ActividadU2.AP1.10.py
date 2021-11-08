#Actividad U2 AP1.10

precioVivienda = input("Dime precio ViVienda:")
zona = input("Dime la zona:")
edad = input("Dime tu edad:")
sueldoAnual = input("Dime tu sueldo anual:")

precioVivienda = int(precioVivienda)
edad = int(edad)
sueldoAnual = float(sueldoAnual)
zona = str(zona)

if zona == "A":
	sueldoAnual = sueldoAnual * 0.85
if zona == "B":
	sueldoAnual = sueldoAnual * 0.9
if zona == "C":
	sueldoAnual = sueldoAnual * 0.92
if zona == "D":
	sueldoAnual = sueldoAnual * 0.97
if zona == "E":
	sueldoAnual = sueldoAnual * 1

SMI = 13300

proporcion = sueldoAnual / SMI

if proporcion < 1.5:
	ayuda = 0.15 * precioVivienda
elif proporcion < 2.5:
	ayuda = 0.1 * precioVivienda
elif proporcion < 3.5:
	ayuda = 0.08 * precioVivienda
elif proporcion < 4.5:
	ayuda = 0.05 * precioVivienda
else:
	ayuda = 0

if edad < 35:
	ayuda = ayuda + 3000

print(ayuda)
