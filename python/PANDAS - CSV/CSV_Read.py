#para esses exercicios vou usar um arquivo csv genérico com dados fictícios
import pandas as pd

dataframe = pd.read_csv('python/PANDAS - CSV/data.csv')

print(dataframe)
#quando há muitos dados, o dataframe vai exibir apenas as primeiras 5 e ultimas 5 colunas
#para mudar isso, a função to_string() pode ser usada.

print(f'\n usando o método to_string(): \n{dataframe.to_string()}')

#o limite de linhas e colunas padrão pode ser exibido usando o seguinte:
print('limite de linhas e colunas: ')
print(pd.options.display.max_rows)
print(pd.options.display.max_columns)

# pd.options.display.max_rows = 'numero desejado'