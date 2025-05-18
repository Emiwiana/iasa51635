from abc import ABC, abstractmethod

class Planeador(ABC):
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """_summary_

        Args:
            modelo_plan (_type_): _description_
            objectivos (_type_): _description_
        Returns:
            _type_: _description_
        """