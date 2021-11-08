import random

print('PROGRAMA PIEDRA PAPEL TIJERA')
print(' ')

eCont = 0
mCont = 0

eleccion = 0
mELeccion = 0

while eCont < 2 and mCont < 2:
    print('Piedra, Papel, Tijera')
    eleccion = input()
    mELeccion = random.choice(["Piedra", "Papel", "Tijera"])
    print(' ')
    print('Jugador eligio',eleccion, 'y Maquina eligio', mELeccion)

    if eleccion == mELeccion:
        print('Hay empate')
        print('Marcador:', eCont,'-', mCont)

    if eleccion == 'Piedra' and mELeccion == 'Papel':
        print('Máquina gana')
        mCont = mCont + 1
        print('Marcador:', eCont, '-', mCont)

    if eleccion == 'Papel' and mELeccion == 'Tijera':
        print('Máquina gana')
        mCont = mCont + 1
        print('Marcador:', eCont, '-', mCont)

    if eleccion == 'Tijera' and mELeccion == 'Piedra':
        print('Máquina gana')
        mCont = mCont + 1
        print('Marcador:', eCont, '-', mCont)

    if eleccion == 'Piedra' and mELeccion == 'Tijera':
        print('Jugador gana')
        eCont = eCont + 1
        print('Marcador:', eCont, '-', mCont)

    if eleccion == 'Tijera' and mELeccion == 'Papel':
         print('Jugador gana')
         mCont = mCont + 1
         print('Marcador:', eCont, '-', mCont)
    if eleccion == 'Papel' and mELeccion == 'Piedr':
        print('JUgador gana')
        eCont = eCont + 1
        print('Marcador:', eCont, '-', mCont)
    else:
        print('Error en la Eleccion del Jugador, no es válida')
print(' ')
print('Se acabo el juego, el resultado final fue Jugador',  eCont, '-', mCont,'Máquina')