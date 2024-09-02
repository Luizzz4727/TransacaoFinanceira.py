import unittest
from io import StringIO
import sys
from classes.ExecutarTransacaoFinanceira import ExecutarTransacaoFinanceira
from classes.AcessoDados import AcessoDados

class TransacaoFinanceiraTeste(unittest.TestCase):

    def test_transferir_valor_quando_saldo_suficiente(self):
        repository = AcessoDados()
        executor = ExecutarTransacaoFinanceira(repository)
        conta_origem = 938485762  # Conta com saldo de 180
        conta_destino = 2147483649  # Conta com saldo de 0
        valor_transferencia = 50

        executor.transferir(1, conta_origem, conta_destino, valor_transferencia)

        saldo_origem = repository.get_registro_conta(conta_origem).get_saldo()
        saldo_destino = repository.get_registro_conta(conta_destino).get_saldo()

        self.assertEqual(130, saldo_origem)
        self.assertEqual(50, saldo_destino)

    def test_cancelar_transferencia_quando_saldo_insuficiente(self):
        repository = AcessoDados()
        executor = ExecutarTransacaoFinanceira(repository)
        conta_origem = 210385733  # Conta com saldo de 10
        conta_destino = 238596054  # Conta com saldo de 478
        valor_transferencia = 20

        captured_output = StringIO()
        sys.stdout = captured_output

        executor.transferir(2, conta_origem, conta_destino, valor_transferencia)

        sys.stdout = sys.__stdout__

        expected_message = "Transacao numero 2 foi cancelada por falta de saldo"
        result_message = captured_output.getvalue().strip()

        self.assertEqual(expected_message, result_message)

        saldo_origem = repository.get_registro_conta(conta_origem).get_saldo()
        saldo_destino = repository.get_registro_conta(conta_destino).get_saldo()

        self.assertEqual(10, saldo_origem)  # Saldo não deve mudar
        self.assertEqual(478, saldo_destino)  # Saldo não deve mudar

    def test_verificar_se_conta_origem_existe(self):
        repository = AcessoDados()
        executor = ExecutarTransacaoFinanceira(repository)
        conta_origem = 0  # Conta inexistente
        conta_destino = 238596054  # Conta com saldo de 478
        valor_transferencia = 20

        captured_output = StringIO()
        sys.stdout = captured_output

        executor.transferir(3, conta_origem, conta_destino, valor_transferencia)

        sys.stdout = sys.__stdout__

        expected_message = "Transacao numero 3 foi cancelada: Conta de origem não existe"
        result_message = captured_output.getvalue().strip()

        self.assertEqual(expected_message, result_message)

        saldo_destino = repository.get_registro_conta(conta_destino).get_saldo()

        self.assertEqual(478, saldo_destino)  # Saldo não deve mudar

    def test_verificar_se_conta_destino_existe(self):
        repository = AcessoDados()
        executor = ExecutarTransacaoFinanceira(repository)
        conta_origem = 210385733  # Conta com saldo de 10
        conta_destino = 0  # Conta inexistente
        valor_transferencia = 20

        captured_output = StringIO()
        sys.stdout = captured_output

        executor.transferir(4, conta_origem, conta_destino, valor_transferencia)

        sys.stdout = sys.__stdout__

        expected_message = "Transacao numero 4 foi cancelada: Conta de destino não existe"
        result_message = captured_output.getvalue().strip()

        self.assertEqual(expected_message, result_message)

        saldo_origem = repository.get_registro_conta(conta_origem).get_saldo()

        self.assertEqual(10, saldo_origem)  # Saldo não deve mudar

if __name__ == '__main__':
    unittest.main()
