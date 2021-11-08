print('PROGRAMA APILAR BOTES')
print(' ')
botes = int(input('Dime el numero de botes que quieres apilar '))
cont = 0

while botes >0:

    botes=botes-cont
    cont=cont+1

if botes != 0:
    print('No se puede apilar')
else:
    print('Se puede apilar')