from .avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):
    """
    Implementação de um avaliador para a procura do tipo custo uniforme, 
    no qual o único parâmetro para definir a prioridade, é ter o menor custo possível.
    """
    def prioridade(self, no):
        return no.custo