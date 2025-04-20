from sae import Agente
from .controlo_react.controlo_react import ControloReact
from .controlo_react.reaccoes.recolher import Recolher


class AgenteReact(Agente):
    """
    Implementação do mecanismo Agente Reactivo
    <p>
    Responsável pela execução do comportamento do agente atravez do método executar.
    Este agente é reactivo uma vez que o seu comportamento é gerado a partir da seleção de comportamentos em base no ambiente.
    """
    def __init__(self):
        """
        Inicializa uma instância da classe AgenteReact, criando uma instância da classe ControloReact, responsável
        pelo controlo do agente
        """
        super().__init__()
        self.__controlo = ControloReact(Recolher()) #cria um controlo reactivo com o comportamento explorar
    
    def executar(self):
        """
        Método responsável pela execução do comportamento do agente, começa por gerar uma percepção,
        após isso gera uma acção atravez da percepção gerada usando o controlo reactivo como meio e por fim
        actua essa ação sobre o ambiente.
        """
        percepcao = super()._percepcionar()
        accao = self.__controlo.processar(percepcao)
        super()._actuar(accao)