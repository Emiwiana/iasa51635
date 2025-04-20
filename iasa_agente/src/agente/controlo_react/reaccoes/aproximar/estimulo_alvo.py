from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

class EstimuloAlvo(Estimulo):
    """
    Representa o estimulo dado quando o agente deteta um alvo.
    
    Isto de modo a definir a associar uma intensidade à deteção do alvo em base na sua distância de modo
    a definir a prioridade do agente reagir à deteção
    """
    def __init__(self, direccao, gama = 0.9):
        self.__gama = gama
        self.__direccao = direccao
        
    def detectar(self, percepcao):
        """
        Método que, dado a percepção de um alvo, retorna uma intensidade em base na sua distância ao alvo
        
        A intensidade é 0 se não for detetado nenhum alvo, ou um valor entre 0 e 1, igual à gama ^ distância se for detetado
        Args:
            percepcao (Percepcao): Percepção do agente

        Returns:
            float: intensidade obtida pela percepção
        """
        elemento, distancia, _ = percepcao[self.__direccao]
        intensidade = self.__gama**distancia if elemento == Elemento.ALVO else 0
        return intensidade
            
            