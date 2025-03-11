package maqest;

import agente.Accao;

/**
 * Classe que representa uma transição entre estados, associada a cada transição está uma acção (símbolo de saida) e
 * o estado sucessor a esta transição.
 */
public class Transicao {
    /**
     * acção associada a esta instância da transição
     */
    private Accao accao;

    /**
     * método getter do atributo acção
     * @return acção
     */
    public Accao getAccao(){
        return this.accao;
    }

    /**
     * estado sucessor associado a esta transição
     */
    private Estado estadoSucessor;

    /**
     * método getter do estado sucessor
     * @return estado sucessor
     */
    public Estado getEstadoSucessor(){
        return this.estadoSucessor;
    }

    /**
     * Inicia uma transição, armazenando nela o estado sucessor e acção
     * @param estadoSucessor estado sucessor associado a esta transição
     * @param accao acção associada a esta transição
     */
    public Transicao(Estado estadoSucessor, Accao accao){
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }
}
