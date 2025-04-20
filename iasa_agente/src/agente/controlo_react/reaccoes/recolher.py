from ecr.hierarquia import Hierarquia
from .aproximar.aproximar_alvo import AproximarAlvo
from .evitar.evitar_obst import EvitarObst
from .explorar.explorar import Explorar
from .explorar.explorar_com_memoria import ExplorarComMemoria

class Recolher(Hierarquia):
    """
    Inicia os vários comportamentos num comportamento composto com seleção por Hierarquia.
    
    Os vários comportamentos serão assim, executados em base na ordem do array.
    A ordem está definida de modo a primeiro o agente ao detectar um alvo, movimentar-se na sua direção, depois se encontrar um obstáculo
    deslocar-se de modo a não chocar contra ele, depois explorar com memória e por fim, explorar de forma aleatória.
    """
    def __init__(self):
        super().__init__([AproximarAlvo(), EvitarObst(), ExplorarComMemoria(), Explorar()])