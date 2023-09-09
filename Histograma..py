numP = 0
numN = 0

while True:
    valor = int(input("Ingrese un valor entero (0 para terminar): "))

    if valor == 0:
        break
    elif valor > 0:
        numP += 1
    else:
        numN += 1

print("Gráfico de valores positivos:")
for i in range(numP):
    print("*", end="")

print("\nGráfico de valores negativos:")
for i in range(numN):
    print("*", end="")
