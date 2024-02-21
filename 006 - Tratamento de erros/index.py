# Crie uma função leia_int() que pede para digitar um número inteiro, e caso outro valor fora disso for digitado, ele insere uma
# mensagem de erro e pergunte novamente, até o valor estar dentro do parâmetro. Faça o mesmo com uma função leia_float()

# Função que lê uma entrada e só passa se for um número inteiro. Se for valor vazio, retorna zero
def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f'VALOR INVÁLIDO! Foi encontrado um erro.')
            continue
        except KeyboardInterrupt:
            print('Valor não definido. Retornando um valor 0.')
            return 0
        else:
            return valor
        
# Função que lê uma entrada e só passa se for um número flutuante, com ponto ou vírgula. Se for valor vazio, retorna zero
def leia_float(msg):
    while True:
        try:
            valor = float(input(msg).replace(',','.'))
        except (ValueError, TypeError):
            print(f'VALOR INVÁLIDO! Foi encontrado um erro.')
            continue
        except KeyboardInterrupt:
            print('Valor não definido. Retornando um valor 0.')
            return 0
        else:
            return valor

# Entrada dos dados e mensagem final
int_number = leia_int('Digite um número inteiro: ')
float_number = leia_float('Digite um número flutuante: ')
print(f'O número inteiro é o {int_number} e o número flutuante é o {float_number}.')
