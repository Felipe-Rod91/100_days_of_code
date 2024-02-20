# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_pares(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
# valores pares sorteados pela função anterior.

from random import randint

# Função que sorteia 5 números aleatórios entre 0 e 100
def sorteia():
    for valor in range(0, 5):
        numbers.append(randint(0, 100))
    print(f'Os {len(numbers)} valores sorteados foram: {numbers}')

# Função que soma todos os números pares sorteados na função sorteia()
def soma_pares():
    soma = 0
    for valor in numbers:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma de todos os números pares é {soma}.')

# Criação da lista e execução das funções
numbers = list()
sorteia()
soma_pares()