from .avaliador_custo_unif import AvaliadorCustoUnif
from ..procura_melhor_prim import ProcuraMelhorPrim

class ProcuraCustoUnif(ProcuraMelhorPrim):
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())