package agente;
import agente.Percepcao;
import agente.Accao;

public interface Controlo {
        default Accao processar(Percepcao percepcao){}
}
