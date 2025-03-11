package agente;
import agente.Percepcao;
import agente.Accao;

/**
 * Interface pública Controlo
 */
public interface Controlo {
        /**
         * Método público processar
         * @param percepcao
         * @return Accao
         */
        default Accao processar(Percepcao percepcao){return null;}
}
