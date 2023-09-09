print("Ingrese coordenadas del caballo.")
fila_caballo = int(input("Fila: "))

if fila_caballo < 1 or fila_caballo > 8:
    print("Posición inválida.")
else:
    columna_caballo = int(input("Columna (1-8): "))

    if columna_caballo < 1 or columna_caballo > 8:
        print("Posición inválida.")
    else:
        print("El caballo puede saltar a las siguientes posiciones:")

        movimientos_filas = [2, 2, 1, 1, -1, -1, -2, -2]
        movimientos_columnas = [1, -1, 2, -2, 2, -2, 1, -1]

        for i in range(8):
            nueva_fila = fila_caballo + movimientos_filas[i]
            nueva_columna = columna_caballo + movimientos_columnas[i]

            if 1 <= nueva_fila <= 8 and 1 <= nueva_columna <= 8:
                print(f"({nueva_fila}, {nueva_columna})")
