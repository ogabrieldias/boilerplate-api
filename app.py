from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
    }, 
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling',
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos',
    },
]

# Consultar todos os livros
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros) # Retorna todos os livros cadastrados na API em formato JSON

# Consultar livros por ID
@app.route('/livros/<int:id>', methods =['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id: # Verifica se o id passado na URL é igual ao id do livro
            return jsonify(livro) 

# Editar livros
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json() # Obter informação que foi enviada do usuário para a API
    for indice, livro in enumerate(livros):
        if livro.get('id') == id: # Verifica se o ID atual é o ID solicitado para alteração
            livros[indice].update(livro_alterado) # Atualiza o livro com as novas informações enviadas pelo usuário
            return jsonify(livros[indice]) # Retorna o livro atualizado em formato JSON

# Criar livros
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json() # Obter informação que foi enviada do usuário para a API
    livros.append(novo_livro) # Adiciona o novo livro à lista de livros
    return jsonify(livros) # Retorna a lista de livros atualizada em formato JSON

# Excluir livros
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros): # Passar sobre todos os livros existentes e excluir de acordo com ID e índice
        if livro.get('id') == id: # Verifica se o ID atual é o ID solicitado para exclusão
            del livros[indice] # Exclui o livro da lista de livros
    return jsonify(livros) # Retorna a lista de livros atualizada em formato JSON

app.run(port=5000, host='localhost', debug=True)
