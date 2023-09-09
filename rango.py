print("Ingrese la cantidad de datos a ingresar: ")
cantidad_datos = int(input())

if cantidad_datos <= 0:
    print("Debe ingresar al menos un dato.")
else:
    suma = 0
    minimo = float('inf')
    maximo = float('-inf')

    for i in range(1, cantidad_datos + 1):
        print(f"Ingrese el dato #{i}: ", end="")
        dato_str = input()
        try:
            dato = float(dato_str)
        except ValueError:
            print("Entrada no válida. Ingrese un número decimal.")
            break

        suma += dato

        if dato < minimo:
            minimo = dato

        if dato > maximo:
            maximo = dato

    else:  # Se ejecuta si el bucle for termina sin un break
        promedio = suma / cantidad_datos
        print(f"El rango de los datos ingresados es de {minimo} a {maximo}")
        print(f"El promedio de los datos ingresados es: {promedio}")
