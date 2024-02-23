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

# Função de menu principal, com o título da função Title()
def main_menu():
    title('MENU PRINCIPAL')
    print(f'{yellow}1-{neutral} {blue}Visualizar pessoas cadastradas{neutral}')
    print(f'{yellow}2-{neutral} {blue}Cadastrar nova pessoa{neutral}')
    print(f'{yellow}3-{neutral} {blue}Sair do programa{neutral}')
    print('-' * 40)

