package jogo.ambiente;

import ambiente.Comando;

/**
 * Enumerador público ComandoJogo, implementa a interface Comando uma vez que implementa o método mostrar
 */
public enum ComandoJogo implements Comando {
    //enumeradores da classe
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    //método a ser implementados de modo a concretrizar o contrato com a interface
    /**
     * Imprime o valor toString do enumerador para a consola
     */
    public void mostrar(){
        System.out.printf("\nEvento: %s\n", this);
    }
}
