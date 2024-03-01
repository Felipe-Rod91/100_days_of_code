# Escreva uma classe chamada ContaBancaria que representa uma conta bancária. Esta classe deve incluir métodos 
# para depositar dinheiro na conta, sacar dinheiro da conta e verificar o saldo atual da conta. Certifique-se de que
# a classe tenha um atributo para armazenar o saldo atual da conta.

# Depois de criar a classe ContaBancaria, crie alguns objetos dessa classe e teste os métodos para depositar,
# sacar e verificar o saldo da conta. Experimente diferentes valores de depósito e saque para garantir que
# os métodos funcionem corretamente.

class ContaBancaria:
    def __init__(self, saldo_atual=0):
        self.saldo_atual = saldo_atual
    
# Função que retorna a quantia do depósito e o saldo atual.
    def depositar(self, deposito=0):
        self.deposito = deposito
        self.saldo_atual += self.deposito
        return f'Fez um depósito de R${self.deposito:.2f} na conta, ficando com R${self.saldo_atual:.2f} no total.'
    
# Método que retorna a quantia de saque e o saldo atual.
    def sacar(self, saque=0):
        self.saque = saque
        self.saldo_atual -= self.saque
        return f'Fez um saque de R${self.saque:.2f}, ficando com R${self.saldo_atual:.2f} no total.'
    
# Método que retorna o saldo atual formatado.
    def saldo(self):
        return f'R${self.saldo_atual:.2f}'

# Movimentação financeira do cliente.
cliente_1 = ContaBancaria(35400)
print(f'Cliente começa o mês com {cliente_1.saldo()}.')
print(cliente_1.depositar(4500))
print(cliente_1.sacar(18500))
print(f'Saldo atual: {cliente_1.saldo()}')
