class ControloReact:
    """
    Implementação do mecanismo Controlo Reactivo.
    <p>
    Este mecanismo é responsável por relacionar as percepções com ações, realizado num módulo comportamental (comportamento)
    que representa o comportamento geral do agente.
    """
    def __init__(self, comportamento):
        """
        Método construtor da classe ControloReact.
        Args:
            comportamento (Comportamento): comportamento que representa o comportamento geral do agente
        """
        self.__comportamento = comportamento
    
    def processar(self, percepcao):
        """
        Retorna a acção que resulta da ativação do comportamento interno em base da percepção recebida
        Args:
            percepcao (Percepcao): percepção responsável por ativar o comportamento
        Returns:
            Accao: acção resultante de ativação do comportamento
        """
        return self.__comportamento.activar(percepcao)