package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/**
 * Classe pública Personagem que herda a classe agente
 */
public class Personagem extends Agente {
    /**
     * Método construtor público da classe Personagem
     * @param ambiente
     */
    public Personagem(AmbienteJogo ambiente) {
        //a classe ControloPersonagem é criada de modo a preencher o parâmetro controlo da classe parente
        //esta classe é compátivel com o parâmetro Controlo uma vez que implementa a interface Controlo
        super(ambiente, new ControloPersonagem());
    }
}
