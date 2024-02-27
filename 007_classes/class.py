class MinhaFamilia:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pai = MinhaFamilia('Otávio', 61)

mae = MinhaFamilia('Bárbara', 63)

irmao = MinhaFamilia('Felipe', 35)

irma = MinhaFamilia('Bruna', 31)

print(f'{pai.nome}, {pai.idade}')
print(f'{mae.nome}, {mae.idade}')
print(f'{irmao.nome}, {irmao.idade}')
print(f'{irma.nome}, {irma.idade}')