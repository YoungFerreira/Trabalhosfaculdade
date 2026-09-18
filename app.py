from flask import render_template, Flask, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', user=user)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template('cadastro.html')


lista = []
@app.route('/Pcadastro', methods=['GET', 'POST'])
def Pcadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        ano = request.form['ano']
        categoria = request.form['categoria']

        lista.append({"nome": nome, "descricao": descricao, "ano": ano, "categoria": categoria})

    return redirect('/viewCadastro')  

@app.route('/viewCadastro')
def viewCadastro():
    return render_template('lista.html', jogos=lista)

if __name__ == '__main__':
    app.run(debug=True)