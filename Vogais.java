//Contador de vogais em uma String em java

public class Vogais {
    static void contarVogais(String palavra){
        String vogais = "aeiouAEIOU";
        int contadorVogal = 0;
        for (int i = 0; i<palavra.length(); i++){
            if (vogais.contains(String.valueOf(palavra.charAt(i)))){
                contadorVogal++;
                System.out.println("Vogal N° " + contadorVogal + " é: "+ palavra.charAt(i));
            }
        }
    }

    public static void main (String[]args){
        String x = "recebaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        contarVogais(x);
    }
}
