print("Piensa en un número entre 1 y 100.")
input("Presiona Enter cuando estés listo para empezar")

menor = 1
mayor = 100
intentos = 0

while True:
    intento = (menor + mayor) // 2
    intentos += 1

    respuesta = input(f"¿Es {intento} tu número? Ingresa '<' si es menor, '>' si es mayor, o '=' si es correcto: ")

    if respuesta == "=":
        print(f"¡Adiviné tu número {intento} en {intentos} intentos!")
        break
    elif respuesta == "<":
        mayor = intento - 1
    elif respuesta == ">":
        menor = intento + 1
    else:
        print("Por favor, ingresa '<', '>', o '=' para responder.")
