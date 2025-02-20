package agente;

import ambiente.Ambiente;

//classe abstrata Agente que implementa métodos não-abstratos
public abstract class Agente {
    //propriedade ambiente do tipo Ambiente, deverá ser inicializada dentro do contrutor de forma a implementar a associação correta
    private Ambiente ambiente;
    //propriedade controlo do tipo Controlo, deverá ser inicializada fora do contrutor de forma a implementar a associação correta
    private  Controlo controlo;
    public Agente(Ambiente ambiente, Controlo controlo){}
    public void Executar(){}
    protected Percepcao percepcionar(){}
    protected void actuar(Accao accao){}
}
