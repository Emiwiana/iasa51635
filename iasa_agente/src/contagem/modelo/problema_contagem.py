from mod.problema import Problema
from .estado_contagem import EstadoContagem
from .operador_incremento import OperadorIncremento

class ProblemaContagem(Problema):
    def __init__(self, valor_inicial, valor_final, incrementos):
        
        operadores = [OperadorIncremento(incremento) for incremento in incrementos ]
        super().__init__(EstadoContagem(valor_inicial), operadores)
        self.__valor_final = valor_final
        
    def objetivo(self, estado):
        return estado.valor >= self.__valor_final