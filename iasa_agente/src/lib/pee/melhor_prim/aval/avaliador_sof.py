from .avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    """
    Classe responsável por definir como a prioridade dos elementos da fronteira da procura sófrega é definida.
    """
    def prioridade(self, no):
        """
        Define a prioridade de um dado nó da fronteira.
        Uma vez que se trata da procura sófrega, este será definido apenas pela heurística, uma vez
        que nesta procura é sempre selecionado o nó com menor heurística para ser expandido.

        Args:
            no (No): nó a ser definida a prioridade

        Returns:
            int: prioridade do nó
        """
        return self.heuristica.h(no.estado)