package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/**
 * Classe pública Jogo onde está localizado o método main
 */
public class Jogo {
    //os atributos ambiente e personagem são estáticos, embora esteja omitido no diagrama de modo a poderem
    //ser utilizados no método estático executar
    /**
     * Atributo privado estático ambiente do tipo Ambiente.
     * A ser inicializado fora do construtor de modo a implementar a associação por agregação
     */
    private static AmbienteJogo ambiente;
    /**
     * Atributo privado estático personagem do tipo Personagem.
     * A ser inicializado fora do construtor de modo a implementar a associação por agregação
     */
    private static Personagem personagem;

    /**
     * Método estático main, por onde será executado o programa
     */
    public static void main(String[] args) {
        //atributos ambiente e personagem inicializados no método main como de acordo com o diagrama
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);

        executar();
    }

    //este método é estático de modo a poder ser executado no método main
    /**
     * Método estático privado executar.
     * Contém um ciclo do-while no qual o método evoluir do atributo ambiente e o método executar do atributo personagem são executados.
     */
    private static void executar(){
        //conceptualmente o ciclo do-while faz mais sentido do que o ciclo while para concretizar o operador loop
        //porque o evento só deve ser testado depois de este existir (depois do método evoluir ser chamado)
        do{
            ambiente.evoluir();
            personagem.executar();
        } while(ambiente.getEvento() != EventoJogo.TERMINAR);
    }
}
