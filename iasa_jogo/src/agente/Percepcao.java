package agente;
import ambiente.Evento;

public class Percepcao {
    //atributo read-only evento, privado de modo a implementar a propriedade read-only em conjunto com o método getter
    private Evento evento;
    //construtor da classe percepção com o atributo evento do tipo Evento
    Percepcao(Evento evento){}
    //método getter de modo a realizar a propriedade read-only do atributo evento, de modo a que este não possa ser alterado por outra Classe mas possa ser acedido
    public Evento getEvento(){}
}
