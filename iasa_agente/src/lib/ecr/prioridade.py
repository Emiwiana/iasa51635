from .comport_comp import ComportComp

class Prioridade(ComportComp):
    """
    Implementação do mecanismo de um comportamento composto tendo em conta a seleção atravéz da prioridade dinãmica
    <p>
    Representa um comportamento composto por vários comportamentos ao derivar da classe ComportamentoComposto.
    Utiliza um mecanismo de seleção por prioridade dinâmica de modo a determinar a acção 
    a realizar em função das respostas dos vários comportamentos internos.
    """
    def seleccionar_accao(self, accoes):
        """
        Implementa o mecanismo de seleção de ações tendo em conta o critério de prioridade dinâmica
        <p>
        Percorre a lista de accoes, retornando a acção cujo valor de prioridade é o maior
        Args:
            accoes (list): Lista de ações
        Returns:
            accao: accao com maior prioridade segundo o critério de prioridade dinâmica
        """
        return max(accoes, key=lambda accao: accao.prioridade) 
        #retornar a maior acção sendo que a a chave de seleção da maior acção é dada pela função lambda
        #função lambda que recebe a acção e devolve a prioridade da acção