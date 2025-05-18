from sae import Direccao, Elemento
from .operador_mover import OperadorMover
from .estado_agente import EstadoAgente
from plan.modelo.modelo_plan import ModeloPlan
import math

class ModeloMundo(ModeloPlan):
    """
    Representa um modelo do mundo, contendo a sua informação de modo a ser usado pelo agente
    para este gerar o seu plano de acção
    """
    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
    
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao ]
        self.__alterado = False
        
    def __contains__(self, estado):
        #implementação do operador in
        #deixa mais tarde usar este operador para verificar se um estado pertence a este modelo do mundo
        return estado in self.__estados
    
    #estes métodos serão usados em vez de propriedades para mais tarde implementar uma interface
    def obter_estado(self):
        return self.__estado
    
    def obter_estados(self):
        return self.__estados
    
    def obter_operadores(self):
        return self.__operadores
    
    def obter_elemento(self, estado):
        #por omissão, o python assume que quando uma chave não está presente no dicionário, retorna None
        return self.__elementos.get(estado.posicao)
    
    def distancia(self, estado):
        """
        Retorna a distância entre o estado do agente e um estado dado
        Sendo que um estado dado por uma posição
        Args:
            estado (Estado): estado para o qual se quer obter a distância

        Returns:
            float: distância entre ambos os estados
        """
        return math.dist(estado.posicao, self.__estado.posicao)
    
    def actualizar(self, percepcao):
        """
        Actualiza o modelo do mundo tendo em conta uma nova percepção, caso tenha havido alguma alteração.
        Args:
            percepcao (Percepção): _description_
        """
        self.__estado = EstadoAgente(percepcao.posicao)
        #verifica se os elementos actuais são diferentes da percepção, se forem, houve alteração do modelo
        self.__alterado = self.elementos != percepcao.elementos
        if self.__alterado:
            #actualiza os elementos e os estados se houve alteração
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
    
    def mostrar(self, vista):
        """
        Mostra todos os alvos, obstáculos e a posição do agente.
        Args:
            vista (Vista): _description_
        """
        for (posicao, elemento) in self.__elementos.items(): #gera uma lista de tuplos, em que o primeiro é uma chave e os seguintes um valor
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)