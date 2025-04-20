from .comport_comp import ComportComp

class Hierarquia(ComportComp):
    """
    Implementação do mecanismo de um comportamento composto tendo em conta a seleção atravéz de hierarquia
    <p>
    Representa um comportamento composto por vários comportamentos ao derivar da classe ComportamentoComposto.
    Utiliza um mecanismo de seleção por hierarquia de modo a determinar a acção 
    a realizar em função das respostas dos vários comportamentos internos.
    """
    
    def __init__(self, comportamentos):
        super().__init__(comportamentos)
        
    def seleccionar_accao(self, accoes):
        """
        Implementa o mecanismo de seleção de acções atravéz de hierarquia
        <p>
        Seleciona a acção no topo da hierarquia, isto é, a primeira da lista
        Args:
            accoes (list): Lista de ações
        Returns:
            acção no topo da hierarquia
        """
        return accoes[0]