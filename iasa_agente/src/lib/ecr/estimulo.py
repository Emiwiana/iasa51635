from abc import ABC, abstractmethod #import de biblioteca que deixa indicar classes abstratas em python

#atravéz do uso do parâmetro "ABC", indica-se que a classe é abstrata
#isto é feito porque uma interface é equivalente a uma classe abstrata sem atributos
class Estimulo(ABC): 
    """
    Interface que define a funcionalidade geral de um estímulo (concretizado em função do problema a resolver)
    <p>
    Representa a detecção de um estímulo presente numa percepção.
    """
    
    #a tag abstractmethod indica que o método é abstrato
    #o método não tem corpo (apenas comentários) uma vez que serve de contrato para outra classe o implementar
    @abstractmethod
    def detectar(self, percepcao):
        """
        Método abstrato responsável por detectar estimulo da percepção
        Args:
            percepcao (Percepcao): percepcao cujo estimulo é detetado
        Returns:
            elemento do tipo float
        """