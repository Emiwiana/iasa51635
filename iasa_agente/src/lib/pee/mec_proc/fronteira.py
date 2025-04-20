from abc import ABC, abstractmethod

class Fronteira(ABC):
    """
    Método abstrato que representa uma estrutura de dados de nós que possui uma relação de ordem de modo a 
    determinar a estratégia de controlo da procura.
    A fronteira é composta por nós com o mesmo nível de profundidade, abertos para expansão.
    """
    
    def __init__(self):
        self.iniciar()
        
    def iniciar(self):
        self._nos = []
    
    @property
    def vazia(self):
        return len(self._nos) == 0
    
    @abstractmethod
    def inserir(self, no):
        """
        Insere um dado nó na fronteira.
        Abstrato de modo a implementar mecanismos de procura diferentes.
        Args:
            no (No): nó a ser inserido
        """
    
    def remover(self):
        """
        Remove o primeiro no da fronteira e retorna-o
        Returns:
            No: nó que se encontrava no inicio da lista
        """
        return self._nos.pop(0)