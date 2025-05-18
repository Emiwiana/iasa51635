from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof

class ProcuraSofrega(ProcuraInformada):
    """
    Implementação da procura sófrega (greedy search), na qual é minimizado o custo para atingir o objectivo,
    sem ter em conta o custo do percurso já explorado, isto é, o critério para escolher o nó a ser explorado
    é apenas ter a menor heurística de todos os da fronteira.
    
    Isto é realisado através da implementação da classe AvaliadorSof, que define a prioridade dos elementos da fronteira
    de modo a realizar a exploração desejada.
    """
    def __init__(self):
        super().__init__(AvaliadorSof())