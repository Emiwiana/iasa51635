package maqest;

import agente.Accao;
import ambiente.Evento;

/**
 * representação de uma máquina de estados em código java.
 * Esta classe permite a implementação de uma máquina de estados construida como o utilizador queira.
 *
 * Esta máquina de estados possui 3 alfabetos, o alfabeto de entrada, de saída e de o conjunto de estados.
 * Desta forma, ao receber um símbolo de entrada, a máquina altera o estado atual para o próximo definido pelo
 * programador, e retorna um símbolo de saída associado à transição que ocorreu.
 *
 * O sistema evolui em base a duas funções de transformação, delta e lambda, a função delta trata-se da função de transição
 * de estado, implementada em base de uma tabela de transição de estado, na qual é dada como entrada um evento, e um estado atual,
 * e como saída, um novo estado. A função lambda trata-se de uma função de saída, dada por uma tabela de saída, onde dado um
 * estado atual e evento como entrada, retorna como saída uma acção
 */
public class MaquinaEstados {
    /**
     * estado atual da máquina de estados, privado de modo a realizar a sua propriedade read-only
     */
    private Estado estado;

    /**
     * método getter do estado atual de modo a realizar a propriedade read-only
     * @return estado atual
     */
    public Estado getEstado(){
        return this.estado;
    }

    /**
     * Método construtor da máquina de estados, inicializa-a no estado inicial de acordo com o diagrama de estados dado
     * @param estadoinicial estado inicial da máquina de estados
     */
    public MaquinaEstados(Estado estadoinicial){
        this.estado = estadoinicial;
    }

    /**
     * implementação do método processar de acordo com o diagrama de sequência presente nos slides
     * @param evento evento a ser processado
     * @return nulo se a transição associada ao evento for nula, se não retorna a acção associada ao evento
     */
    public Accao processar(Evento evento){
        Transicao transicao = this.estado.processar(evento);
        //if é equivalente ao operador alt no diagrama
        if(transicao != null){
            this.estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        } else return null;
    }
}
