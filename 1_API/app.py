from flask import Flask , jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def people(id):
    return jsonify(
        {'id': id,
        'Name': 'Allyson',
        'Profission': 'Developer'}
    )

# @app.route('/soma/<int:valor_1>/<int:valor_2>/')
# def soma(valor_1,valor_2):
#     return jsonify(
#         {'soma':valor_1 + valor_2}
#     )

@app.route('/soma',methods=['PUT','POST','GET'])
def soma():
    if request.method == 'POST':
        dados = json.load(request.data)
        total = sum(dados['valores'])
    elif request.method =='GET':
        total = 10 + 10
    return jsonify({'soma':total})

if __name__ == '__main__':
    app.run(debug=True)