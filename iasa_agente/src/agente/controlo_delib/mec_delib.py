from sae import Elemento

class MecDelib:
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
        
    def deliberar(self):
        """
        Implementa o Mecanismo de deliberação que gera e depois selecciona os objectivos
        a serem usados pelo controlo de deliberação para gerar um plano de acção.
        Returns:
            list: Lista de objectivos, ordenada segunda a sua distância ao agente
        """
        objectivos = self.__gerar_objectivos()
        if objectivos:
            return self.__seleccionar_objectivos(objectivos)
        
    def __gerar_objectivos(self):
        """
        Gera um conjunto de objectivos a ser seguidos pelo agente
        Returns:
            list: Lista de objectivos
        """
        return [estado for estado in self.__modelo_mundo.obter_estados()        #gera uma list usando um mecanismo de geradores
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO] #constituida por estados, para cada estado estados do mundo, se 
                                                                                #cada elemento do estado for ALVO
        
    def __seleccionar_objectivos(self, objectivos):
        """
        Ordena os objectivos segundo a sua distância ao agente
        Args:
            objectivos (list): lista de objectivos

        Returns:
            list: Lista de objectivos ordenada
        """
        objectivos.sort(key = self.__modelo_mundo.distancia) #o método distancia é passado como objeto para ser activado dinâmicamente por cada elemento dos objectivos
        return objectivos