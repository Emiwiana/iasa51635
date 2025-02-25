package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Classe AmbienteJogo, implementa a interface Ambiente pois implementa os métodos evoluir, observar e executar
 */
public class AmbienteJogo implements Ambiente {
    /**
     * Container eventos que guarda uma quantidade entre 0 e infinito de instâncias de enumerações da classe EventoJogo.
     * Este mapa é usado de modo a atribuir um caracter de input do utilizador a um evento.
     */
    private final Map <String, EventoJogo> eventos;
    /**
     * Elemento read-only evento do tipo EventoJogo.
     * Privado de modo a realizar a sua propriedade read-only atravéz de um método getter público.
     */
    private EventoJogo evento;
    /**
     * Elemento scanner a ser usado para obter input do utilizador
     */
    private final Scanner scanner = new Scanner(System.in);

    /**
     * Construtor público da classe AmbienteJogo
     */
    public AmbienteJogo(){
        //inicialização do HashMap a ser usado, atribuindo um caracter a cada evento
        eventos = new HashMap<String, EventoJogo>();
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }

    /**
     * Método privado GerarEvento, responsável por processar o input do utilizador.
     * @return evento associado à tecla precionada pelo utilizador
     */
    private EventoJogo gerarEvento(){
        System.out.print("\nEvento? ");
        String codigoEvento = scanner.next();
        return eventos.get(codigoEvento);
    }

    /**
     * Método público getter do elemento evento de modo a realizar a sua propriedade read-only
     * @return evento
     */
    public EventoJogo getEvento(){
        return this.evento;
    }

    //métodos a ser implementados de modo a concretrizar o contrato com a interface Ambiente

    //método público evoluir
    /**
     * Evolui o evento atravéz do método gerarEvento.
     */
    public void evoluir(){
        evento = gerarEvento();
    }

    //método público observar, retorna elemento do tipo Evento
    /**
     * Mostra o evento atual se este não for nulo, e retorna-o independentemente do valor
     * @return evento atual
     */
    public Evento observar(){
        if(evento != null) evento.mostrar();
        return evento;
    }

    //método público executar
    /**
     * Executa (mostra o nome do comando no ecrã) o comando
     * @param comando comando a ser executado
     */
    public void executar(Comando comando){
        comando.mostrar();
    }
}
