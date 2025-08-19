import pandas as pd

DataFrame = pd.read_csv('python/PANDAS - CleanData/data.csv')

DataFrame_usando_Dropna = DataFrame.dropna() #criando um novo dataframe, removendo os dados nulos

#O método dropna() remove todas as linhas que possuam algum campo nulo
#além disso, o método dropna() não altera o dataframe original, apenas cria um novo

print(f'esse é um dataframe deletando linhas com valores nulos \n{DataFrame_usando_Dropna.to_string}')

#usando o argumento "dropna(inplace = True)" o dataframe original será alterado


#fillna(): caso queira preencher os campos nulos com algum dado, use esse método.

DataFrame.fillna('ESSE CAMPO ESTAVA NULO', inplace = True)

print(f'\nesse é um DataFrame usando o método fill: \n{DataFrame.to_string}\n')

#pode ser especificado a coluna de preenchimento, também.
# "DataFrame.fillna({'nome': 'ESTE CAMPO ESTAVA NULO'}, inplace=True)"
#nesse caso, apenas a coluna nome será preenchida






