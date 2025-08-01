#Nesses exemplos vou usar o arquivo json na pasta "PANDAS - JSON"
import pandas as pd

DataFrame = pd.read_json('python/PANDAS - JSON/data.json')

#método head():
#Retorna os cabeçalhos e um numero especifico de linhas (por padrão 5)

print(DataFrame.head(10)) #numero de linhas como parametro da função

#método tail():
#Mesma coisa, porém inverso, exibindo de baixo para cima

print(DataFrame.tail(10))

#método info():
#como o nome indica, exibe informações sobre os dados

print(DataFrame.info())
