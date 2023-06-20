from unittest.mock import patch
import adivina as adv

def test_adivina_el_numero():
    with patch('builtins.input', side_effect=['Test', 50, 25, 75, 60]):
        with patch('builtins.print') as mock_print:
            adv.adivina_el_numero()
            assert mock_print.call_args_list[0][0][0] == "Hola, Test. Estoy pensando en un número entre 1 y 100."
            assert mock_print.call_args_list[-1][0][0] == "¡Felicitaciones, Test! ¡Adivinaste el número en 4 intentos!"

if __name__ == '__main__':
    test_adivina_el_numero()