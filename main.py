from classes.Transacao import Transacao
from classes.ContasSaldo import ContasSaldo
from classes.AcessoDados import AcessoDados
from classes.ExecutarTransacaoFinanceira import ExecutarTransacaoFinanceira

def main():
    transacoes = [
        Transacao(1, "09/09/2023 14:15:00", 938485762, 2147483649, 150),
        Transacao(2, "09/09/2023 14:15:05", 2147483649, 210385733, 149),
        Transacao(3, "09/09/2023 14:15:29", 347586970, 238596054, 1100),
        Transacao(4, "09/09/2023 14:17:00", 675869708, 210385733, 5300),
        Transacao(5, "09/09/2023 14:18:00", 238596054, 674038564, 1489),
        Transacao(6, "09/09/2023 14:18:20", 573659065, 563856300, 49),
        Transacao(7, "09/09/2023 14:19:00", 938485762, 2147483649, 44),
        Transacao(8, "09/09/2023 14:19:01", 573659065, 675869708, 150),
        Transacao(9, "09/09/2023 14:19:02", 123456789, 675869708, 47),
        Transacao(10, "09/09/2023 14:19:03", 573659065, 987654321, 27),
        Transacao(11, "09/09/2023 14:19:04", 675869708, 573659065, 20.09)
    ]

    repository = AcessoDados()
    executor = ExecutarTransacaoFinanceira(repository)

    for item in transacoes:
        executor.transferir(item.correlation_id, item.conta_origem, item.conta_destino, item.valor)

if __name__ == "__main__":
    main()
