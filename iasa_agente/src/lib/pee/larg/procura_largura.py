from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_fifo import FronteiraFIFO

class ProcuraLargura(MecanismoProcura):
    """
    Aplica um algoritmo de procurar uma solução para um problema em largura, esta procura é ótima e completa, isto é
    encontra a solução ideal entre todas as possíveis, mas ocupa imensa memória, não sendo viável para problemas 
    complexos
    """
    def __init__(self):
        super().__init__(FronteiraFIFO())