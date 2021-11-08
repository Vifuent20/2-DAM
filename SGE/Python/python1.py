import sys

def calcularSalario(horasDia, tarifaHoras, diasLaborables, horasExtra) :
	if horasDia > 8 :
		salario = (diasLaborables*(8 * float(tarifaHoras)) + horasExtra)
	else :
		salario = (diasLaborables * (float(horasDia) * float(tarifaHoras)))
	return salario

horasDia = input('Cuantas horas trabajas al dia?')
tarifaHoras = input('Cuanto cobras cada hora?')
diasLaborables = input('Dime los dias laborables del mes')

try :
	horasDia = float(horasDia)
	tarifaHoras = float(tarifaHoras)
	diasLaborables = int(diasLaborables)
	horasExtra = float((horasDia - 8) * (tarifaHoras * 1.5) * diasLaborables)

except :
	print ("ERROR EN LA INTRODUCCION DE LOS DATOS")
	sys.exit()

print(calcularSalario(horasDia, tarifaHoras, diasLaborables, horasExtra))

