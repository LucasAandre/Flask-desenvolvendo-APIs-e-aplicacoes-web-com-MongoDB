# -*- coding: utf-8 -*-
# Define explicitamente que este arquivo usa codificação UTF-8,
# garantindo que caracteres acentuados funcionem corretamente.

from flask import Blueprint, jsonify, request
# Blueprint: permite organizar rotas em módulos
# jsonify: converte dicionários Python em respostas JSON válidas
# request: permite acessar dados da requisição HTTP (body, headers, etc.)

from app.models.user import LoginPayload
# Importa o modelo de dados LoginPayload,
# normalmente um modelo Pydantic que define os campos esperados no login

from pydantic import ValidationError
# Exceção lançada pelo Pydantic quando os dados recebidos não
# correspondem ao modelo definido (campos faltando, tipos errados, etc.)

main_bp = Blueprint('main_bp', __name__)
# Cria um Blueprint chamado 'main_bp'
# Ele será registrado no app principal para agrupar rotas relacionadas

# RF (Requisito Funcional):
# O sistema deve permitir que um usuário se autentique para obter um token
@main_bp.route('/login', methods=['POST'])
# Define uma rota POST no endpoint /login
# Essa rota pertence ao Blueprint main_bp

def login():
    try:
        # Obtém o corpo da requisição HTTP no formato JSON
        # Exemplo esperado:
        # {
        #   "email": "teste@email.com",
        #   "password": "123456"
        # }
        raw_data = request.get_json()

        # Cria uma instância do modelo LoginPayload
        # O operador ** faz o "desempacotamento" do dicionário
        # Cada chave do JSON vira um argumento do modelo
        user_data = LoginPayload(**raw_data)

    except ValidationError as e:
        # Captura erros de validação do Pydantic
        # Exemplo: campo obrigatório ausente, tipo inválido, etc.

        return jsonify({
            'Error': e.errors()
        }), 400
        # Retorna erro 400 (Bad Request), pois o cliente enviou dados inválidos

    except Exception as e:
        # Captura qualquer outro erro inesperado
        # Exemplo: JSON vazio, erro interno, etc.

        return jsonify({
            'Error': 'Erro durante a requisição do dado'
        }), 500
        # Retorna erro 500 (Internal Server Error)
    
    if user_data.username == 'admin' and user_data.password == '123':
        # Se tudo ocorrer bem, retorna uma resposta de sucesso
        # model_dump_json() converte o objeto Pydantic em JSON
        return jsonify({
            'message': f'Realizar o login do usuário {user_data.model_dump_json()}'
        })
    
    else:
        return jsonify({'message': 'Credenciais inválidas'})

# RF: O sistema deve permitir a listagem de todos os produtos
@main_bp.route('/products', methods=['GET'])
def get_products():
    return jsonify({'message': 'Esta é a rota de listagem dos produtos'})

# RF: O sistema deve permitir a criação de um novo produto
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({'message': 'Esta é a rota de criação de produto'})

# RF: O sistema deve permitir a visualização dos detalhes de um único produto
@main_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return jsonify({'message': f'Esta é a rota de visualização dos detalhes de um produto: ID {product_id}'})

# RF: O sistema deve permitir a atualização de um único produto e produto existente
@main_bp.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return jsonify({'message': f'Esta é a rota de atualização do produto: ID {product_id}'})

# RF: O sistema deve permitir a deleção de um único produto e produto existente
@main_bp.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return jsonify({'message': f'Esta é a rota de deleção do produto: ID {product_id}'})

# RF: O sistema deve permitir a importação de vendas através de um arquivo
@main_bp.route('/sales/upload', methods=['POST'])
def upload_sales():
    return jsonify({'message': 'Esta é a rota de upload do arquivo de vendas'})

@main_bp.route('/category', methods='GET')
def get_categories():
    return jsonify({"message": "Retorna a lista de todas as categorias"}) 

@main_bp.route('/category', methods='POST')
def create_categories():
    return jsonify({"message": "Cria uma categoria"})

# @main_bp.route('/')
# def index():
#     return jsonify({'message': 'Bem-vindo ao StyleSync!'})
