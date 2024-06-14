class character:
    def __init__(self, name, category, health, magic, stamina, strength, intelligence, faith):
        self.name = name
        self.category = category
        self.health = health
        self.magic = magic
        self.stamina = stamina
        self.strength = strength
        self.intelligence = intelligence
        self.faith = faith
    
    
    def show_status(self):
        print(f'Name: {self.name}')
        print(f'Class:  {self.category}')
        print(f'Health: {self.health}')
        print(f'Magic: {self.magic}')
        print(f'Stamina: {self.stamina}')
        print(f'Strength: {self.strength}')
        print(f'Intelligence: {self.intelligence}')
        print(f'Faith: {self.faith}')


warrior = character('Krum', 'warrior', 10, 0, 10, 12, 2, 6)
warrior.show_status()
