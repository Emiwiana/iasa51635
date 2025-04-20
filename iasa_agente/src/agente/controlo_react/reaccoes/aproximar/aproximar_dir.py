from ecr.reaccao import Reaccao
from .estimulo_alvo import EstimuloAlvo
from ..resposta.resposta_mover import RespostaMover

class AproximarDir(Reaccao):
    """
    Representa uma reação, composta pelo estímulo EstimuloAlvo (cuja intensidade é medida em base da proximidade do
    agente a um alvo) e a resposta à deteção de um alvo.
    
    Este estímulo e resposta são associados de modo a definir o comportamento do agente quando deteta um alvo
    """
    def __init__(self, direccao):
        super().__init__(
            EstimuloAlvo(direccao), 
            RespostaMover(direccao)
        )