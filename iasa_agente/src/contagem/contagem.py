from modelo.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_prof_iter import ProcuraProfIter

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2]

problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)
mec_procura = ProcuraProfundidade()
solucao = mec_procura.procurar(problema)
if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    passos = []
    for passo in solucao:
        passos.append(passo.estado.valor)
    print(f"Passo: {passos}")