from abc import ABC
from .avaliador import Avaliador

class AvaliadorHeur(Avaliador, ABC):
    """
    Classe que representa um avaliador, implementando uma heurística que influencia o cálculo da prioridade
    de cada nó na fronteira.
    Esta prioridade terá de ser implementada de forma diferente dependendo do tipo de procura desejado.
    """
    
    def __init__(self):
        self._heurisitica = None
        
    @property
    def heuristica(self):
        return self._heuristica
    @heuristica.setter
    def heuristica(self, valor):
        self._heuristica = valor