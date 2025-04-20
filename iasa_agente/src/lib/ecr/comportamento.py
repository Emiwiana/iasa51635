from abc import ABC, abstractmethod

class Comportamento(ABC):
    """
    Interface que define a funcionalidade geral de um comportamento, representa o comportamento geral do agente.
    """
    @abstractmethod
    def activar(self, percepcao):
        """
        Método abstrato comportamento, constitui um contrato a ser implementado por classes
        que implementam esta interface
        Args:
            percepcao (Percepcao): percepção que ativa o comportamento
        Returns: 
            Accao: Acção resultante a activação do comportamento
        """