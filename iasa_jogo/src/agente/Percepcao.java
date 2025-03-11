package agente;
import ambiente.Evento;

/**
 * Classe pública Percepção
 */
public class Percepcao {
    /**
     * Atributo read-only evento, privado de modo a implementar a propriedade read-only em conjunto com o método getter
     */
    private Evento evento;

    /**
     * Construtor público da classe percepção
     * @param evento
     */
    public Percepcao(Evento evento){
        this.evento= evento;
    }

    /**
     * Método público getter de modo a realizar a propriedade read-only do atributo evento, de modo a que este não possa ser alterado por outra Classe mas possa ser acedido
     * @return atributo read-only evento
     */
    public Evento getEvento(){
        return this.evento;
    }
}
