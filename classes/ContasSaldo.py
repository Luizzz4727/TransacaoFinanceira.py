class ContasSaldo:
    def __init__(self, conta, saldo_inicial):
        self._conta = conta
        self._saldo = saldo_inicial

    def get_conta(self):
        return self._conta

    def get_saldo(self):
        return self._saldo

    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            raise ValueError("Saldo insuficiente.")
