import pandas as pd

#simplificando bastante, series são como colunas de dados em uma table.

a = [1,2,3,4,5]

print(f"lista comum:{a}")

b = pd.Series(a)

print(f"serie com pandas: \n{b}")

#Labels: usando o argumento index, posso mudar o nome dos indices

c = pd.Series(a, index=["primeiro","segundo","terceiro","quarto","quinto"])

print(f"exemplo de label proprio: \n{c}")

#acessar pelo indice que criei
print(f"o terceiro valor é: {c["terceiro"]}")

#usando objetos ao criar uma serie:
computadores = {"velho": "ruim", "novo": "bom"} #pode usar o nome do objeto como indice para acessar a lista
listar_computadores = pd.Series(computadores)
print(listar_computadores)

#DataFrame usando series:
lista_para_dataframe = {
    "pessoa": ["joão", "maria", "pinóquio"],
    "idade": [15, 15, 16]
}
TOD = pd.DataFrame(lista_para_dataframe)
print(TOD)