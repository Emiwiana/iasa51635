from .mecanismo_procura import MecanismoProcura
from abc import abstractmethod
from abc import ABC

class ProcuraGrafo(MecanismoProcura, ABC):
    
    @property
    def estados_repetidos(self):
        return self.__estados_repetidos
    
    def _iniciar_memoria(self):
        """
        Inicia a memória de procura, iniciando a fronteira e criando um dicionário que contém os nós explorados.
        A memória de nós explorados é criada por um dicionário que associa o estado do nó ao próprio nó.
        """
        super()._iniciar_memoria()
        self._explorados = {}
        self.__estados_repetidos = 0 #inicia a contagem de estados repetidos nesta procura
    
    def _memorizar(self, no):
        """
        Memoriza um nó, se este for para manter, acrescentando-o ao dicionário de nós explorados e inserindo-o na fronteira
        Args:
            no (No): nó a ser memorizado
        """
        if(self._manter(no)):
            self._explorados[no.estado] = no
            super()._memorizar(no)
        else:                                           #se um estado estiver na lista de estados explorados, foi repetido
            self.__estados_repetidos += 1               #incrementa a contagem
    
    @abstractmethod
    def _manter(no):
        raise NotImplementedError