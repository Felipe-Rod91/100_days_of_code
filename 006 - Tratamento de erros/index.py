# Vamos criar um menu em Python usando modularização.

# Função que define a estética dos títulos de cada função
def title(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)

# Função de menu principal, com o título da função Title()
def main_menu():
    title('MENU PRINCIPAL')
    print('1- Visualizar pessoas cadastradas')
    print('2- Cadastrar nova pessoa')
    print('3- Sair do programa')
    print('-' * 40)


def option_1():
    title('OPÇÃO 1')


def option_2():
    title('OPÇÃO 2')

# Programa principal
while True:
    main_menu()
    option = int(input('Digite a opção desejada: '))
    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        break

title('PROGRAMA ENCERRADO')

