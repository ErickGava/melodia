MelodiaLab 🎶
Plataforma de organização e criação musical, voltada para artistas e músicos que desejam criar, gerenciar e personalizar seus projetos musicais.
Logo

Tecnologias Utilizadas
Backend: Python com Flask
Frontend: HTML, CSS e JavaScript
Banco de Dados: SQLite3 com Python
✅ Casos de Uso
Criar Conta

Formulário: Nome, E-mail, Senha.
Cadastro na tabela de usuários.
Fazer Login

Verificação de e-mail e senha.
Se válido, manter login com sessão (session do Flask).
Excluir Conta

Remover usuário da tabela.
Remover todos os projetos musicais ligados a esse usuário.
Criar Projetos Musicais

Formulário: Nome da música, artista, status (ex: composição, gravação, finalizada), letra.
Opcional: Upload de uma capa de imagem.
Ver Projetos Musicais

Exibir em cards com capa, nome da música, artista, status e trecho da letra.
Excluir Projeto Musical

Botão de deletar projeto associado ao usuário.
Adicionar Capa ao Projeto Musical

Upload de imagem (.jpg, .png) e associação ao projeto.
Editar Projeto Musical

Alterar informações: nome da música, artista, status, letra, capa.
🗃 Diagrama Banco de Dados
Tabelas:

usuarios

email (primary key)
nome
senha
projetos_musicais

id (primary key)
nome_musica
artista
status
letra
caminho_capa (para o arquivo de imagem)
email_usuario (foreign key ligando ao usuário)
Diagrama de classes
Diagrama de Classes

Como instalar o sistema
Requisitos
Computador
Internet
Visual Studio Code
Python
Biblioteca flask para Python
Extensão Python do VS Code
Git
Clonar repositório do Github
Abra o Visual Studio Code e clique no botão "Controle de código de fonte"

Clique em "Clonar repositório", "Clonar de Github" e Clique em "Permitir" na janela que vai aparecer.

Faça o login, autorize o Visual Code e depois "Abrir Link" para abrir novamente o programa.

Escolha o repositório do projeto para clonar

Deseja abrir o repositório clonado? Abrir

Instalar a extensão do Python
Clique em "Extensões" no menu a esquerda ou CTRL+SHIFT+X
Procure por "Python"
Clique em "Instalar"
Instalar a biblioteca Flask
Abrir um novo terminal: Barra de ferramentas > Três pontinhos > Terminal > Novo Terminal

No terminal, digite o comando pip install flask e pressione enter

Configurando GIT
No terminal digite os comandos:
git config user.name seu_usuario

git config user.email seu_nome@email.com

Como executar o servidor
Clique com o botão direito no arquivo "app.py" e selecione "Executar o arquivo Python no terminal"