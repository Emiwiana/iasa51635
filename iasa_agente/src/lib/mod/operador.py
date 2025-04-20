from abc import ABC, abstractmethod
class Operador(ABC):
    
    @abstractmethod
    def aplicar(estado):
        """
        método a ser implementado por classes que implementem operador,
        aplica o operador a um dado estado
        Args:
            estado (Estado): estado a ser aplicado

        Returns Estado: estado com 
        """
        raise NotImplementedError
    
    @abstractmethod
    def custo(estado, estado_suc):
        """
        método a ser implementado por classes que implementem operador, 
        representa o custo de um operador
        Args:
            estado (Estado): estado
            estado_suc (Estado): estado sucessor
            
        Returns: double
        """