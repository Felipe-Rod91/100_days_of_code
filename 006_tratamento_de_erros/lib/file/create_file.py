from ..interface.functions import *

# função que abre o arquivo de texto de pessoas cadastradas, caso ele exista
def file_exists(name):
    try:
        file = open(name, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
# Função que cria o arquivo de texto de pessoas cadastradas, caso ele não exista
def create_file(name):
    try:
        file = open(name, 'wt+')
    except:
        print(f'Houve um erro ao criar o arquivo "{name}".')
    else:
        print(f'Arquivo "{green}{name}{neutral}" criado com sucesso.')

# Função que lê o arquivo de texto de pessoas cadastradas com a formatação correta
def read_file(name):
    try:
        file = open(name, 'rt')
    except:
        print(f'Erro ao ler o arquivo "{name}".')
    else:
        title('PESSOAS CADASTRADAS')
        print(f'{"NOME":<35}{"IDADE"}')
        for line in file:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]}{'.' * (35 - len(data[0]))}{data[1]:^5}')
    finally:
        file.close()

# Função que cadastra as pessoas na lista
def register(file, name, age):
    try:
        file = open(file, 'at')
    except:
        print(f'Houve um erro ao abrir o arquivo {file}.')
    else:
        try:
            file.write(f'{name};{age}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo cadastro de {green}{name}{neutral} realizado com sucesso.')

