#não muda quase nada de uma leitura json para uma leitura csv
#dito isso, não explicar tudo que está sendo feito, pois é mais do mesmo.

import pandas as pd

dataframe = pd.read_json('python/PANDAS - JSON/data.json')

print(f'dataframe json sem usar o método to_string(): \n{dataframe}')

print(f'\ndataframe json usando o método to_string(): \n{dataframe.to_string()}')