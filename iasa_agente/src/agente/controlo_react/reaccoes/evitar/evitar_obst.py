from ecr.hierarquia import Hierarquia
from sae import Direccao
from .evitar_dir import EvitarDir

class EvitarObst(Hierarquia):
    """
    Define um comportamento composto, no qual o comportamento a ser executade é escolhido em base numa seleção de
    Hierarquia.
    
    Este comportamento é composto por um comportamento EvitarDir para cada direção possível.
    """
    def __init__(self):
        super().__init__([EvitarDir(direccao) for direccao in Direccao])