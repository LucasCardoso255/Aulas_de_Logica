import pandas as pd

#dataframes:
#Se as series são como colunas, dataframes são como linhas e colunas, com duas dimensões.

pessoas = {
    "nome": ["toji","gojo","yuuji"],
    "sobrenome": ["fushiguro", "satoru", "itadori"]
}

dataframe1 = pd.DataFrame(pessoas)

print(dataframe1)

#localizando dados: o comando "loc[x]" retorna uma linha com o indice desejado

print(f"\no feiticeiro mais forte é: \n{dataframe1.loc[1]}") #retorna uma series como resultado

#loc duplo: 
print(f"\nos feiticeiros com energia são: \n{dataframe1.loc[[1,2]]}") #retorna um dataframe

#o loc pode ser usado em indices também, para localizar os dados direto pelo nome do indice
#dataframes pode ter o nome do indice alterado da mesma forma que as series.
