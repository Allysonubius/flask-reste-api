import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {
        'nome':'Allyson',
        'habilidade':['HTML','Flask']
     },
    {
        'nome':'Rafael',
        'Habildades':['CSS','Bootstrap']
    }
]

@app.route('/dev/<int:id>/', methods=['GET','PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedor[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluido !'})

if __name__ == '__main__':
    app.run(debug=True)