import juegos as juego
import unittest

def test_generar_lista_juegos(): # Test de la función generar_lista_juegos
    juegos = juego.generar_lista_juegos()
    assert len(juegos) == 10
    assert juegos[2] == "The Legend of Zelda: Breath of the Wild"
    assert juegos[1] == "Red Dead Redemption 2"
    assert juegos[1] == "God of War"
    assert juegos[3] == "Minecraft"
    assert juegos[4] == "Grand Theft Auto V"
    assert juegos[5] == "The Witcher 3: Wild Hunt"
    assert juegos[6] == "Super Mario Odyssey"
    assert juegos[7] == "Overwatch"
    assert juegos[8] == "Fortnite"
    assert juegos[9] == "Call of Duty: Modern Warfare"
    
if __name__ == "__main__": 
    test_generar_lista_juegos()
    print("¡Todos los tests pasaron!")