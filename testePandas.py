import pandas as pd

conjunto = {
    'carros:':["carro1", "carro2", "carro3"],
    'motos:':["moto1","moto2","moto3"]
}

x = pd.DataFrame(conjunto)
print(x)