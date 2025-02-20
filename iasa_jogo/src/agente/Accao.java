package agente;

import ambiente.Comando;

public class Accao {
    //atributo read-only comando, privado de modo a implementar a propriedade read-only em conjunto com o método getter
    private Comando comando;
    //construtor da classe accao com o atributo comando do tipo Comando
    Accao(Comando comando){}

    //método getter de modo a realizar a propriedade read-only do atributo comando, de modo a que este não possa ser alterado por outra Classe mas possa ser acedido
    public Comando getComando(){}
}
