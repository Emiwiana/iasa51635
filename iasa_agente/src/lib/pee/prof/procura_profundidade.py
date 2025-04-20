from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    """
    Aplica um algoritmo de procurar uma solução para um problema em procura, esta procura não é ótima ou completa, isto é
    não encontra todas as soluções possíveis e não encontra a solução mais eficiente, mas apenas ocupa memória equivalente
    à profundidade do problema, sendo mais eficiente em termos de recursos do sistema.
    """
    def __init__(self):
        super().__init__(FronteiraLIFO())