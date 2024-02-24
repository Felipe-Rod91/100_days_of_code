# Cores
white = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
neutral = '\033[m'

# Função que define a estética dos títulos de cada função
def title(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)

# Opção para receber um número inteiro
def int_number(msg):
    while True:
        try:
            option = int(input(msg))
        except(ValueError, TypeError):
            print(f'{red}Valor inválido! Digite um número inteiro.{neutral}')
            continue
        except KeyboardInterrupt:
            print(f'{red}Valor não encontrado. Digite um número inteiro.{neutral}')
        else:
            return option

# Função de menu principal, com o título da função Title()
def main_menu(msg):
    title('MENU PRINCIPAL')
    options = ('Pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa')
    for i, option in enumerate(options):
        print(f'{yellow}{i+1}-{neutral} {blue}{option}{neutral}')
    print('-' * 40)
    choose = int_number(msg)
    return choose

