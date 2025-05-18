from abc import ABC, abstractmethod
class Problema(ABC):
    
    def __init__(self, estado_inicial, operadores):
        assert len(operadores) >= 1 #garante que a lista operadores tem pelo menos 1 valor
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
    
    @abstractmethod
    def objetivo(self, estado):
        """
        Método que representa o objetivo do problema dado um estado
        Args:
            estado (Estado)
        Returns:
            boolean
        """
        #o método objetivo é abstrato uma vez que cada problema implementa um objetivo diferente, 
        #e tem de obrigatóriamente ter um objetivo
    
    @property
    def estado_inicial(self):
        #retorna o valor do atributo __estado_inicial, para o exterior
        #basta chamar p.estado_inicial de modo a obtê-lo
        #desta forma é realizado o parâmetro read-only da propriedade __estado_inicial
        return self.__estado_inicial
    
    @property
    def operadores(self):
        return self.__operadores