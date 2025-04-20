from .passo_solucao import PassoSolucao

#o estereótipo <<iterable>> indica a definição de mecanismos de iteração
class Solucao():
    
    def __init__(self, no_final):
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo)
            no = no.antecessor

    #se uma classe tiver um método iter, e retornar um iterador, transforma-se numa classe iterável
    def __iter__(self):
        return iter(self.__passos)
    
    def __getitem__(self, index):
        return self.__passos[index]
    
    @property
    def dimensao(self):
        return self.__no_final.profundidade
    
    @property
    def custo(self):
        return self.__no_final.custo