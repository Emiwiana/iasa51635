package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/**
 * Classe pública ControloPersonagem que implementa a Interface Controlo
 */
public class ControloPersonagem implements Controlo {
    private MaquinaEstados maqest;

    /**
     * Método público construtor da classe ControloPersonagem.
     *
     * Inicia e programa a máquina de estados de acordo com o diagrama de máquina de estado dado
     */
    public ControloPersonagem(){
        //declaração dos estados
        Estado procura = new Estado("Procura");
        Estado observacao = new Estado("Observacao");
        Estado registo = new Estado("Registo");
        Estado inspeccao = new Estado("Inspecção");

        //declaração das acções
        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);

        //define as transições da máquina de estados
        //transições do estado procura
        procura
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.RUIDO, inspeccao, aproximar)
                .transicao(EventoJogo.SILENCIO, procura, procurar);
        //transições do estado inspecção
        inspeccao
                .transicao(EventoJogo.RUIDO, inspeccao, procurar)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.SILENCIO, procura);
        //transições do estado observação
        observacao
                .transicao(EventoJogo.ANIMAL, registo, observar)
                .transicao(EventoJogo.FUGA, inspeccao);
        //transições do estado registo
        registo
                .transicao(EventoJogo.ANIMAL, registo, fotografar)
                .transicao(EventoJogo.FUGA, procura)
                .transicao(EventoJogo.FOTOGRAFIA, procura);

        //inicia a máquina de estados no estado inicial (procura)
        maqest = new MaquinaEstados(procura);
    }

    /**
     * o estado da personagem é o estado da maquina de estados, então este é obtido apenas por um getter
     * @return estado da personagem
     */
    public Estado getEstado(){
        return maqest.getEstado();
    }

    /**
     * Método privado mostrar, imprime o nome do estado atual da máquina de estados para a consola.
     */
    private void mostrar(){
        System.out.printf("Estado: %s\n",getEstado().getNome());
    }

    //método a ser implementados de modo a concretrizar o contrato com a interface Controlo

    /**
     * Processa uma percepção, começando por obter a sua ação e processando-a tendo em conta a máquina de estados
     * de modo a avançá-la. Em seguida imprime o novo estado e retorna a ação que ocorreu.
     * @param percepcao
     * @return
     */
    public Accao processar(Percepcao percepcao){
        Evento evento = percepcao.getEvento();
        Accao accao = maqest.processar(evento);
        mostrar();
        return accao;
    }
}
