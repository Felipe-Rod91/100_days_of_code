# Vamos criar um menu em Python usando modularização, onde existem as funções de cadastrar pessoas, visualizar
# as pessoas cadastradas e sair do programa

from time import sleep

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

# Função para escolher a opção certa e o tratamento de erros
def options(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Valor inválido! Tente novamente.')
            continue
        else:
            return num

# Função da opção 1, de visualizar as pessoas cadastradas
def option_1():
    title('OPÇÃO 1')
    sleep(3)

# Função da opção 2, de cadastrar nova pessoa
def option_2():
    title('OPÇÃO 2')
    sleep(3)

# Programa principal
while True:
    main_menu()
    option = options('Digite um valor: ')
    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        break
    else:
        print('Valor não encontrado. Digite um número válido.')

# Mensagem de programa encerrado
title('PROGRAMA ENCERRADO')

