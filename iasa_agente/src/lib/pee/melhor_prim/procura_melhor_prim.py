from .fronteira_prioridade import FronteiraPrioridade
from ..mec_proc.procura_grafo import ProcuraGrafo
from abc import ABC

class ProcuraMelhorPrim(ProcuraGrafo, ABC):
    
    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador
        
    def _manter(self, no):
        """
        Método usado para decidir se um nó deve ou não ser mantido na fronteira.
        Retorna verdadeiro se um nó não possuir um estado que já foi encontrado antes, ou
        se já tiver sido encontrado antes, mas o seu custo é menor.

        Args:
            no (No): no a ser decidido manter ou não.

        Returns:
            bool: valor booleano da decisão
        """ 
        return no.estado not in self._explorados or \
               no.custo < self._explorados[no.estado].custo
        #retorna verdade se o estado correspondente ao nó não estiver nos explorados ou se estiver nos explorados
        #e o custo do novo nó é inferior ao já presente, de modo a substituí-lo
