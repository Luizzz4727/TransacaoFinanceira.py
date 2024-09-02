class Transacao:
    def __init__(self, correlation_id, datetime, conta_origem, conta_destino, valor):
        self.correlation_id = correlation_id
        self.datetime = datetime
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.valor = valor
