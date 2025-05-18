from sae import Simulador
from agente.agente_react import AgenteReact
from agente.agente_delib import AgenteDelib

"""
simulador = Simulador(1, AgenteReact()) #instancia o agente e inicia-o no simulador
simulador.executar() #executa o simulador
"""

#executa a simulação do agente deliberativo
Simulador = Simulador(4, AgenteDelib(), vista_modelo=True)
Simulador.executar()