def aumentar(preço=0, taxa=0, formato=False):
    result = preço + (preço * taxa / 100)
    return result if formato is False else moeda(result)


def diminuir(preço=0, desconto=0, formato=False):
    result = preço - (preço * desconto / 100)
    return result if formato is False else moeda(result)


def dobro(preço=0, formato=False):
    result = preço * 2
    return result if formato is False else moeda(result)


def metade(preço=0, formato=False):
    result = preço / 2
    return result if formato is False else moeda(result)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa=0, desconto=0):
    print('~' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('~' * 40)
    print(f'Preço analisado: \t\t{moeda(preço)}')
    print(f'Preço com {taxa}% de aumento: \t{aumentar(preço, taxa, True)}')
    print(f'Preço com {desconto}% de desconto: \t{diminuir(preço, desconto, True)}')
    print(f'Dobro do preço: \t\t{dobro(preço, True)}')
    print(f'Metade do preço: \t\t{metade(preço, True)}')


    