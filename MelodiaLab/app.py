from flask import Flask, render_template, request, url_for, redirect, flash, session
import database
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "chave_muito_segura"

# Cria um dicionário e usuários e senha, SERÁ MIGRADO PARA O BANCO DE DADOS
usuarios = {
    'usuario' : 'senha',
    'admin' : 'admin'
}

@app.route('/') #rota para a página inicial
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')

    verificação=database.login(formulario=request.form)
    if not verificação:
        return "Algo deu de errado, tente novamente"
    
    session['username']=request.form['username']
    return redirect(url_for('home'))


@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == "POST":
        form = request.form
        if database.cadastro(form) == True:
            return render_template('login.html')
        else:
            return "Ocorreu um erro ao cadastrar usuário"  # Caso contrário, exibe mensagem de erro
    else:
        return render_template('cadastro.html')
    
@app.route('/criar-musicas', methods=['POST', 'GET'])
def criar_musicas():
    if request.method == "POST":
        form = request.form
        if database.cadastro(form) == True:
            return render_template('home.html')
        else:
            return "Ocorreu um erro ao criar uma musica"
    else:
        return render_template('musica.html')

# parte principal do
if __name__ == '__main__':
    app.run(debug=True)