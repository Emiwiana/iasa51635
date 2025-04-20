from ecr.estimulo import Estimulo

class EstimuloObst(Estimulo):
    """
    Representa o estimulo ao interagir com um obstáculo presente para o funcionamento do comportamento evitar
    """
    def __init__(self, direccao, intensidade = 1.0):
        super().__init__()
        self.__intensidade = intensidade
        self.__direccao = direccao
        
    def detectar(self, percepcao):
        """
        Detecta contacto com um obstáculo usando uma percepção
        Args:
            percepcao (Percepcao): percepção usada para detectar o obstaculo

        Returns:
            float: valor da intensidade quando o agente encontra-se junto a um obstáculo
        """
        return self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0