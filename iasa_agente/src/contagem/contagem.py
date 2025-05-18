from modelo.problema_contagem import ProblemaContagem
from modelo.heuristica_constagem import HeuristicaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.melhor_prim.aval.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_aa import ProcuraAA

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2, -1]

problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)
mec_procura = ProcuraLargura()
heuristica = HeuristicaContagem(VALOR_FINAL)
solucao = mec_procura.procurar(problema)
if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    print(f"Nós processados: {mec_procura.nos_processados}")
    print(f"Nós em memória: {mec_procura.nos_em_memoria}")
    #print(f"Numero de Estados Repetidos: {mec_procura.estados_repetidos}")
    passos = []
    for passo in solucao:
        passos.append(passo.operador.incremento)
    print(f"Passos: {passos}")
else:
    print("solução não encontrada")
    
"""
RESULTADOS DA CONTAGEM DE ESTADOS REPETIDOS
As alterações foram feitas na classe ProcuraGrafo, com comentários na classe referentes às mesmas
Criei uma propriedade "estados_repetidos" para conter a contagem, e no método manter, sempre que é verificado
que um nó já se encontra no dicionário da memória, esta contagem é incrementada.

ProcuraAA
Dimensão: 9
Custo: 9
Nós processados: 28
Nós em memória: 22
Numero de Estados Repetidos: 16
Passos: [1, 1, 1, 1, 1, 1, 1, 1, 1]

Podemos então verificar que nesta procura, o algoritmo encontrou 16 estados repetidos, tendo os de modo a 
tornar a procura mais eficiente.
"""
    
    
"""
PARAMS:
VALOR_INICIAL = 0
VALOR_FINAL = 20
INCREMENTOS = [5, 1, 6, 3, 5]

Procura em Profundidade 
Dimensão: 4
Custo: 100
Nós processados: 21
Nós em memória: 21
Passos: [5, 5, 5, 5]

Esta procura encontrou a melhor solução, em termos de menor dimensão, uma vez que o valor "5" é o primeiro da lista.
Esta procura foi também a mais eficiente em termos de uso total de recursos do sistema, uma vez que expandiu sempre
o primeiro nó da fronteira, até chegar à solução.

Procura em Largura
Dimensão: 4
Custo: 100
Nós processados: 781
Nós em memória: 781
Passos: [5, 5, 5, 5]

Esta procura foi a menos eficiente em termos de nós processados e dimensão, uma vez que antes de avançar para um novo nível
de profundidade, esta expande todos os nós, de modo a encontrar todas os estados possíveis até encontrar a primeira 
solução possível.

Procura em Profundidade Limitada
Dimensão: 4
Custo: 100
Nós processados: 21
Nós em memória: 21
Passos: [5, 5, 5, 5]

Procura em Profundidade Iterativa
Dimensão: 4
Custo: 100
Nós processados: 21
Nós em memória: 21
Passos: [5, 5, 5, 5]

Uma vez que a dimensão da solução da procura em profundidade é 4, é de esperar que as soluções da procura em profundidade
limitada e iterativa fossem iguais, uma vez que a profundidade máxima definida (5) é maior que a dimensão da solução
encontrada. Se a solução fosse maior, era de esperar que na profundidade limitada não fosse encontrada, e na iterativa, 
o valor da profundidade máxima fosse incrementada até chegar à primeira soluºão.

Procura custo Uniforme
Dimensão: 20
Custo: 20
Nós processados: 161
Nós em memória: 76
Numero de Estados Repetidos: 135
Passos: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Uma vez que esta procura explora sempre os nós com menor custo, pelo que 
a fronteira está ordenada tendo em conta o custo dos nós, sendo estes onde o incremento é 1, o número de passos
para chegar à solução é o maior possível (20), sendo o custo também o menor possível.
Uma vez que esta procura implementa a verificação de estados repetidos, esta torna-se mais eficiente
em termos de recursos do sistema, pelo que não explora caminhos redundantes.

Procura Sofrega
Dimensão: 5
Custo: 110
Nós processados: 26
Nós em memória: 23
Numero de Estados Repetidos: 6
Passos: [6, 6, 6, 1, 1]

Esta procura tenta encontrar a solução que explora o menor número de nós possíveis, ao procurar reduzir a heuristica
o máximo possível em cada estado.
A solução encontra-se dentro dos parâmetros esperados, uma vez que avança sempre a contagem o máximo possível
em cada passo para chegar à solução.


Procura AA
Dimensão: 20
Custo: 20
Nós processados: 101
Nós em memória: 83
Numero de Estados Repetidos: 75
Passos: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


"""