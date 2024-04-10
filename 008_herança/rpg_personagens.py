class Character:
    def __init__(self, name, category, level, hp, attack, defense):
        self.name = name
        self.category = category
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def show_status(self):
        print(f'Nome: {self.name}')
        print(f'Classe: {self.category}')
        print(f'Nível: {self.level}')
        print(f'Vida: {self.hp}')
        print(f'Ataque: {self.attack}')
        print(f'Defesa: {self.defense}')


class Warrior(Character):
    def __init__(self, name, category, level, hp, attack, defense, strength, weapon):
        super().__init__(name, category, level, hp, attack, defense)
        self.strength = strength
        self.weapon = weapon
    
    def show_status(self):
        super().show_status()
        print(f'Força: {self.strength}')
        print(f'Arma: {self.weapon}')
        print()


class Wizard(Character):
    def __init__(self, name, category, level, hp, attack, defense, intelligence, spell):
        super().__init__(name, category, level, hp, attack, defense)
        self.intelligence = intelligence
        self.spell = spell
    
    def show_status(self):
        super().show_status()
        print(f'Inteligência: {self.intelligence}')
        print(f'Feitiço: {self.spell}')
        print()


class Archer(Character):
    def __init__(self, name, category, level, hp, attack, defense, dexterity, bow):
        super().__init__(name, category, level, hp, attack, defense)
        self.dexterity = dexterity
        self.bow = bow
    
    def show_status(self):
        super().show_status()
        print(f'Destreza: {self.dexterity}')
        print(f'Arco: {self.bow}')
        print()


warrior = Warrior('Skrull', 'guerreiro', 7, 120, 120, 80, 150, 'espada longa')
wizard = Wizard('Gandalfo', 'mago', 8, 40, 20, 20, 150, 'bola de fogo')
archer = Archer('Legolos', 'arqueiro', 5, 100, 100, 80, 140, 'arco longo')
warrior.show_status()
wizard.show_status()
archer.show_status()