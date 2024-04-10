# Classe pai de formas geométricas com uma função vazia
class Forma:
    def area(self):
        pass
    
# Classe filha de forma para definir um quadrado e um método para calcular sua área
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

# Classe filha de forma para definir um círculo e um método para calcular sua área
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2

# dois objetos quadrados, cada um usando o método da classe Quadrado para calcular sua área
quadrado1 = Quadrado(5)
area_quadrado1 = quadrado1.area()
print(area_quadrado1)

quadrado2 = Quadrado(7)
area_quadrado2 = quadrado2.area()
print(area_quadrado2)

# dois objetos circulares, cada um usando o método da classe Círculo para calcular a área
circulo1 = Circulo(5)
area_circulo1 = circulo1.area()
print(area_circulo1)

circulo2 = Circulo(9)
area_circulo2 = circulo2.area()
print(area_circulo2)