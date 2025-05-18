from abc import ABC, abstractmethod

#o parâmetro <<hashable>> indica que a classe implementa um mecanismo de identificação única
class Estado(ABC):
    """
    Representação abstrata de um estado a ser implementado por outras classes
    que representem estados concretos.
    
    Implementa um mecanismo de identificação única de modo a ser comparável com
    outras instâncias desta classe.
    """
    
    @abstractmethod
    def id_valor():
        """
        Função que gera o id único do estado de modo a ser comparado com outra instância de Estado
        Returns:
            int
        """
    
    #ao definir que a classe __hash__ retorna o id_valor, é possível comparar instâncias desta classe
    #uma vez que cada estado diferente terá um id_valor concreto
    #a função __hash__ é responsável pelo valor usado para testar a igualdade de instãncias da classe
    #por omissão retorna o valor do endereço memória, por isso não é possível comparar se é o mesmo estado 
    def __hash__(self):
        return self.id_valor()
    
    #se estivermos a comparar duas instâncias da classe estado, comparamos o valor da função __hash__ de ambos
    def __eq__(self, other):
        if isinstance(other, Estado):
            return hash(self) == hash(other)