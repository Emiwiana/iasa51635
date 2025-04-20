from ecr.comportamento import Comportamento
from sae import Avancar

class ExplorarComMemoria(Comportamento):
    """
    Define o comportamento de exploração, tendo em conta situações em que o agente já se encontrou, isto é, 
    verifica se o agente já percorreu um certo caminho de modo a não o repetir.
    Ao contrário do comportamento explorar, o agente não pode repete movimento já tomado, então perde menos tempo
    a explorar.
    """
    def __init__(self, dimimensao_maxima = 100):
        self.__dimensao_maxima = dimimensao_maxima #define a dimensão máxima da memória, isto pois, se nao houver, eventualmente o agente pode ficar preso por considerar todos os locais possíveis à sua volta como já atravessados.
        self.__memoria = []
        
    def activar(self, percepcao):
        """
        Gera uma ação em base no comportamento ExplorarComMemoria, 

        Args:
            percepcao (_type_): _description_

        Returns:
            _type_: _description_
        """
        posicao = percepcao.posicao
        direccao = percepcao.direccao
        
        situacao = (posicao, direccao)
        accao = None
        if situacao not in self.__memoria: #verifica se a situação já existe na memória, se não, explora
            self.__memoria.append(situacao) #acrescenta a situação nova à memória, de modo a esta não ser repetida
            if len(self.__memoria) > self.__dimensao_maxima: #se a memória estiver cheia, remove o elemento mais antigo
                self.__memoria.pop(0)
            accao = Avancar()
        return accao
        
    
        
    
    