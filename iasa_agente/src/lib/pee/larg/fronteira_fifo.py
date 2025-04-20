from ..mec_proc.fronteira import Fronteira

class FronteiraFIFO(Fronteira):
    """_
    Define uma fronteira com um mecanismo de procura Last in first out, de modo a implementar a procura por profundidade.
    Esta fronteira destaca-se por inserir os nós no fim da lista
    """
    def __init__(self):
        super().__init__()
        
    def inserir(self, no):
        self._nos.insert(0, no)