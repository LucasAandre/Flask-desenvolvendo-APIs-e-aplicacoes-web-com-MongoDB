# Importa a função make_server do módulo wsgiref.simple_server
# Esse módulo faz parte da biblioteca padrão do Python
# Ele permite criar um servidor web simples usando o padrão WSGI
from wsgiref.simple_server import make_server


# Define a função principal da aplicação WSGI
# Toda aplicação WSGI OBRIGATORIAMENTE recebe dois parâmetros:
# 1) environ -> um dicionário com informações da requisição HTTP
# 2) start_response -> uma função usada para iniciar a resposta HTTP
def aplicacao(environ, start_response):
    
    # Lista de produtos simulando dados que poderiam vir de:
    # - um banco de dados
    # - uma API
    # - um arquivo
    # Aqui estamos usando uma lista fixa apenas para exemplo
    produtos = [
        {'nome': 'Notebook', 'valor': 3500.89},
        {'nome': 'Celular', 'valor': 1200.00},
        {'nome': 'Cadeira', 'valor': 259.99},
        {'nome': 'T-shirt', 'valor': 179.59}
    ]

    linhas_html = ''
    
    for produto in produtos:
        linhas_html += f'<li>{produto['nome']} - R${produto['valor']}</li>'


    # start_response define o status da resposta HTTP e os headers
    # '200 Ok' significa que a requisição foi bem-sucedida
    # Content-type informa ao navegador que o conteúdo é HTML
    # charset=utf-8 garante suporte a acentos e caracteres especiais
    start_response('200 Ok', [('Content-type', 'text/html;charset=utf-8')])

    # Ao deixar o servidor aberto e entrar no caminho http://localhost:5000/ pelo navegador,
    # aparece na tela o que está no arquivo index.html
    with open('index.html', 'r', encoding='utf-8') as file:
        html = file.read()
    
    html_final = html.replace('{{PRODUTOS}}', linhas_html)

    # A função WSGI deve retornar um ITERÁVEL (lista, por exemplo)
    # Cada item desse iterável deve ser um objeto bytes
    # Aqui retornamos uma lista contendo o HTML
    return [html_final.encode('utf-8')]


# Cria um servidor HTTP simples
# Parâmetros:
# ''       -> significa que o servidor vai escutar em todas as interfaces
# 5000     -> porta onde o servidor vai rodar
# aplicacao -> função WSGI que será chamada a cada requisição
# serve_forever() mantém o servidor rodando indefinidamente
make_server('', 5000, aplicacao).serve_forever()
