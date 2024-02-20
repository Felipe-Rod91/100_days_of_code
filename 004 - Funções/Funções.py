# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_pares(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
# valores pares sorteados pela função anterior.

from random import randint

# Função que sorteia 5 números aleatórios de 0 a 100
def sorteia():
    for v in range(0, 5):
        numeros.append(randint(0, 100))
    print(f'Sorteando os {len(numeros)} da lista: {numeros}.')

# Função que identifica todos os números pares dentro da lista de números sorteados e soma todos eles
def soma_pares():
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += n
    print(f'Somando os valores pares dessa lista, temos {total}.')

# Chamada e resultado das funções
numeros = list()
sorteia()
print()
soma_pares()
