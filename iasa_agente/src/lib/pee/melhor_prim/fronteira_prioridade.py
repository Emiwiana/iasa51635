from ..mec_proc.fronteira import Fronteira 
import heapq

class FronteiraPrioridade(Fronteira):
    """
    Classe que representa um fronteira cujo mecanismo de inserção e remoção funciona em torno de uma prioridade
    associada aos nós por um avaliador.
    Nesta fronteira, os nós são inseridos com um valor de prioridade
    e os primeiros nós removidos são os com o menor valor de prioridade.
    """
    def __init__(self, avaliador):
        """
        Construtor da Fronteira prioridade, inicia a fronteira e associa um avaliador à mesma.
        """
        super().__init__()
        self.__avaliador = avaliador
    
    def inserir(self, no):
        """
        Insere um nó na fronteira, tendo em conta a prioridade em função ao avaliador.
        Args:
            no (No): nó a ser inserido
        """
        no.prioridade = self.__avaliador.prioridade(no) #calcula a prioridade do nó em função ao avaliador
        heapq.heappush(self._nos, no)                   #insere o nó na lista, tendo em conta a prioridade
    
    def remover(self):
        """
        Remove o nó com menos prioridade da fronteira
        Returns:
            No: nó removido
        """
        return heapq.heappop(self._nos)