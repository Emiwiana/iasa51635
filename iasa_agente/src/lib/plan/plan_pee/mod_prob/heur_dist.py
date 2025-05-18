from pee.melhor_prim.heuristica import Heurisitica
import math

class HeurDist(Heurisitica):
    """
    Implementa a função heuristica, tendo em conta a distância entre um estado dado
    e o estado final, a ser usada no simulador.
    """
    def __init__(self, estado_final):
        self.__estado_final = estado_final
        
    def h(self, estado):
        return math.dist(estado.posicao, self.__estado_final.posicao)