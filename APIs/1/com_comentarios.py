# nesse arquivo, vamos fazer uma requisição GET manualmente.
# passos para entender como funcionam APIs:

from http.server import BaseHTTPRequestHandler,HTTPServer #imports para criar um servidor
import json

# abaixo, estamos criando uma classe e herdando o baseHTTPRequestHandler.
# a ideia é que essa classe vai lidar com as requisições.
# por isso vamos usá-la, porém a herança será para adicionar o método get manualmente.
class SimpleAPI(BaseHTTPRequestHandler): 
    def do_GET(self):
        if self.path == "/": # enquanto não houver rotas, vamos usar a padrão
            self.send_response(200) # o famoso código "ok"
            self.send_header("Content-type", "application/json") #informando que a resposta é JSON
            self.end_headers()
            # após o fim dos headers, vem o body. abaixo é o corpo da mensagem com valor e chave 
            resposta = {"mensagem": "parabens, voce fez um get!"}
            self.wfile.write(json.dumps(resposta).encode())
        
        else: # caso seja uma rota inexistente
            self.send_response(404) # o famoso código "não encontrado"
            self.end_headers()

server = HTTPServer(("localhost", 8000), SimpleAPI) # definindo a porta e criando servidor
print("Servidor rodando em http://localhost:8000") # só para fins informativos
server.serve_forever() # função para rodar infinitamente



