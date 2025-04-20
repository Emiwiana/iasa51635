from ecr.comportamento import Comportamento
from sae import Avancar, Rodar, Direccao
import random

class Explorar(Comportamento):
    """
    Comportamento completo explorar que realiza o contrato Comportamento
    <p>
    Responsável pelo movimento aleatório do agente no ambiente
    """
    def __init__(self, probabilidade_rotacao = 0.7):
        """
        Instância uma instância de classe Explorar com a probabilidade da acção escolhida na activação
        Args:
            probabilidade_rotacao (float): Probabilidade de a acção escolhida ser rodar, valor entre 0 e 1
        """
        self.__probabilidade_rotacao = probabilidade_rotacao
        self.__direccoes = list(Direccao) #cria a lista de direcções apenas uma vez quando a classe é instanciada
       
    def activar(self, percepcao):
        """
        Gera um comportamento aleatório em que o agente movimenta-se de forma aleatória no ambiente
        atravéz das acções avançar e rodar.
        Args:
            percepcao (Percepcao): Apenas presente para garantir o contrato, neste caso é ignorada
        Returns:
            Accao: Acção a ser tomada pelo agente
        """
        
        if random.random() > self.__probabilidade_rotacao: #gera um número entre 0 e 1 e verifica se este é maior ou menor que a probabilidade de rotação para escolher a acção gerada
            direccao_aleatoria = random.choice(self.__direccoes) #escolhe aleatóriamente uma direcção a partir da lista de direcções
            accao = Rodar(direccao_aleatoria)
        else:
            accao = Avancar()
        return accao