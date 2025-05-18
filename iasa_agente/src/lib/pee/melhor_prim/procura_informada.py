from abc import ABC
from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim, ABC):
    def procurar(self, problema, heuristica):
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)
    