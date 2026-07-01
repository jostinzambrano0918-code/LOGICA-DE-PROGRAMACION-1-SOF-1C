import random

opciones = ["piedra", "papel", "tijera"]

while True:
    victorias_seguidas = 0
    intentos = 0

    print("Bienvenido al juego de Piedra, Papel o Tijera")
    print("Debes ganar 3 veces seguidas.")
    print("Solo tienes 3 intentos.\n")

    while intentos < 3 and victorias_seguidas < 3:
        jugador = input("Elige piedra, papel o tijera: ").lower()

        if jugador not in opciones:
            print("Opción inválida. Intenta otra vez.\n")
            continue

        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")

        intentos += 1

        if jugador == computadora:
            print("Empate. Se rompe la racha.\n")
            victorias_seguidas = 0

        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            victorias_seguidas += 1
            print("Ganaste esta ronda.")
            print(f"Victorias seguidas: {victorias_seguidas}/3\n")

        else:
            print("Perdiste esta ronda. Se rompe la racha.\n")
            victorias_seguidas = 0

    if victorias_seguidas == 3:
        print("¡Felicidades! Ganaste el juego.")
    else:
        print("Perdiste el juego. No ganaste 3 veces seguidas en 3 intentos.")

    jugar_otra_vez = input("¿Quieres jugar otra vez? (si/no): ").lower()

    if jugar_otra_vez != "si":
        print("Gracias por jugar. ¡Hasta luego!")
        break
    else:
        print("\nNueva partida...\n")