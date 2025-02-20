package ambiente;
import ambiente.Evento;
import ambiente.Comando;

public interface Ambiente {
    default void evoluir(){}
    default Evento observar(){}
    default void executar(Comando comando){}
}
