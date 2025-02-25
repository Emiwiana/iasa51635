package jogo.ambiente;

import ambiente.Evento;

/**
 * Enumerador público EventoJogo, implementa a interface Evento uma vez que implementa o método mostrar
 */
public enum EventoJogo implements Evento {
    //enumeradores da classe
    SILENCIO, //S
    RUIDO,  //R
    ANIMAL,  //A
    FUGA, //F
    FOTOGRAFIA, //O
    TERMINAR; //T

    //método a ser implementados de modo a concretrizar o contrato com a interface
    /**
     * Imprime o valor toString do enumerador para a consola
     */
    public void mostrar(){
        System.out.printf("\nEvento: %s\n", this);
    }
}
