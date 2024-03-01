# Escreva uma classe chamada Retângulo que representa um retângulo e inclui métodos para calcular sua área e perímetro. 
# A classe deve ter dois atributos para representar o comprimento e a largura do retângulo. Certifique-se de incluir métodos 
# para configurar o comprimento e a largura do retângulo.

# Depois de criar a classe Retângulo, crie alguns objetos dessa classe e calcule suas áreas e perímetros. Experimente com diferentes 
# tamanhos de retângulos e veja como os métodos funcionam.

class Retangulo:
    def __init__(self, nome, comprimento=1, largura=1):
        self.nome = nome
        self.comprimento = comprimento
        self.largura = largura
    
# Método que calcula a área e retorna a formatação
    def calcular_area(self):
        area = self.comprimento * self.largura
        return f'A área do {self.nome} é {area}m².'
    
# Método que calcula o perímetro e retorna a formatação
    def calcular_perimetro(self):
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return f'O perímetro do {self.nome} é {perimetro}m.'


retangulo_1 = Retangulo('retângulo 1', 35, 39)
print(retangulo_1.calcular_area())
print(retangulo_1.calcular_perimetro())
print()
retangulo_2 = Retangulo('retângulo 2', 12, 24)
print(retangulo_2.calcular_area())
print(retangulo_2.calcular_perimetro())
