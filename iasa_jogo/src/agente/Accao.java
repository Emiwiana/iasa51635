package agente;

import ambiente.Comando;

/**
 * Classe pública Accao
 */
public class Accao {
    /**
     * Atributo read-only comando, privado de modo a implementar a propriedade read-only em conjunto com o método getter
     */
    private Comando comando;

    /**
     * //Construtor público da classe Accao
     * @param comando
     */
    public Accao(Comando comando){}


    /**
     * Método público getter de modo a realizar a propriedade read-only do atributo comando, de modo a que este não possa ser alterado por outra Classe mas possa ser acedido
     * @return Atributo  read-only comando
     */
    public Comando getComando(){}
}
