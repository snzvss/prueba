# Declaración de variables
jugador1 = ""
jugador2 = ""
juego_actual = [0, 0]  # [puntos_jugador1, puntos_jugador2]
juegos_partido = [0, 0]  # [juegos_jugador1, juegos_jugador2]
puntajes = ["0", "15", "30", "40","VENTAJA"]
ganador_partido = None

# Funciones auxiliares
def imprimir_puntuacion():
    print("Puntuación del partido:")
    print(f"{jugador1}: {juegos_partido[0]} juegos")
    print(f"{jugador2}: {juegos_partido[1]} juegos")
    print("Puntuación del juego actual:")
    print(f"{jugador1}: {puntajes[juego_actual[0]]}")
    print(f"{jugador2}: {puntajes[juego_actual[1]]}")
    print()


def dar_punto(jugador):
    global juego_actual, juegos_partido, ganador_partido

    if ganador_partido is not None:
        print(f"El partido ya ha terminado. El ganador es {ganador_partido}.")
        return

    if jugador == 1:
        juego_actual[0] += 1
    elif jugador == 2:
        juego_actual[1] += 1
    else:
        print("Jugador no válido.")
        return

    # Verificar si el marcador actual es "VENTAJA - 40" y el jugador 2 anota
    if puntajes[juego_actual[0]] == "VENTAJA" and juego_actual[1] == 4:
        juego_actual[0] = 3
        juego_actual[1] = 3
        print("Deuce.")
        return

    # Comprobar si se ha ganado el juego
    if juego_actual[0] == 4 and juego_actual[1] < 3:
        juegos_partido[0] += 1
        print(f"{jugador1} gana el juego.")
        juego_actual = [0, 0]
    elif juego_actual[1] == 4 and juego_actual[0] < 3:
        juegos_partido[1] += 1
        print(f"{jugador2} gana el juego.")
        juego_actual = [0, 0]
    elif juego_actual[0] == 3 and juego_actual[1] == 3:
        print("Deuce.")
    elif juego_actual[0] == 4 and juego_actual[1] == 3:
        print(f"Ventaja para {jugador1}.")
    elif juego_actual[1] == 4 and juego_actual[0] == 3:
        print(f"Ventaja para {jugador2}.")
    elif juego_actual[0] == 5:
        juegos_partido[0] += 1
        print(f"{jugador1} gana el juego.")
        juego_actual = [0, 0]
    elif juego_actual[1] == 5:
        juegos_partido[1] += 1
        print(f"{jugador2} gana el juego.")
        juego_actual = [0, 0]

    # Comprobar si se ha ganado el partido
    if juegos_partido[0] >= 1:
        ganador_partido = jugador1
        print(f"{jugador1} gana el partido.")
    elif juegos_partido[1] >= 1:
        ganador_partido = jugador2
        print(f"{jugador2} gana el partido.")
        if juegos_partido[0] >= 1:
            ganador_partido = jugador1
            print(f"{jugador1} gana el partido.")
        elif juegos_partido[1] >= 1:
            ganador_partido = jugador2
            print(f"{jugador2} gana el partido.")
            
        if juegos_partido[0] == 2:
            ganador_partido = jugador1
            print(f"{jugador1} gana el partido.")
        elif juegos_partido[1] == 2:
            ganador_partido = jugador2
            print(f"{jugador2} gana el partido.")
        elif juegos_partido[0] == 1 and juegos_partido[1] == 1:
            print("Juego decisivo")
        elif juegos_partido[0] == 1 and juegos_partido[1] == 0 and juego_actual[0] >= 40:
            ganador_partido = jugador1
            print(f"{jugador1} gana el partido.")
        elif juegos_partido[0] == 0 and juegos_partido[1] == 1 and juego_actual[1] >= 40:
            ganador_partido = jugador2
            print(f"{jugador2} gana el partido.")


# Etapa de configuración
while jugador1 == "":
    jugador1 = input("Introduce el nombre del jugador 1: ")
while jugador2 == "":
    jugador2 = input("Introduce el nombre del jugador 2: ")

print(f"Jugador 1: {jugador1}")
print(f"Jugador 2: {jugador2}")
print("Empieza el partido.")

# Bucle principal
while ganador_partido is None:
    imprimir_puntuacion()

    jugador_ganador = None
    while jugador_ganador is None:
        jugador = int(input(f"¿Quién gana el punto, 1: {jugador1}, 2: {jugador2}? "))
        if jugador not in [1, 2]:
            print("Jugador no válido.")
        else:
            dar_punto(jugador)
            jugador_ganador = jugador

print("Fin del partido.")