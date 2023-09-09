import random

numero_secreto = random.randint(0, 100)
intentos = 0
adivinado = False

print("¡Bienvenido al juego de adivinanza de números!")

while not adivinado:
    try:
        intento = int(input("Adivina el número entre 0 y 100: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número secreto es menor. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
            adivinado = True
    except ValueError:
        print("Ingresa un número válido.")

