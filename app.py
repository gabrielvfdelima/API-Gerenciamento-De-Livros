from flask import Flask, jsonify, request

app = Flask(__name__)

livros = {
    1: {
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien',
    },
    2: {
        'titulo': 'Cristianismo Puro e Simples',
        'autor': 'C.S. Lewis',
    },
    3: {
        'titulo': 'A Esperança do Evangelho',
        'autor': 'Chesterton',
    },
}

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def pesquisa_id(id):
    return jsonify(livros.get(id))

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    livros[id].update(livro_alterado)
    return jsonify(livros.get(id))

@app.route('/livros', methods=['POST'])
def inluir_novo_livro():
    id = len(livros)
    novo_livro = request.get_json()
    livros[id+1] = novo_livro
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=["DELETE"])
def deletar_livro(id):
    livros.pop(id)
    return jsonify(livros)
app.run(port=5000, host="localhost", debug=True)

