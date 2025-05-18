from abc import ABC
from abc import abstractmethod

class Heurisitica(ABC):
    """
    Representação da heuristica a ser usada pelas procuras do tipo procura informada, nas quais são criadas
    uma estimativa do custo de modo a chegar à soluçâo do problema, usando a função heuristica.
    """
    @abstractmethod
    def h(self, estado):
        """
        Método abstrato que pretende obrigar a implementação da função heuristica responsável
        por criar uma estimativa do custo para chegar desde o nó atual, ao nó final do problema.
        """
