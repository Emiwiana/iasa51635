from abc import ABC, abstractmethod

class Plano(ABC):
    @abstractmethod
    def obter_accao(self, estado):
        """_summary_

        Args:
            estado (_type_): _description_

        Returns:
            Operador: _description_
        """
        
    @abstractmethod
    def mostrar(self, vista):
        """_summary_

        Args:
            vista (_type_): _description_
        """