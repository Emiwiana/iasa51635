#importa a classe presente num ficheiro diferente
# "." indica um import relativo (ao módulo), cada ponto indica para procurar a um nível acima da pasta, começando na pasta atual
# como é apenas ".", encontra-se na pasta atual

#para um import poder ser absoluto, este tem de se encontrar nas bibliotecas do python ou na pythonpath configurada

#imports absolutos usam-se para obter bibliotecas, imports relativos encontram-se DENTRO das bibliotecas
#como está a ser desenvolvida uma biblioteca, o import deve ser relativo
from .comportamento import Comportamento

class Reaccao(Comportamento):
    """
    Implementação do mecanismo base de uma reacção
    <p>
    Associa um estímulo a uma resposta.
    """
    def __init__(self, estimulo, resposta):
        """
        Método construtor da classe Reaccao
        Args:
            estimulo (Estimulo): elemento privado estimulo
            resposta (Resposta): elemento privado resposta
        """
        #declaração das variáveis da classe no construtor
        self.__estimulo = estimulo
        self.__resposta = resposta
    
    def activar(self, percepcao):
        """
            ativa um comportamento dado uma percepção
        Args:
            percepcao (Percepcao): _description_
        Returns:
            Accao: accao originante da percepção ativada
        """
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0: #operador opt corresponde a um 'if' sem 'else'
            accao = self.__resposta.activar(percepcao, intensidade)
            #accao é uma variãvel explicativa
            # - pode ser eliminada e só está presente de modo a tornar o código mais evidente
            return accao
        #não existe "return None" uma vez que uma função de python retorna a marca "None" por omissão

        