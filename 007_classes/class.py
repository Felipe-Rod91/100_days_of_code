class MinhaFamilia:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

    def educacao(self):
        if self.idade <= 14:
            print(f'{self.nome} tem {self.idade} anos e está no ensino fundamental.')
        elif 14 < self.idade <= 17:
            print(f'{self.nome} tem {self.idade} anos e está no ensino médio.')
        else:
            print(f'{self.nome} tem {self.idade} anos e já pode ir para a faculdade.')


pai = MinhaFamilia('Adilson', 44)
MinhaFamilia.educacao(pai)

mae = MinhaFamilia('Sonia', 40)
MinhaFamilia.educacao(mae)

filho = MinhaFamilia('Rafael', 16)
filho.educacao()

filha = MinhaFamilia('Gabriela', 12)
filha.educacao()
