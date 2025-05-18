class No:
    """
    Representação de um nó neuronal, cada nó possui um estado e pode, ou não, possuir um operador e sucessor
    """
    
    #ao criar atributos fora de métodos, estes são estáticos
    #se forem acedidos usando self., tornam-se atributos de instância
    nos_criados = 0
    nos_eliminados = 0
    nos_memoria_maximo = 0
    
    #ao definir o construtor com argumentos opcionais, é possível simular múltiplos construtores
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        self.__estado = estado
        self.__custo = custo
        self.__profundidade = 0
        self.__prioridade = None
        
        self.__operador = operador
        self.__antecessor = antecessor                          #o antecessor indica o nó a partir do qual o nó atual foi expandido
         
        if(operador is not None and antecessor is not None):    #construtor no caso de haver operador e antecessor                                       
            self.__profundidade = antecessor.profundidade + 1   #se houver antecessor, a profundidade é iniciada com a profundidade do nó antecessor mais 1
                                                                #a profundidade serve para indicar quantos nós antecedem este
        else:                                                   #reinicia as contagens de nó se este nó não tiver antecessores
            No.nos_criados = 0
            No.nos_eliminados = 0
            No.nos_memoria_maximo = 0
        
        No.nos_criados += 1                                     #incrementa o número total de nós criados
        nos_memoria = No.nos_criados - No.nos_eliminados
        if No.nos_memoria_maximo < nos_memoria:
            No.nos_memoria_maximo = nos_memoria
            
    def __lt__(self, outro_no):
        return self.prioridade < outro_no.prioridade
    
    @property
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter
    def prioridade(self, prioridade):
        self.__prioridade = prioridade
    
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
    
    def __del__(self):
        No.nos_eliminados += 1
            