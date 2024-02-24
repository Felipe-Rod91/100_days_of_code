# Vamos criar um menu em Python usando modularização, onde existem as funções de cadastrar pessoas, visualizar
# as pessoas cadastradas e sair do programa.

from time import sleep
from lib.interface.functions import *
from lib.file.create_file import *

# Cria o arquivo de texto das pessoas registradas, caso não exista
file = 'registered_people.txt'
if not file_exists(file):
    create_file(file)

# Programa principal
people = list()
while True:
    option = main_menu('Digite a opção desejada: ')
    if option == 1:
        read_file(file)
    elif option == 2:
        name = str(input('Nome: '))
        age = int_number('Idade: ')
        register(file, name, age)
    elif option == 3:
        title('PROGRAMA ENCERRADO')
        break
    else:
        print(f'{red}Valor não encontrado. Digite um número válido.{neutral}')
