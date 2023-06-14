import random

# Se define una lista con las posibles palabras que pueden ser adivinadas
palabras = ['manzana', 'amarillo', 'laptop', 'gato', 'programacion', 'futbol']

# Se elige al azar una de las palabras de la lista
palabra_secreta = random.choice(palabras)

letras_encontradas = []

# Se inicializa el número de intentos del jugador
intentos_restantes = 6

while intentos_restantes > 0:
    # Muestra el estado actual del tablero
    tablero = ''
    for letra in palabra_secreta:
        if letra in letras_encontradas:
            tablero += letra
        else:
            tablero += '_'
    print(tablero)

    # Solicita al jugador que ingrese una letra
    letra_jugador = input('Ingresa una letra: ')

    # Verifica si la letra ingresada por el jugador se encuentra en la palabra secreta
    if letra_jugador in palabra_secreta:
        letras_encontradas.append(letra_jugador)
        print('¡Adivinaste!')
    else:
        intentos_restantes -= 1
        print('No adivinaste. Intentos restantes: ' + str(intentos_restantes))

    # Verifica si el jugador ha adivinado todas las letras de la palabra secreta
    if all(letra in letras_encontradas for letra in palabra_secreta):
        print('¡Felicidades! Adivinaste la palabra secreta: ' + palabra_secreta)
        break

# Si el jugador se queda sin intentos, se muestra un mensaje de derrota
if intentos_restantes == 0:
    print('Lo siento, has perdido. La palabra secreta era: ' + palabra_secreta)