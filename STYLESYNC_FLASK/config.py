# Importa o módulo os para acessar variáveis de ambiente do sistema
import os

# Importa a função load_dotenv para carregar variáveis do arquivo .env
from dotenv import load_dotenv

# Carrega as variáveis de ambiente definidas no arquivo .env para o sistema
load_dotenv()

# Classe responsável por centralizar as configurações da aplicação
class Config:
    # Define a URI de conexão com o MongoDB a partir da variável de ambiente MONGO_URI
    MONGO_URI = os.getenv('MONGO_URI')
