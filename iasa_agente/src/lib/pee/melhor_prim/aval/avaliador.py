from abc import ABC, abstractmethod

class Avaliador(ABC):
    """
    Classe abstrata que representa um avaliador genérico.
    Um avaliador é responsável por definir a prioridade a atribuir a cada nó da fronteira,
    de modo a implementar as várias procuras do tipo melhor primeiro.
    """
    
    @abstractmethod
    def prioridade(self, no):
        """
        Método a ser implementado de modo a calcular e atribuir a prioridade de cada nó.
        """