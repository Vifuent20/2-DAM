print('PROGRAMA PREGUNTAS MULTIPLICACIONES Y NOTA SOBRE 10')
print(' ')
import random
nPreguntas = int(input('Dime el numero de preguntas '))
nPreguntasInicio = nPreguntas
nAciertos = 0

while nPreguntas != 0:
    x = int(1 +(random.random()*100)%(10-1+1))
    y = int(1 +(random.random()*100)%(10-1+1))
    x = round(x)
    y = round(y)



    print('Cuanto es', x,'*', y,'?')
    res = int(input())
    if res == (x*y):
        print('Correcto')
        nAciertos = nAciertos + 1
        nPreguntas = nPreguntas - 1
    if res != (x*y):
        print('Incorrecto')
        nPreguntas = nPreguntas - 1
print('Has acertado', nAciertos, ' de', nPreguntasInicio)
resFin = (nAciertos * 10)/nPreguntasInicio
resFin = round(resFin, 2)
print('Tu nota sobre 10 es', resFin)

