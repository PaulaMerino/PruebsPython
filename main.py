
def print_hi():
    print(f'Hello world!!')
def print_tablero(tablero):
    print("  A   B   C")
    print("a "+tablero[0][0]+" | "+tablero[0][1]+" | "+tablero[0][2])
    print("  ─  ─  ─ ")
    print("b "+tablero[1][0] + " | " + tablero[1][1] + " | " + tablero[1][2])
    print("  ─  ─  ─ ")
    print("c "+tablero[2][0] + " | " + tablero[2][1] + " | " + tablero[2][2])

def obtenerCoor(mov):
    if mov[0] == "a":
        x = 0
    else:
        if mov[0]=="b":
            x = 1
        else:
            x = 2
    if mov[1] == "A":
        y = 0
    else:
        if mov[1]=="B":
            y = 1
        else:
            y = 2
    return x,y

def compruebaCasilla(tablero, mov, jugador):
    x = obtenerCoor(mov)[0]
    y = obtenerCoor(mov)[1]

    print("Las coordenados son "+str(x)+" "+str(y))

    if tablero[x][y]==" ":
        tablero[x][y]=jugador
        return 0
    else:
        print("Movimiento incorrecto, intentelo de nuevo")
        return -1

def compruebaHorizontal(tablero):
    for i in range(3):
        if tablero [i][0] == tablero [i][1] and tablero [i][1] == tablero [i][2] and tablero[i][0]!=" ":
            return 1, tablero[i][0]

    return [0]
def compruebaVertical(tablero):
    for i in range(3):
        #print("valores que comprueba "+tablero [0][i]+", "+tablero [1][i]+", "+tablero [2][i])
        if tablero [0][i] == tablero [1][i] and tablero [1][i] == tablero [2][i] and tablero[0][i]!=" ":
            return 1, tablero[0][i]
    return [0]
def compruebaDiagonal(tablero):
        if tablero [0][0] == tablero [1][1] and tablero [2][2] == tablero [1][1] and tablero[0][0]!=" ":
            return 1, tablero[0][0]

        if tablero [0][2] == tablero [1][1] and tablero [0][2] == tablero [2][0] and tablero[0][2]!=" ":
            return 1, tablero[0][2]

        return [0]

def compruebaJugada(tablero):
    fin = compruebaHorizontal(tablero)
    if fin[0] == 1:
        return fin[1]
    fin = compruebaDiagonal(tablero)
    if fin[0] == 1:
        return fin[1]
    fin = compruebaVertical(tablero)
    if fin[0] == 1:
        return fin[1]

    return 0

def reset(tablero):
    for i in range(3):
        for j in range(3):
            tablero[i][j]=" "

if __name__ == '__main__':
    print_hi()
    tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
    print_tablero(tablero)
    movimientos = 0
    ganador = 1
    while ganador != "X" and ganador!="O":

        if movimientos % 2 == 0:
            jugador = "X"
        else:
            jugador = "O"

        print("Intoduzca movimiento JUGADOR "+jugador+" (Ej. aC)")

        correcto = -1
        while correcto == -1:
            mov = input()
            correcto = compruebaCasilla(tablero, mov, jugador)

        print_tablero(tablero)

        ganador = compruebaJugada(tablero)

        movimientos=movimientos+1
        if movimientos == 8:
            reset(tablero)

    print("GANADOR DE LA PARTIDA: "+str(ganador))



