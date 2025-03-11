package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

/**
 * Classe que representa um estado na máquina de estados, cada estado possui um nome e um HashMap com as transições associadas
 * a este evento
 */
public class Estado {
    /**
     * atributo nome do estado, privado de modo a implementar a sua propriedade read-only especificada pelo professor
     */
    private String nome;

    /**
     * método getter público getNome
     * @return nome do estado
     */
    public String getNome(){
        return this.nome;
    }

    private Map<Evento, Transicao> transicoes;

    /**
     * Cria um estado novo através do construtor, iniciando um Map que contem as transições associadas a esse estado
     * @param nome nome do estado
     */
    public Estado(String nome){
        this.nome = nome;
        //iniciar mapa com as transicoes
        transicoes = new HashMap<Evento, Transicao>();
    }

    /**
     * retorna a transição associada ao evento dado
     * @param evento evento a usar como chave
     * @return transição associada ao evento dado
     */
    public Transicao processar(Evento evento){
        return transicoes.get(evento);
    }

    /**
     * adiciona uma transição a um estado, sem accao
     * @param evento evento que leva à transição
     * @param estadoSucessor estado que sucede este estado
     * @return a própria instância Estado de modo a poder ser chamada repetidamente
     */
    public Estado transicao(Evento evento, Estado estadoSucessor){
        transicoes.put(evento, new Transicao(estadoSucessor, null));
        return this;
    }

    /**
     * adiciona uma transição a um estado, com accao
     * @param evento evento que leva à transição
     * @param estadoSucessor estado que sucede este estado
     * @param accao accao resultante da transição
     * @return a própria instância Estado de modo a poder ser chamada repetidamente
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao){
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }
}
