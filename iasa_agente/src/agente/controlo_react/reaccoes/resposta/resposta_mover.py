from ecr.resposta import Resposta
from sae import Rodar

class RespostaMover(Resposta):
    """
    Resposta gerada pelo pelo comportamento Aproximar Alvo. Esta resposta, dada uma direção em que se encontra um alvo,
    gera uma acção de Rodar nessa direção, de modo a o agente se deslocar para o alvo.
    Args:
        Resposta (_type_): _description_
    """
    def _init_(self, direccao):
        accao = Rodar(direccao)
        super()._init_(accao)