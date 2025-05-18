from ..planeador import Planeador
from .plano_pee import PlanoPEE
from .mod_prob.problema_plan import ProblemaPlan
from .mod_prob.heur_dist import HeurDist
from pee.melhor_prim.procura_aa import ProcuraAA

class PlaneadorPEE(Planeador):
    
    def __init__(self):
        self.__mec_pee = ProcuraAA()                            #cria uma instãncia de procura a* a ser usada para criar um plano
        
    def planear(self, modelo_plan, objectivos):
        estado_final = objectivos[0]                            #instancia o estado final, equivalente ao primeiro objectivo da lista
        problema = ProblemaPlan(modelo_plan, estado_final)      #instancia o problema com o modelo_plan e estado final
        heuristica = HeurDist(estado_final)                     #instancia a heuristica com o estado final
        solucao = self.__mec_pee.procurar(problema, heuristica) #calcula a solução, usando o mecanismo de procura
        return PlanoPEE(solucao)                                #retorna uma instância da classe PlanoPEE usando a solução