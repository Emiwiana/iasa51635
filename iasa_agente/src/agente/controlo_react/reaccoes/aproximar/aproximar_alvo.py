from ecr.prioridade import Prioridade
from .aproximar_dir import AproximarDir
from sae import Direccao

class AproximarAlvo(Prioridade):
    """
    Representa um comportamento composto de seleção do tipo Prioridade, composto por comportamentos
    "AproximarDir" para cada direção possível. Isto de modo a que o agente se desloque para o alvo mais
    próximo uma vez que o comportamento da direção selecionada será o que o leva ao alvo mais
    próximo.
    """
    def __init__(self):
        #gera uma lista com objetos da classe AproximarDir em que o parâmetro de cada elemento é cada uma das direções no enum Direccao
        comportamentos = [AproximarDir(direccao) for direccao in Direccao]
        super().__init__(comportamentos)