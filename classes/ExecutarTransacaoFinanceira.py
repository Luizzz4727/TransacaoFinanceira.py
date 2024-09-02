class ExecutarTransacaoFinanceira:
    def __init__(self, repositorio):
        self._repositorio = repositorio

    def transferir(self, correlation_id, conta_origem, conta_destino, valor):
        conta_saldo_origem = self._repositorio.get_registro_conta(conta_origem)
        conta_saldo_destino = self._repositorio.get_registro_conta(conta_destino)

        if conta_saldo_origem is None:
            print(f"Transacao numero {correlation_id} foi cancelada: Conta de origem não existe")
            return

        if conta_saldo_destino is None:
            print(f"Transacao numero {correlation_id} foi cancelada: Conta de destino não existe")
            return

        if conta_saldo_origem.get_saldo() < valor:
            print(f"Transacao numero {correlation_id} foi cancelada por falta de saldo")
            return

        # Realiza a transferência
        conta_saldo_origem.debitar(valor)
        conta_saldo_destino.creditar(valor)

        print(f"Transacao numero {correlation_id} foi efetivada com sucesso! Novos saldos: Conta Origem: {conta_saldo_origem.get_saldo():.2f} | Conta Destino: {conta_saldo_destino.get_saldo():.2f}")
