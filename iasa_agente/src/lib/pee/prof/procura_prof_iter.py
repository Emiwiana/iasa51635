from .procura_prof_lim import ProcuraProfLim

class ProcuraProfIter(ProcuraProfLim):
    """
    Aplica um algoritmo de procura de solução de Profundidade iterativa, aplicando o algoritmo de profundidade limitada
    repetetivamente, aumentando o limite de profundidade, até ser encontrada uma solução.
    Assim, é possível encontrar a solução com menor profundidade
    """
    def __init__(self, prof_max=10):
        super().__init__(prof_max)
        
    def procurar(self, problema, inc_prof = 1, limite_prof = 100):
    
        for profundidade in range(0, limite_prof+1, inc_prof):
            self._prof_max = profundidade           #atualiza a profundidade, aprofundando-a
            solucao = super().procurar(problema)    
            if solucao: return solucao              #retorna a primeira solução encontrada