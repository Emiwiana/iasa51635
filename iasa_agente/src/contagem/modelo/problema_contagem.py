from mod.problema import Problema
from .estado_contagem import EstadoContagem
from .operador_incremento import OperadorIncremento

class ProblemaContagem(Problema):
    """
    Implementa um problema "contagem",no qual dado um valor inicial, um valor final e uma lista de incrementos
    o programa procura chegar ao valor final somando os incrementos ao valor inicial.
    
    Para isso é preciso definir o objetivo do problema (o valor com incrementos encontrar-se com o valor final).
    Os estados e operadores deste problema estão implementados na classe "EstadoContagem" e "OperadorIncremento",
    havendo um operador para cada incremento.
    """
    def __init__(self, valor_inicial, valor_final, incrementos):
        
        operadores = [OperadorIncremento(incremento) for incremento in incrementos ]
        super().__init__(EstadoContagem(valor_inicial), operadores)
        self.__valor_final = valor_final
        
    def objetivo(self, estado):
        return estado.valor >= self.__valor_final