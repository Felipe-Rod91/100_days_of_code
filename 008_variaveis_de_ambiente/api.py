# Função que verifica usuário e senha. Se forem corretos, ocorre login.
# Caso contrário, não ocorre login.
def login(usuario, senha):
    if usuario == 'felipe.rod' and senha == 'pastel':
        print('Usuário e senha CORRETOS, você está logado.')
    else:
        print('Usuário e/ou senha INCORRETOS, você NÃO está logado.')
