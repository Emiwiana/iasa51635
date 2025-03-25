from abc import ABC

class Comportamento(ABC):
    """
    Interface que define a funcionalidade geral de um comportamento
    """
    def activar(self, percepcao):
        """
        Método abstrato comportamento, constitui um contrato a ser implementado por classes
        que implementam esta interface
        Args:
            percepcao (Percepcao): _description_
        Returns: Accao
        """