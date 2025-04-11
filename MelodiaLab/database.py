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
                   (email TEXT PRIMARY KEY, nome TEXT, senha TEXT)''')
    
    # Criando a tabela de tarefas
    cursor.execute('''CREATE TABLE IF NOT EXISTS musica
                   (id INTEGER PRIMARY KEY, conteudo TEXT, email TEXT,
                   FOREIGN KEY(email) REFERENCES usuarios(email))''')
    
    conexao.commit()
    
def cadastro(formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT COUNT(email) from usuarios WHERE email=?""", (formulario['email'],))
    conexao.commit()
    quantidade_de_emails = cursor.fetchone()
    print(quantidade_de_emails)
    
    if quantidade_de_emails[0] > 0:
        print("E-mail já cadastrado! Tente novamente")
        return False

    senha_criptografada = generate_password_hash(formulario['senha'])

    cursor.execute('''INSERT INTO usuarios(email, nome, senha) 
                   VALUES (?, ?, ?)''', (formulario['email'], formulario['usuario'], senha_criptografada))
    
    conexao.commit()
    return (True)

def login(formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''SELECT COUNT(email) FROM usuarios WHERE email=?''', (formulario['email'],))
    conexao.commit()
    
    quantidade_de_emails = cursor.fetchone()
    print(quantidade_de_emails)
    
    if quantidade_de_emails[0] == 0:
        print("E-mail não cadastrado! Tente novamente")
        return False
    
    cursor.execute('''SELECT senha FROM usuarios WHERE email=?''', (formulario['email'],))
    conexao.commit()
    senha_criptografada = cursor.fetchone()
  
    return check_password_hash(senha_criptografada[0], formulario['senha'])

# PARTE PRINCIPAL DO PROGRAMA
if __name__ == '__main__':
    criar_tabelas()
    print("Hello, world!")