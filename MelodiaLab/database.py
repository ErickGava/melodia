import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def conectar_banco():
    conexao = sqlite3.connect("bancodedados")
    return conexao


def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Criando a tabela de usuários
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                   (username TEXT, email TEXT PRIMARY KEY, senha TEXT)''')
    
    # Criando a tabela de tarefas
    cursor.execute('''CREATE TABLE IF NOT EXISTS musica
                   (id INTEGER PRIMARY KEY, letra TEXT, nome_compositor TEXT,
                   nome_musica TEXT, status TEXT, imagem TEXT,
                   email_usuario TEXT,
                   FOREIGN KEY(email_usuario) REFERENCES usuarios(email))''')
    
    conexao.commit()
    
def cadastro(formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT COUNT(email) from usuarios WHERE email=?""", (formulario['username'],))
    conexao.commit()
    quantidade_de_emails = cursor.fetchone()
    print(quantidade_de_emails)
    
    if quantidade_de_emails[0] > 0:
        print("E-mail já cadastrado! Tente novamente")
        return False

    senha_criptografada = generate_password_hash(formulario['senha'])

    cursor.execute('''INSERT INTO usuarios(username, email, senha) 
                   VALUES (?, ?, ?)''', (formulario['username'], formulario['email'], senha_criptografada))
    
    conexao.commit()
    return (True)

def login(formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''SELECT COUNT(email) FROM usuarios WHERE email=?''', (formulario['username'],))
    conexao.commit()
    
    quantidade_de_emails = cursor.fetchone()
    print(quantidade_de_emails)
    
    if quantidade_de_emails[0] == 0:
        print("E-mail não cadastrado! Tente novamente")
        return False
    
    cursor.execute('''SELECT senha FROM usuarios WHERE email=?''', (formulario['username'],))
    conexao.commit()
    senha_criptografada = cursor.fetchone()
  
    return check_password_hash(senha_criptografada[0], formulario['password'])

def excluir_usuario(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM usuarios WHERE email = ?''', (email,))
    cursor.execute('''DELETE FROM musica WHERE email_usuario = ?''', (email,))
    conexao.commit()
    return True

def criar_musica(nome_musica, nome_compositor, status, letra, email_usuario, imagem):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    if nome_musica == "1" and nome_compositor == "1" and status == "1" and letra == "1":
        return "Você não poderá realizar esta ação!"
    cursor.execute('''INSERT INTO musica (nome_musica, nome_compositor, status, letra, email_usuario, imagem) VALUES(?,?,?,?,?,?)''', (nome_musica, nome_compositor, status, letra, email_usuario, imagem))
    conexao.commit()
    cursor.close()
    return True
    
def mostrar_musica(usuarios):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT id, nome_musica, nome_compositor, status, letra, email_usuario, imagem FROM musica WHERE email_usuario = ?""",(usuarios,))
    conexao.commit()
    musicas = cursor.fetchall()
    cursor.close()
    return musicas
    
def listar_musicas(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM musica WHERE id = ?''',(id,))
    conexao.commit()
    cursor.close()
    return True

def apagar_musica(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM musica WHERE id = ?''', (id,))
    conexao.commit()
    return True

# PARTE PRINCIPAL DO PROGRAMA
if __name__ == '__main__':
    criar_tabelas()
    print("Hello, world!")