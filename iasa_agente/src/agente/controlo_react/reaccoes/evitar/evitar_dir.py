from ecr.reaccao import Reaccao
from .estimulo_obst import EstimuloObst
from .resposta_evitar import RespostaEvitar

class EvitarDir(Reaccao):
    """
    Reação do agente obtida através do estímulo "EstimuloObst" que gera a resposta "RespostaEvitar"
    
    Esta reação é responsável pelo comportamento do agente ao encontrar um obstáculo.
    """
    def __init__(self, direccao):
        super().__init__(
            EstimuloObst(direccao), 
            RespostaEvitar(direccao)
        )