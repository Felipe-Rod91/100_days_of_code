# Crie um programa que pergunte ao usuário quantos números inteiros ele deseja armazenar em uma lista. Em seguida, peça para o usuário 
# digitar cada número e adicione-o à lista. Por fim, mostre na tela o maior, o menor e a média dos números digitados.

# Criação da lista vazia e quantos números deseja armazenar nela
numbers = list()
quant = int(input('Quantos números deseja armazenar na lista? '))

# Loop para adicionar os números à lista
for n in range(quant):
    num = int(input(f'Digite o {n+1}º número: '))
    numbers.append(num)

# Calcula o maior, menor, soma e a média dos números
maximum = max(numbers)
minimum = min(numbers)
sum = sum(numbers)
average = sum / quant

# Mostra na tela todas as informações
print(f'Maior número: {maximum}')
print(f'Menor número: {minimum}')
print(f'Média: {average}')