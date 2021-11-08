#Actividad U2 AP1.3

añoActual = input('Dime el año actual')
año = input('Dame el año que quieras')

if añoActual > año:
	faltan = float(añoActual) - float(año)
	print("Han pasado", faltan , "años desde el" , año)

if añoActual < año:
	sobran = float(año) - float(añoActual)
	print("Faltan", sobran , "años para el" , año)
