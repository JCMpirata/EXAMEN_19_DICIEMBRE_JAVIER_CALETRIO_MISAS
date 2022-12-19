def knight(fila, columna):
    if fila == 0 and columna == 0:
        return 0
    elif fila == 0 or columna == 0:
        return 1
    else:
        return knight(fila-1, columna) + knight(fila, columna-1)

def tablero(fila, columna):
    tablero = []
    for i in range(fila):
        tablero.append([])
        for j in range(columna):
            tablero[i].append(knight(i, j))
    return tablero

if __name__ == '__main__':
    fila = int(input("Ingrese un número: "))
    columna = int(input("Ingrese un número: "))
    print(knight(fila, columna))