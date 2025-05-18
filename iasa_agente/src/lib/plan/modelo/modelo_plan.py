from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    @abstractmethod
    def obter_estado(self):
        """_summary_

        Args:
            modelo_plan (_type_): _description_
            objectivos (_type_): _description_
        """
        
    @abstractmethod
    def obter_estados(self):
        """_summary_
        
        Returns:
            _type_: _description_
        """
        
    @abstractmethod
    def obter_operadores(self):
        """_summary_
        
        Returns:
            _type_: _description_
        """