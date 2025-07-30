//Somador de todos os pares de uma lista em java
package java;
public class soma{
    static int getSomaPares(int lista[]){
        int lista_temporaria[] = new int[lista.length];
        int indice_lista = 0;
        int resultado = 0;
        for(int i = 0;i<lista.length; i++){
            if (lista[i] % 2 == 0){
                lista_temporaria[indice_lista] = lista[i];
                indice_lista++;
            }
        }
        for(int j = 0; j<lista_temporaria.length; j++){
            resultado += lista_temporaria[j];
        }
        return resultado;
    }
    public static void main (String[]args){
        int lista_original[] = {1,2,3,4,5,6,7,8,9};
        System.out.println("a soma dos pares de 1-9 é: " + getSomaPares(lista_original));
    }
}
