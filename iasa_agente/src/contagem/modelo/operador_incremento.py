from mod.operador import Operador
from .estado_contagem import EstadoContagem

class OperadorIncremento(Operador):
    """
    Representa os operadores do problema de contagem, isto é, as mudanças que ocorrem quando é criado um estado sucessivo.
    No contexto deste problema, o estado sucessivo será sempre o estado anterior com um incremento.
    """
    def __init__(self, incremento):
        super().__init__()
        self.incremento = incremento
        
    def aplicar(self, estado):
        """
        Aplica um incremento a um dado estado, criando um estado sucessor
        Args:
            estado (EstadoContagem): estado anterior

        Returns:
            EstadoContagem: estado sucessor
        """
        novo_valor = estado.valor + self.incremento
        return EstadoContagem(novo_valor)
    
    def custo(self, estado, estado_suc):
        """
        Calcula o custo da operação, e aplica-o ao operador (neste caso, o custo é o incremento ao quadrado)
        """
        return self.incremento ** 2