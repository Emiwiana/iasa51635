from ..mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    """_
    Define uma fronteira com um mecanismo de procura Last in first out, de modo a implementar a procura por profundidade.
    """
    def __init__(self):
        super().__init__()
        
    def inserir(self, no):
        """
        Insere um nó no fim da lista da fronteira, de modo a implementar o mecanismo Last in First Out
        Em que o primeiro nó a ser inserido é o primeiro a ser processado.
        Args:
            no (No): Nó a ser inserido
        """
        self._nos.insert(0, no)