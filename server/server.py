from http.server import BaseHTTPRequestHandler, HTTPServer
import json

#Incrementa o Num de Premios
def editar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = int(arquivo.read())
    except FileNotFoundError:
        conteudo = 0
    
    incrementa = str(conteudo + 1)
    
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(incrementa)


# Le e retorna o Json
def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            return {"Premios": conteudo}
    except FileNotFoundError:
        return {"erro": "Arquivo não encontrado"}

# Trata as requisições
class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        path = self.path

        if path == "/editar/premio1":
            editar_arquivo("arquivos/premio1.txt")
            self.wfile.write(json.dumps({"mensagem": "premio1 editado"}).encode())
        elif path == "/editar/premio2":
            editar_arquivo("arquivos/premio2.txt")
            self.wfile.write(json.dumps({"mensagem": "premio2 editado"}).encode())
        elif path == "/editar/premio3":
            editar_arquivo("arquivos/premio3.txt")
            self.wfile.write(json.dumps({"mensagem": "premio3 editado"}).encode())
        elif path == "/ler/premio1":
            response = ler_arquivo_json("arquivos/premio1.txt")
            self.wfile.write(json.dumps(response).encode())
        elif path == "/ler/premio2":
            response = ler_arquivo_json("arquivos/premio2.txt")
            self.wfile.write(json.dumps(response).encode())
        elif path == "/ler/premio3":
            response = ler_arquivo_json("arquivos/premio3.txt")
            self.wfile.write(json.dumps(response).encode())
        else:
            self.wfile.write(json.dumps({"erro": "Rota inválida"}).encode())

host = "localhost"
port = 8000

# cria o servidor HTTP
server = HTTPServer((host, port), CustomRequestHandler)

print(f"Servidor rodando em http://{host}:{port}")
server.serve_forever()
