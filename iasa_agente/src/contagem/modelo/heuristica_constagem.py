from pee.melhor_prim.heuristica import Heurisitica

class HeuristicaContagem(Heurisitica):
    """
    Implementação da heuristica usada no problema de contagem.
    """
    def __init__(self, valor_final):
        self.__valor_final = valor_final
    
    def h(self, estado):
        """
        Calcula uma estimativa do custo entre o um estado atual e o estado final do problema de contagem,
        através do módulo da subtração do valor do estado atual pelo valor do estado final.
        Args:
            estado (Estado): estado atual

        Returns:
            int: estimativa do custo para chegar ao estado final, a partir de um estado dado.
        """
        return abs(estado.id_valor() - self.__valor_final) 
        