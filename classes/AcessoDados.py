from classes.ContasSaldo import ContasSaldo

class AcessoDados:
    def __init__(self):
        self._tabela_saldos = [
            ContasSaldo(938485762, 180),
            ContasSaldo(347586970, 1200),
            ContasSaldo(2147483649, 0),
            ContasSaldo(675869708, 4900),
            ContasSaldo(238596054, 478),
            ContasSaldo(573659065, 787),
            ContasSaldo(210385733, 10),
            ContasSaldo(674038564, 400),
            ContasSaldo(563856300, 1200)
        ]

    def get_registro_conta(self, id):
        for conta in self._tabela_saldos:
            if conta.get_conta() == id:
                return conta
        return None
