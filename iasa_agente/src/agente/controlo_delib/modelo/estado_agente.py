from mod.estado import Estado

class EstadoAgente(Estado):
    """
    Representa o estado do agente, definido por uma posição
    A posição é dada por um tuplo, contendo as coordenadas em x e y.
    """
    @property
    def posicao(self):
        return self.__posicao
    
    def __init__(self, posicao):
        self.__posicao = posicao
        
    def id_valor(self):
        """
        Retorna o valor único referente a este estado, este valor único é calculado
        usando o hash do tuplo posição.
        Returns:
            int: valor único ao estado
        """
        return hash(self.__posicao)