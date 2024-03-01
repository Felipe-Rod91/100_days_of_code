class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @classmethod
    def carro_esportivo(cls, marca, modelo):
        return cls(marca, modelo + ' Esportivo')


meu_carro = Carro('Toyota', 'Corolla')
print('Meu carro:', meu_carro.marca, meu_carro.modelo)

carro_esportivo = Carro.carro_esportivo('Ferrari', 'Enzo')
print('Carro esportivo:', carro_esportivo.marca, carro_esportivo.modelo)