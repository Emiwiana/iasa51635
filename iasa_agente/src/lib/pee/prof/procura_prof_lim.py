from .procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    """
    Representa um mecanismo de procura em profundidade onde a expansão da fronteira está limitada a um dado
    nível de profundidade.
    """
    def __init__(self, prof_max = 10):
        self._prof_max = prof_max
        super().__init__()
    
    def _expandir(self, problema, no):
        #limita o método expandir a apenas retornar os sucessores se a profundidade do nó for igual ou inferior
        #à profundidade máxima
        #se não, retorna uma lista de sucessores vazia
        return super()._expandir(problema, no) if no.profundidade <= self._prof_max else []