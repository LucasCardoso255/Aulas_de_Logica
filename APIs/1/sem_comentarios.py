# literalmente o mesmo arquivo de antes, porém sem os comentários para visualizar melhor:
from http.server import BaseHTTPRequestHandler,HTTPServer
import json

class SimpleAPI(BaseHTTPRequestHandler): 
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            resposta = {"mensagem": "parabens, voce fez um get!"}
            self.wfile.write(json.dumps(resposta).encode())
        
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("localhost", 8000), SimpleAPI)
print("Servidor rodando em http://localhost:8000")
server.serve_forever()