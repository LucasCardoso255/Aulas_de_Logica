import java.util.Scanner;

public class Main{
    public static void main (String[]args){
        ContaBancaria conta1 = new ContaBancaria();
        Scanner ler = new Scanner(System.in);
    
        int loop = 1;
        while (loop == 1) {

        System.out.println("\nBem vindo a sua conta bancária \ndigite 1 para sacar \n2 para depositar \n3 para ver o saldo \n0 para sair");
        int x = ler.nextInt();

        switch (x) {
            case 1:
                System.out.println("Qual valor deseja sacar?");
                double y = ler.nextDouble();
                conta1.sacar(y);
                System.out.println("Seu saldo agora é: " + conta1.getSaldo());
                break;
            case 2:
                System.out.println("Qual valor deseja depositar?");
                double z = ler.nextDouble();
                conta1.depositar(z);
                System.out.println("Seu saldo agora é: " + conta1.getSaldo());
                break;
            case 3:
                System.out.println("Seu saldo é: " + conta1.getSaldo());    
                break;
            case 0:
                loop = 0;
            default:
                System.out.println("Opção inválida!");
                break;
        }
    }
        ler.close();
    }
}