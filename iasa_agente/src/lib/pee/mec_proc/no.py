class No:
    """
    Representação de um nó neuronal, cada nó possui um estado e pode, ou não, possuir um operador e sucessor
    """
    #ao definir o construtor com argumentos opcionais, é possível simular múltiplos construtores
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        self.__estado = estado
        self.__custo = custo
        self.__profundidade = 0
        
        self.__operador = operador
        self.__antecessor = antecessor                          #o antecessor indica o nó a partir do qual o nó atual foi expandido
         
        if(operador is not None and antecessor is not None):    #construtor no caso de haver operador e antecessor                                       
            self.__profundidade = antecessor.profundidade + 1   #se houver antecessor, a profundidade é iniciada com a profundidade do nó antecessor mais 1
                                                                #a profundidade serve para indicar quantos nós antecedem este
            
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def antecessor(self):
        return self.__antecessor
            