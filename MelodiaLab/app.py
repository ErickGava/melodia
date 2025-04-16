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
    lista_de_musicas = database.mostrar_musica(session['email'])
    print(lista_de_musicas)
    return render_template('home.html', musicas = lista_de_musicas)


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')

    verificação=database.login(formulario=request.form)
    if not verificação:
        return "Algo deu de errado, tente novamente"
    
    session['email']=request.form['email']
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
        if database.criar_musica(nome_musica = form["nome_musica"], nome_compositor = form["nome_compositor"], status = form["status"], letra = form["letra"], email_usuario = session['username'], imagem = form['imagem']) == True:
            return redirect(url_for('home'))
        else:
            return "Ocorreu um erro ao criar uma musica"
    else:
        return render_template('musica.html')
    
@app.route('/home/excluir-musica/<int:id>', methods=['GET'])
def excluir_musica(id):
    if database.apagar_musica(id):
        return redirect(url_for('home'))
    else:
        return "Algo deu errado!!"
    
@app.route('/home/editar-musica/<int:id>', methods=['POST', 'GET'])
def editar_musica(id):
    if request.method == "POST":
        form = request.form
        if database.editar_musica(id = id, nome_musica = form["nome_musica"], nome_compositor = form["nome_compositor"], status = form["status"], letra = form["letra"], imagem = form['imagem']) == True:
            return redirect(url_for('home'))
        else:
            return "Algo deu errado!!"
    else:
        procurar_musica = database.procurar_musicas(id)
        print(procurar_musica)
        return render_template('editar.html', musica = procurar_musica, id=id)

@app.route('/home/excluir-usuario', methods=['GET'])
def excluir_usuario():
    email = session['username']
    if database.excluir_usuario(email):
        return redirect(url_for('index'))
    else:
        return "Algo deu errado!"

# parte principal do
if __name__ == '__main__':
    app.run(debug=True)