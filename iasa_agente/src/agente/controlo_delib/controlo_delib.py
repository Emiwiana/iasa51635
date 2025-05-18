from .modelo.modelo_mundo import ModeloMundo
from .mec_delib import MecDelib

class ControloDelib:
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__plano = None
        self.__objectivos = None
    
    def processar(self, percepcao):
        """
        Implementa o processo de tomada de decisão e acção, gerando as acções a serem tomadas
        pelo agente de modo a determinar o seu comportamento, tendo em conta as percepções obtidas e
        o estado atual do mundo.
        Args:
            percepcao (Percepcao): _description_

        Returns:
            Accao: acção a ser executada segundo a decisão
        """
        self.__assimilar(percepcao) #actualiza o modelo do mundo tendo em conta a percepção recebida
        if(self.__reconsiderar()):  #Se o plano deve ser reconsiderado
            self.__deliberar()      #Gera um conjunto de objectivos de modo a deliberar o que fazer
            self.__planear()        #Gera um plano de acção tendo em conta os objectivos gerados
        return self.__executar()    #Retorna a acção a ser executada para cumprir o plano.
        
    
    def __assimilar(self, percepcao):
        """Actualiza o modelo do mundo tendo em conta a percepção
        Args:
            percepcao (Percepcao): percepção recebida
        """
        self.__modelo_mundo.actualizar(percepcao)
     
    def __reconsiderar(self):
        """
        Método booleano que indica se o plano deve ou não ser reconsiderado.
        Retorna true quando o modelo mundo foi alterado ou o plano não existe.
        Returns:
            boolean: Indicação de o plano deve ser alterado
        """
        return self.__modelo_mundo.alterado or self.__plano is None

    
    def __deliberar(self):
        """
        Gera um conjunto de objectivos através do uso do mecanismo de deliberação.
        """
        self.__objectivos = self.__mec_delib.deliberar()
    
    def __planear(self):
        """
        Cria um novo plano se houverem objectivos.
        """
        if self.__objectivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        else: 
            self.__plano = None
    
    def __executar(self):
        """
        Retorna a acção a ser executada de modo a seguir o plano.
        Se não houver plano ou o plano for inválido, retorna None
        Returns:
            Accao: acção do operador
        """
        if self.__plano:
            estado = self.__modelo_mundo.obter_estado() #verificar o estado se houver plano
            operador = self.__plano.obter_accao(estado) #obter operador do estado
            if operador:
                return operador.accao                   #se o operador for válido, retorna a sua acção
            else:
                self.__plano = None                     #senão, houve um erro,   invalida o plano
    
    def mostrar(self, vista):
        """
        Cria uma pre-visualização do plano e objectivos, de modo a poder ser observada a decisão tomada
        pelo agente
        Args:
            vista (Vista): _description_
        """
        vista.limpar()
        self.__modelo_mundo.mostrar(vista)
        if self.__plano:
            self.__plano.mostrar(vista)
        if self.__objectivos:
            for objectivo in self.__objectivos:
                vista.marcar_posicao(objectivo.posicao)
        
    