# Importa a classe Flask do pacote flask
# Flask é um microframework para criação de aplicações web em Python
from flask import Flask


# Cria uma instância da aplicação Flask
# __name__ informa ao Flask qual é o módulo principal da aplicação
# Isso ajuda o Flask a localizar arquivos e recursos corretamente
app = Flask(__name__)


# Define uma rota da aplicação
# @app.route('/') é um decorator que diz:
# "Quando alguém acessar a URL raiz '/', execute a função abaixo"
@app.route('/')
def main():
    # Função que será executada quando a rota '/' for acessada
    # O valor retornado aqui será enviado como resposta HTTP
    # Como é uma string simples, o Flask automaticamente:
    # - cria a resposta HTTP
    # - define o status 200 OK
    # - define o Content-Type como text/html
    return 'Hello, World!'


# Inicia o servidor Flask
# debug=True ativa o modo debug, que:
# - reinicia o servidor automaticamente ao salvar o código
# - mostra mensagens de erro detalhadas no navegador
# ⚠️ Esse modo deve ser usado apenas em desenvolvimento
app.run(debug=True)
