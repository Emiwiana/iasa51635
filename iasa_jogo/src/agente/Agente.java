package agente;

import ambiente.Ambiente;

/**
 * Classe abstrata Agente que implementa 4 métodos não-abstratos
 */
public abstract class Agente {
    /**
     * Atributo ambiente do tipo Ambiente, deverá ser inicializada dentro do construtor de forma a implementar a associação correta
     */
    private Ambiente ambiente;
    /**
     * Atributo controlo do tipo Controlo, deverá ser inicializada fora do construtor de forma a implementar a associação de agregação
     */
    private Controlo controlo;

    /**
     * Método construtor público da classe Agente
     * @param ambiente
     * @param controlo
     */
    public Agente(Ambiente ambiente, Controlo controlo){}

    /**
     * Método público executar do tipo Void
     */
    public void executar(){}

    /**
     * Método protegido percepcionar
     * @return Percepcao
     */
    protected Percepcao percepcionar(){}

    /**
     * Método protegido actuar do tipo void
     * @param accao
     */
    protected void actuar(Accao accao){}
}
