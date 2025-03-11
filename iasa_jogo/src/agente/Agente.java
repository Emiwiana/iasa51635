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
    public Agente(Ambiente ambiente, Controlo controlo){
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /**
     * Método público executar do tipo Void
     */
    public void executar(){
        Percepcao percepcao = this.percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);

        //maneira alternativa de implementar
        //actuar(controlo.processar(percepcionar()));
    }

    /**
     * Método protegido percepcionar
     *
     *
     *
     * @return Percepcao
     */
    protected Percepcao percepcionar(){
        ambiente.Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    /**
     * Método protegido actuar do tipo void
     *
     * Se a accão não for nula, executa o comando da acção
     *
     * @param accao
     */
    protected void actuar(Accao accao){
        if(accao != null){
            ambiente.executar(accao.getComando());
        }
    }
}
