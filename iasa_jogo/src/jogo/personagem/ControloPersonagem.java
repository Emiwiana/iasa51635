package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;

/**
 * Classe pública ControloPersonagem que implementa a Interface Controlo
 */
public class ControloPersonagem implements Controlo {
    /**
     * Método público construtor da classe ControloPersonagem
     */
    public ControloPersonagem(){}

    /**
     * Método privado mostrar
     */
    private void mostrar(){}

    //método a ser implementados de modo a concretrizar o contrato com a interface Controlo
    public Accao processar(Percepcao percepcao){}
}
