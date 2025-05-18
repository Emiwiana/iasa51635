from mod.operador import Operador
from .estado_agente import EstadoAgente
from sae import Accao
import math

class OperadorMover(Operador):
    """
    Implementa o operador que representa uma acção, que compõe uma translação.
    """
    
    @property
    def ang(self):
        return self.__ang
    
    @property
    def accao(self):
        return self.__accao
    
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Accao(direccao)
    
    def aplicar(self, estado):
        nova_posicao = self.__translacao(estado.posicao, self.__accao.passo, self.__ang) #calcula a nova posição
        novo_estado = EstadoAgente(nova_posicao)    #cria um novo estado com um 
        if novo_estado in self.__modelo_mundo:      #se o novo estado pertence ao modelo do mundo
            return novo_estado                      #retorna o estado
    
    def custo(self, estado, estado_suc):
        """
        Calcula o custo de o operador transicionar de um estado para um estado sucessor,
        sendo este a distância entre os dois, e no mínimo, igual a 1.

        Args:
            estado (Estado): estado anterior
            estado_suc (Estado): estado sucessor

        Returns:
            int: custo de transição de estados
        """
        return max(1, math.dist(estado.posicao, estado_suc.posicao))
    
    def __translacao(self, posicao, dist, ang):
        """
        Calcula a nova posição, tendo em conta uma translação segundo uma dstância e ângulo dados

        Args:
            posicao (tuple): Posicao Inicial
            dist (int): distancia do movimento
            ang (int): angulo do movimento
        """
        
        x, y = posicao
        dx = round(dist * math.cos(ang))    #calcula a distancia em x
        dy = -round(dist * math.sin(ang))   #calcula a distancia em y
        
        nova_posicao = x + dx , y + dy
        return nova_posicao
        
        