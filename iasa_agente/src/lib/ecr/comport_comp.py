from abc import ABC, abstractmethod
from .comportamento import Comportamento

class ComportComp(Comportamento):
    """
    Implementação do mecanismo base de um comportamento composto
    <p>
    Representa um comportamento composto por vários comportamentos
    Requer um mecanismo de selecção de acção para determinar a acção a realizar 
    em função das respostas dos vários comportamentos internos.
    """
    def __init__(self, comportamentos):
        """
        Método construtor da classe ComportComp
        Args:
            comportamentos (List): lista de comportamentos que compõem este comportamento composto
        """
        super().__init__()
        self.__comportamentos = comportamentos
        
        
    def activar(self, percepcao):
        """
        Activa todos os comportamentos que compõem o comportamento composto
        <p>
        Activa todos os comportamentos da lista de comportamentos do comportamento composto,
        apenas ativa os comportamentos com uma acção associada.
        Args:
            percepcao (Percepcao): _description_
        Returns:
            List: lista com as acções dos comportamentos
        """
        super().activar(percepcao)
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao: #verifica se a accao não tem um valor nulo antes de a juntar à lista
                accoes.append(accao)
        if accoes: #verifica se há accoes para serem retornadas
            return self.seleccionar_accao(accoes)
        
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """
        Seleciona uma acção para ativar tendo em conta a sua hierarquia ou atravéz de prioridade dinâmica
        Args:
            accoes (List): Lista composta por ações
        Returns:
            Accao: acção selecionada
        """
    