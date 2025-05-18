from mod.estado import Estado

class EstadoContagem(Estado):
    """
    Representa um estado no problema da contagem, no qual o seu valor é o próprio ID.
    Este valor representa o valor atual da contagem, no qual são aplicados os incrementos.
    """
    def __init__(self, valor):
        self.valor = valor
        super().__init__()
        
    def id_valor(self):
        return self.valor