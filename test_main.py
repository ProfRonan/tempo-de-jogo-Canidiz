"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_01(self):
        """Função que testa Exemplo 01."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['08:30:00', '12:45:30']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 2
            mock_print.assert_called_with('04:15:30')

    def test_02(self):
        """Função que testa Exemplo 02."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['18:43:50', '21:17:45']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 2
            mock_print.assert_called_with('02:33:55')

    def test_03(self):
        """Função que testa Exemplo 03."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['22:17:16', '21:16:15']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 2
            mock_print.assert_called_with('22:58:59')

    def test_04(self):
        """Função que testa exemplo 04."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['00:00:00', '23:59:59']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 2
            mock_print.assert_called_with('23:59:59')

    def test_05(self):
        """Função que testa Exemplo 05."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['00:00:00', '00:00:00']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 2
            mock_print.assert_called_with('24:00:00')


if __name__ == '__main__':
    unittest.main()
