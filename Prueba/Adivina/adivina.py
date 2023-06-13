import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0
    nombre_jugador = input("¡Hola! ¿Cómo te llamas? ")

    print(f"Hola, {nombre_jugador}. Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("¿Cuál crees que es el número? "))
        intentos_realizados += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta nuevamente.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta nuevamente.")
        else:
            print(f"¡Felicitaciones, {nombre_jugador}! ¡Adivinaste el número en {intentos_realizados} intentos!")
            break

    print("¡Gracias por jugar!")

adivina_el_numero()