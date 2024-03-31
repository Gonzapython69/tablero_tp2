def crear_tablero(filas, columnas):
    # Crear techo
    techo = '-' * (columnas * 2 + 1)

    # Crear piso
    piso = '-' * (columnas * 2 + 1)

    # Crear paredes y celdas vacías
    tablero = []
    for _ in range(filas):
        fila = ['|'] * (columnas * 2)
        fila.insert(0, '|')
        fila.append('|')
        tablero.append(fila)

 # Colocar personaje en la posición inicial
    tablero[0][1] = 'P'  # Aquí posicionamos al personaje en la esquina superior izquierda

    return techo, tablero, piso

def imprimir_tablero(tablero):
    for fila in tablero:
        print("".join(fila))
        

def mover_personaje(tablero, direccion, posicion):
    filas = len(tablero)
    columnas = len(tablero[0]) // 2

    fila, columna = posicion

    if direccion == 'w' and fila > 0:
        fila -= 1
    elif direccion == 's' and fila < filas - 2:
        fila += 1
    elif direccion == 'a' and columna > 0:
        columna -= 1
    elif direccion == 'd' and columna < columnas - 2:
        columna += 1
    else:
        raise ValueError("Estás intentando mover el personaje fuera del tablero.")

    return fila, columna


def juego_tablero():
    while True:
        try:
            filas = int(input("Ingrese el número de filas del tablero: "))
            if filas <= 0:
                raise ValueError("El número de filas debe ser positivo.")
            columnas = int(input("Ingrese el número de columnas del tablero: "))
            if columnas <= 0:
                raise ValueError("El número de columnas debe ser positivo.")
            break
        except ValueError as e:
            print(e)

    techo, tablero, piso = crear_tablero(filas, columnas)
    posicion_personaje = (0, 0)

    while True:
        print("\nTablero:")
        imprimir_tablero([techo] + tablero + [piso])
        print("Posición del personaje:", posicion_personaje)

        direccion = input("Ingrese la dirección para mover al personaje (w/s/a/d), o 'e' para salir: ").lower()

        if direccion == 'e':
            print("¡Juego terminado!")
            break

        if direccion not in ['w', 's', 'a', 'd']:
            print("Dirección inválida. Por favor, ingrese 'w', 's', 'a' o 'd'.")
            continue

        try:
            nueva_posicion = mover_personaje(tablero, direccion, posicion_personaje)
        except ValueError as e:
            print(e)
            continue

        if nueva_posicion != posicion_personaje:
            tablero[posicion_personaje[0]][posicion_personaje[1] * 2 + 1] = ' '
            tablero[nueva_posicion[0]][nueva_posicion[1] * 2 + 1] = 'P'
            posicion_personaje = nueva_posicion

def main():
    juego_tablero()

main()


