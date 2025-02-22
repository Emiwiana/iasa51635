package ambiente;
import ambiente.Evento;
import ambiente.Comando;

/**
 * Interface pública Ambiente
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
    default Evento observar(){}

    /**
     * Método público executar
     * @param comando
     */
    default void executar(Comando comando){}
}
