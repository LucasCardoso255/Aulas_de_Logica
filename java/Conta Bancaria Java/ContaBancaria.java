class ContaBancaria {
    private String titular;
    private double saldo;


public void depositar(double valor){
    if (saldo + valor < 0) {
        System.out.println("tentando depositar um saldo negativo né espertinho? \npode não!");
    }
    else{
    saldo += valor;
    }
}

public void sacar(double valor){
    if (valor <= saldo){
        saldo -= valor;
    }
    else{
        System.out.println("Valor insuficiente");
    }

}

public String getTitular() {
    return titular;
}

public double getSaldo() {
    return saldo;
}

}