from dataclasses import dataclass
from mod.operador import Operador
from mod.estado import Estado
        
@dataclass #a anotação dataclasse gera getter e setter para cada atributo, mudando os atributos de read-only para read-write
class PassoSolucao:
    estado: Estado
    operador: Operador