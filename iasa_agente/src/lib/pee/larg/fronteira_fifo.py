from ..mec_proc.fronteira import Fronteira

class FronteiraFIFO(Fronteira):
    """_
    Define uma fronteira com um mecanismo de procura Last in first out, de modo a implementar a procura por profundidade.
    """
    def __init__(self):
        super().__init__()
        
    def inserir(self, no):
        """
        Insere o nó no fim da lista de modo a implementar o mecanismo First in First Out
        No qual o último nó que foi inserido é o primeiro a ser processado.
        Args:
            no (No): Nó a ser inserido
        """
        self._nos.append(no)