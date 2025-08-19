import pandas as pd

DataFrame = pd.read_csv('python/PANDAS - CleanData/data.csv')

#outras formas de limpeza de dados incluem os métodos "mean()", "median()" e mode()

#mean(): É a soma de todos os valores, dividido pelo numero de valores.
#É literalmente a média.

x = DataFrame['idade'].mean()

DataFrame.fillna({'idade': x}, inplace=True)

print(f'esse é um dataframe com a idade preenchida usando "mean()" - média:\n{DataFrame}')

#median(): É o valor do meio, calculado após a soma de todos os valores.
#Literalmente o valor do meio.

y = DataFrame['id'].median()

DataFrame.fillna({'id': y}, inplace=True)

print(f'\nesse é um dataframe com o id preenchido usando "median()" - valor do meio:\n{DataFrame}')

#mode(): É o valor com maior frequencia de ocorrencias.
#Literalmente o valor que mais aparece.

z = DataFrame['salario'].mode()

DataFrame.fillna({'salario': z}, inplace=True)

print(f'\nesse é um dataframe cujo o salario foi preenchido usando mode() - o valor que mais aparece: \n{DataFrame}')

