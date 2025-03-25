class Resposta:
    """
    Implementação do mecanismo base de uma resposta
    <p>
    Representa a geração de uma resposta a um estímulo.
    """
    def __init__(self, accao):
        """
        Método construtor da classe Resposta
        Args:
            accao (Accao): _description_
        """
        self._accao = accao
        raise NotImplementedError
        
    #intensidade é 0.0 (em vez de apeans 0) de modo a especificar que a varável está a ser inicializada como float
    def activar(self, percepcao, itensidade = 0.0):
        """
        activa uma percepcao
        Args:
            percepcao (Percepccao): percepcao a ser activada
            itensidade (float, optional): _description_ Defaults to 0.
        Returns:
            accao Accao: accao retornada pela ativação da percepção
        """
        raise NotImplementedError