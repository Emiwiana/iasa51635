from sae import Simulador
from agente.agente_react import AgenteReact

simulador = Simulador(1, AgenteReact()) #instancia o agente e inicia-o no simulador
simulador.executar() #executa o simulador
