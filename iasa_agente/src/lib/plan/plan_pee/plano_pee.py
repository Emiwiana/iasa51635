from ..plano import Plano

class PlanoPEE(Plano):
    
    @property
    def dimensao(self):
        return len(self.__passos)
    
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]
        
    def obter_accao(self, estado):
        """
        Retorna a primeira ação do plano, removendo-a do array de modo à execução
        dela não ser repetida.
        Args:
            estado (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operador
    
    def mostrar(self, vista):
        """
        Representa o plano através de várias setas, a indicar a direção para onde o agente se irá movimentar.
        Args:
            vista (_type_): _description_
        """
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, 
                                     passo.operador.ang)
            