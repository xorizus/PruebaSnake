import unittest
from unittest.mock import patch
import adivina  # Asegúrate de tener el archivo adivina_el_numero.py en el mismo directorio

class TestAdivinaElNumero(unittest.TestCase):
    @patch('builtins.input', side_effect=['Test', 50, 25, 75, 60])
    def test_adivina_el_numero(self, mock_input):
        with patch('builtins.print') as mock_print:
            adivina.adivina_el_numero()
            self.assertEqual(mock_print.call_args_list[0][0][0], "Hola, Test. Estoy pensando en un número entre 1 y 100.")
            self.assertEqual(mock_print.call_args_list[-1][0][0], "¡Felicitaciones, Test! ¡Adivinaste el número en 4 intentos!")

if __name__ == '__main__':
    unittest.main()