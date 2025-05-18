from sae import Agente
from .controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE


class AgenteDelib(Agente):
    """
    """
    def __init__(self):
        """
        Inicia uma instância da classe AgenteDelib, criando uma instância da classe PlaneadorPEE, responsável
        pela criação de um plano para o agente
        """
        super().__init__()
        self.__controlo = ControloDelib(PlaneadorPEE())
    
    def executar(self):
        """
        Método responsável pela execução do comportamento do agente, começa por gerar uma percepção,
        após isso gera um plano atravez da percepção gerada usando o controlo deliberativo como meio e por fim
        actua as acções que compõem o plano de modo
        """
        percepcao = super()._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        super()._actuar(accao)