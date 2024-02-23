# Vamos criar um menu em Python usando modularização, onde existem as funções de cadastrar pessoas, visualizar
# as pessoas cadastradas e sair do programa.

from time import sleep
from interface import format

# Função para escolher a opção certa e o tratamento de erros
def options(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'{format.red}Valor inválido! Tente novamente.{format.neutral}')
            continue
        except KeyboardInterrupt:
            print(f'{format.red}Valor não encontrado. Digite um valor.{format.neutral}')
        else:
            return num

# Função da opção 1, de visualizar as pessoas cadastradas
def registered_people():
    format.title('PESSOAS CADASTRADAS')
    print(f'{"NOME":<35}{"IDADE"}')
    for person in people:
        print(f'{person['nome']:<35}{person['idade']:^5}')
    sleep(2)

# Função da opção 2, de cadastrar nova pessoa
def register():
    format.title('CADASTRO DE PESSOAS')
    while True:
        try:
            person['nome'] = str(input('Nome: '))
        except (ValueError, TypeError):
            print('Nome inválido! Digite um nome.')
            continue
        else:
            break
    while True:
        try:
            person['idade'] = int(input('Idade: '))
        except (ValueError, TypeError):
            print(f'{format.red}Valor inválido! Digite um número inteiro.{format.neutral}')
            continue
        else:
            break
    people.append(person.copy())  
    print(f'{format.green}Armazenando os dados...', end=' ')
    sleep(2)
    print(f'PRONTO!{format.neutral}')
    sleep(2)

# Programa principal
person = dict()
people = list()
while True:
    format.main_menu()
    option = options(f'Digite um valor: ')
    if option == 1:
        registered_people()
    elif option == 2:
        register()
    elif option == 3:
        break
    else:
        print(f'{format.red}Valor não encontrado. Digite um número válido.{format.neutral}')

# Mensagem de programa encerrado
format.title('PROGRAMA ENCERRADO')
