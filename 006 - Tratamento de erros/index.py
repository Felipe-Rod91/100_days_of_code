# Vamos criar um menu em Python usando modularização, onde existem as funções de cadastrar pessoas, visualizar
# as pessoas cadastradas e sair do programa

from time import sleep

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

# Função para escolher a opção certa e o tratamento de erros
def options(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'{red}Valor inválido! Tente novamente.{neutral}')
            continue
        except KeyboardInterrupt:
            print(f'{red}Valor não encontrado. Digite um valor.{neutral}')
        else:
            return num

# Função da opção 1, de visualizar as pessoas cadastradas
def option_1():
    title('OPÇÃO 1')
    for person in people:
        print(f'{person['nome']}, {person['idade']}')
    #sleep(2)

# Função da opção 2, de cadastrar nova pessoa
def option_2():
    title('OPÇÃO 2')
    sign_up()
    print('Armazenando os dados...', end=' ')
    #sleep(2)
    print('PRONTO!')
    #sleep(2)


def sign_up():
    person['nome'] = str(input('Nome: '))
    while True:
        try:
            person['idade'] = int(input('Idade: '))
        except (ValueError, TypeError):
            print(f'{red}Valor inválido! Digite um número inteiro.{neutral}')
            continue
        else:
            break
    people.append(person.copy())    

# Programa principal
person = dict()
people = list()
while True:
    main_menu()
    option = options(f'{green}Digite um valor: {neutral}')
    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        break
    else:
        print(f'{red}Valor não encontrado. Digite um número válido.{neutral}')

# Mensagem de programa encerrado
title('PROGRAMA ENCERRADO')