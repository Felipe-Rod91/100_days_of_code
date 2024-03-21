import api
import os

# Verifica usuário e login pelas variáveis de ambiente
usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')

print(usuario)
print(senha)

# Executa a função login do arquivo usuário.
login = api.login(usuario, senha)

