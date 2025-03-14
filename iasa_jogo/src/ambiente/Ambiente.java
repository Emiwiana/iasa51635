package ambiente;
import ambiente.Evento;
import ambiente.Comando;

/**
 * Interface pública Ambiente, dependente nas interfaces Comando e Evento
 */
public interface Ambiente {
    /**
     * Método público evoluir
     */
    default void evoluir(){}

    /**
     * Método público observar
     * @return Evento
     */
    default Evento observar(){
        return null;
    }

    /**
     * Método público executar
     * @param comando
     */
    default void executar(Comando comando){}
}
