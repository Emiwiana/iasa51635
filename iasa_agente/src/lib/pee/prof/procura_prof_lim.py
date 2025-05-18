from .procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    """
    Representa um mecanismo de procura em profundidade onde a expansão da fronteira está limitada a um dado
    nível de profundidade.
    """
    def __init__(self, prof_max = 5):
        self._prof_max = prof_max
        super().__init__()
    
    def _expandir(self, problema, no):
        #limita o método expandir a apenas retornar os sucessores se a profundidade do nó sucessor for igual ou inferior
        #à profundidade máxima
        #a profundidade do nó sucessor será então igual ou inferior à profundidade máxima se a profundidade do nó de origem for
        #inferior à profundidade máxima, se esta for verificada como menor ou igual, o nó sucessor pode a ter uma profundidade
        #igual a prof_max + 1
        #se não, retorna uma lista de sucessores vazia
        return super()._expandir(problema, no) if no.profundidade < self._prof_max else []