class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_product(self):
        print(f'Nome: {self.name}')
        print(f'Preço: {self.price}')
        print(f'Quantidade: {self.quantity}')
        print()

    def update_price(self, new_price):
        self.price = new_price
        print(f'O novo preço de {self.name} é de R${new_price}.')
        print()

    def add_product(self, add):
        self.quantity += add
        print(f'Adicionando {add} ao estoque. Total: {self.quantity}.')
        print()

    def remove_product(self, remove):
        self.quantity -= remove
        print(f'Removendo {remove} do estoque. Total: {self.quantity}')
        print()


iphone = Product('iPhone', 5600, 10)
xiaomi = Product('Xiaomi', 3200, 6)

iphone.show_product()
iphone.update_price(5900)
iphone.add_product(4)
iphone.remove_product(9)
iphone.show_product()

xiaomi.show_product()
xiaomi.update_price(2900)
xiaomi.remove_product(6)
xiaomi.show_product()