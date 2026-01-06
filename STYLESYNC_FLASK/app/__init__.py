# Importa a classe Flask, usada para criar a aplicação web
from flask import Flask

# Importa o cliente do MongoDB para conexão com o banco de dados
from pymongo import MongoClient

# Variável global para armazenar a referência do banco de dados
db = None

# Função factory responsável por criar e configurar a aplicação Flask
def create_app():
    # Cria a instância da aplicação Flask
    app = Flask(__name__)

    # Carrega as configurações da aplicação a partir da classe Config
    app.config.from_object('config.Config')

    # Indica que a variável db usada aqui é a variável global
    global db

    try:
        # Cria o cliente MongoDB usando a URI definida nas configurações
        client = MongoClient(app.config['MONGO_URI'])

        # Obtém o banco de dados padrão definido na URI
        db = client.get_default_database()
    
    except Exception as e:
        # Captura e exibe qualquer erro ocorrido durante a conexão com o banco
        print(f'Erro ao realizar a conexão com o banco de dados: {e}')
    
    # Importa o blueprint principal da aplicação (rotas)
    from .routes.main import main_bp

    # Registra o blueprint principal na aplicação
    app.register_blueprint(main_bp)
        
    # Retorna a aplicação Flask configurada
    return app

