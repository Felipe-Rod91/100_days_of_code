# Classe Client para definir nome, email e plano de assinatura do usuário.
class Client:
    def __init__(self, name, email, subscription=None):
        self.name = name
        self.email = email
        self.avaliable_subscription_plans = [None, 'Basic', 'Premium']
        if subscription in self.avaliable_subscription_plans:
            self.subscription = subscription
        else:
            raise Exception('Plano inválido')
    
# Método para mudar o plano de assinatura.
    def change_subscription_plan(self, new_subscription_plan):
        if new_subscription_plan in self.avaliable_subscription_plans:
            print(f'Plano alterado com sucesso para "{new_subscription_plan}".')
            self.subscription = new_subscription_plan
    
# Método para cancelar a assinatura.
    def cancel_subscription(self):
        print('Plano cancelado com sucesso.')
        self.subscription = None
    
# Método para visualizar os dados da assinatura e o plano atual.
    def check_current_subscription_plan(self):
        print(f'Nome: {self.name}, e-mail: {self.email}, '
              f'Plano atual: {self.subscription}')
    
# Método para assistir filmes e verificar se o plano de assinatura atual permite.
    def watch_movie(self, movie, required_subscription_plan):
        if self.subscription == None:
            print(f'Você precisa de uma assinatura "{required_subscription_plan}" para assistir {movie}.')
        elif self.subscription == required_subscription_plan:
            print(f'Assistir filme {movie}.')
        elif self.subscription == 'Premium':
            print(f'Assistir filme {movie}')
        elif self.subscription == 'Basic' and required_subscription_plan == 'Premium':
            print(f'Faça um upgrade da sua assinatura para "Premium" para poder assistir {movie}.')
        else:
            print(f'Plano inválido!')

# Instância 'adilson' e seus métodos dentro da classe Client.
adilson = Client('Adilson', 'adilson@mail.com')
adilson.check_current_subscription_plan()
adilson.watch_movie('Star Wars', 'Premium')
adilson.change_subscription_plan('Premium')
adilson.check_current_subscription_plan()
adilson.watch_movie('Star Wars', 'Premium')
adilson.change_subscription_plan('Basic')
adilson.check_current_subscription_plan()
adilson.watch_movie('Star Wars', 'Premium')
adilson.cancel_subscription()
adilson.check_current_subscription_plan()
adilson.watch_movie('Star Wars', 'Premium')
print()

# Instância 'helena' e seus métodos dentro da classe Client.
helena = Client('Helena', 'helena@mail.com')
helena.check_current_subscription_plan()
helena.watch_movie('Transformers', 'Basic')
helena.change_subscription_plan('Premium')
helena.check_current_subscription_plan()
helena.watch_movie('Transformers', 'Basic')
helena.change_subscription_plan('Basic')
helena.check_current_subscription_plan()
helena.watch_movie('Transformers', 'Basic')
helena.cancel_subscription()
helena.check_current_subscription_plan()
helena.watch_movie('Transformers', 'Basic')
