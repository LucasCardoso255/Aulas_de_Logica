# criar APIs usando frameworks, é codar no easy, principalmente com a do exemplo abaixo.

from fastapi import FastAPI

batata = FastAPI() # faz tudo que tivemos que faz na pasta 1, porém em uma linha só.

@batata.get("/") # basicamente é: faça a função abaixo, caso façam um GET na rota '/' 
def inicio():
    return {"mensagem": "esse foi um get usando FastAPI!"}

# após isso, digite no terminal: uvicorn main:batata
# ou uvicorn main:batata --reload caso queira que o servidor reinicie toda vez que salvar o arquivo