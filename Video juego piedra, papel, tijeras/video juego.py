import random

lista = ["piedra", "papel", "tijera"]
print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
while True:
    jugador = input("Elige piedra, papel o tijera: ").lower()
    computadora = random.choice(lista)
    
    print(f"Computadora eligió: {computadora}")
    
    if jugador == computadora:
        print("Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:        print("¡Perdiste!")
    jugar_otra_vez = input("¿Quieres jugar otra vez? (si/no): ").lower()
    if jugar_otra_vez != "si":
    
        break

print("Gracias por jugar. ¡Hasta luego!")