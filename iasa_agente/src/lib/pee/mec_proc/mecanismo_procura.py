from abc import ABC
from .no import No
from .solucao import Solucao

class MecanismoProcura(ABC):
    """
    Classe abstrata que representa um mecanismo de procura genérico, a ser implementada de modo a implementar
    outros mecanismos de procura.
    Trata a gestão da fronteira de exploração.
    """
    
    def __init__(self, fronteira):
        self._fronteira = fronteira
    
    def _iniciar_memoria(self):
        """
        Inicia estruturas de memória de procura de acordo com o tipo de procura, incluindo a fronteira de exploração.
        (pg.5 ppt-p3)
        """
        self._fronteira.iniciar()
    
    def _memorizar(self, no):
        """
        Memoriza um nó, concretização depende do tipo de procura.
        (pg.5 ppt-p3)

        Args:
            no (No): Nó a ser memorizado
        """
        self._fronteira.inserir(no)
    
    def procurar(self, problema):
        self._iniciar_memoria()                                 #inicia a memória do mecanismo de fronteira
        no = No(problema.estado_inicial)                        #cria o nó correspondente ao estado inicial.
        self._memorizar(no)                                     #memoriza o nó inicial
        while not self._fronteira.vazia:                        #enquanto a fronteira não for vazia,
            no = self._fronteira.remover()                      #remove o primeiro nó da fronteira.
            if problema.objetivo(no.estado):                   #verifica se o estado do nó é objetivo,
                return Solucao(no)                              #retorna a solução que termina no nó.
            for no_sucessor in self._expandir(problema, no):    #expande o nó e insere cada nó sucessor na fronteira.
                self._memorizar(no_sucessor)
        return None                                             #caso a fronteira esteja vazia, retorna None de modo a definir que não existe solução.
    
    def _expandir(self, problema, no):
        sucessores = []                                                 #Inicia lista de sucessores vazia
        estado = no.estado                                              #Obtem o estado do nó
        for operador in problema.operadores:                            #Para cada operador do problema,
            estado_suc = operador.aplicar(estado)                       #gerar estado sucessor aplicando o operador ao estado atual,
            if estado_suc is not None:                                  #se o nó sucessor existir,
                custo = no.custo + operador.custo(estado, estado_suc)   #calcula o custo do nó sucessor,
                no_successor = No(estado_suc, operador, no, custo)      #gera o nó sucessor,
                sucessores.append(no_successor)                         #junta o nó sucessor à lista de nós sucessores,
        return sucessores                                               #Retorna a lista de nós sucessores.