# Criação da classe mãe de atributos gerais dos personagens
class Character:
    def __init__(self, name, category, level, hp, attack, defense):
        self.name = name
        self.category = category
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense

# Método para mostrar os atributos em comum do personagem
    def status(self):
        print(f'Nome: {self.name}')
        print(f'Classe: {self.category}')
        print(f'Nível: {self.level}')
        print(f'Vida: {self.hp}')
        print(f'Ataque: {self.attack}')
        print(f'Defesa: {self.defense}')

# Criação da classe guerreiro com os atributos adicionais de arma e força
class Warrior(Character):
    def __init__(self, name, category, level, hp, attack, defense, weapon, strength):
        super().__init__(name, category, level, hp, attack, defense)
        self.weapon = weapon
        self.strength = strength

# Método para mostrar os atributos do personagem guerreiro com os adicionais de tipo de arma e pontos de força
    def status(self):
        super().status()
        print(f'Arma: {self.weapon}')
        print(f'Força: {self.strength}')
        print()

# Criação da classe mago com os atributos adicionais de magia e pontos de magia
class Wizard(Character):
    def __init__(self, name, category, level, hp, attack, defense, spell, magic_points):
        super().__init__(name, category, level, hp, attack, defense)
        self.spell = spell
        self.magic_points = magic_points

# Método para mostrar os atributos do personagem mago com os adicionais de magia e pontos de magia
    def status(self):
        super().status()
        print(f'Magia: {self.spell}')
        print(f'Pontos de magia: {self.magic_points}')
        print()

# Criação da classe arqueiro com os atributos adicionais de tipo de arco e pontos de destreza
class Archer(Character):
    def __init__(self, name, category, level, hp, attack, defense, bow, dexterity):
        super().__init__(name, category, level, hp, attack, defense)
        self.bow = bow
        self.dexterity = dexterity

# Método para mostrar os atributos do personagem arqueiro com os adicionais de tipo de arco e pontos de destreza 
    def status(self):
        super().status()
        print(f'Arco: {self.bow}')
        print(f'Destreza: {self.dexterity}')
        print()

warrior = Warrior('Skrull', 'guerreiro', 12, 80, 120, 50, 'espada', 120)
wizard = Wizard('Gandalfo', 'mago', 5, 40, 20, 10, 'bola de fogo', 80)
archer = Archer('Arya', 'arqueiro', 6, 60, 50, 50, 'arco longo', 120)
warrior.status()
wizard.status()
archer.status()
