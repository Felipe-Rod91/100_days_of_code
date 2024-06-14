# Escreva uma classe chamada ContaBancaria que representa uma conta bancária. Esta classe deve incluir métodos 
# para depositar dinheiro na conta, sacar dinheiro da conta e verificar o saldo atual da conta. Certifique-se de que
# a classe tenha um atributo para armazenar o saldo atual da conta.

# Depois de criar a classe ContaBancaria, crie alguns objetos dessa classe e teste os métodos para depositar,
# sacar e verificar o saldo da conta. Experimente diferentes valores de depósito e saque para garantir que
# os métodos funcionem corretamente.

class ContaBancaria:
    def __init__(self, saldo_atual=0, nome=''):
        self.saldo_atual = saldo_atual
        self.nome = nome
    
# Função que retorna a quantia do depósito e o saldo atual.
    def depositar(self, deposito=0):
        self.deposito = deposito
        self.saldo_atual += self.deposito
        return f'{self.nome} fez um depósito de R${self.deposito:.2f}, seu saldo é R${self.saldo_atual:.2f}.'
    
# Método que retorna a quantia de saque e o saldo atual.
    def sacar(self, saque=0):
        self.saque = saque
        self.saldo_atual -= self.saque
        return f'{self.nome} fez um saque de R${self.saque:.2f}, seu saldo é R${self.saldo_atual:.2f}.'
    
# Método que retorna o saldo atual formatado.
    def saldo(self):
        return f'Saldo de {self.nome}: R${self.saldo_atual:.2f}'

# Movimentação financeira do cliente.
adilson = ContaBancaria(35400, 'Adilson')
print(adilson.saldo())
print(adilson.depositar(4500))
print(adilson.sacar(18500))
print(adilson.saldo())
felipe = ContaBancaria(354, 'Felipe')
print(felipe.saldo())
print(felipe.depositar(564))
print(felipe.sacar(12))
print(felipe.saldo())
