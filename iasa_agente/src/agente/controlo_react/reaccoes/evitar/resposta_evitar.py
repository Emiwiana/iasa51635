from ecr.resposta import Resposta
from sae import Accao
from sae import Rodar

class RespostaEvitar(Resposta):
    """
    Define a resposta do agente à detecção de um obstáculo.
    """ 
    def activar(self, percepcao, itensidade=0):
        """
        Define a resposta que o agente irá executar em base numa percepção e intensidade.
        
        Esta resposta é definida pela rotação do agente num único sentido de modo a ficar o mínimo de tempo
        possível preso num obstáculo.
        Args:
            percepcao (Percepcap): percepção do agente
            itensidade (float, optional): intensidade do estimulo que gerou esta resposta.
        """
        dir_actual = percepcao.direccao
        if percepcao.contacto_obst(dir_actual):
            nova_direccao = dir_actual.rodar()
            self._accao = Rodar(nova_direccao) #roda o agente sempre na mesma direção. isto porque se a direção for aleatória, existe uma maior chance de o agente ir contra o obstáculo mais vezes
            return super().activar(percepcao, itensidade)
            
        