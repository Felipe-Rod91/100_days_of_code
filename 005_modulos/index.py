# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() 
# e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar 
# os números como um valor monetário formatado.

# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida 
# no desafio anterior.

# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre 
# na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma 
# função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação 
# de dados para aceitar apenas valores que seja monetários.

from Utilidades import moeda, dado

price = dado.leia_dinheiro('Digite um valor: R$')
moeda.resumo(price, 20, 10)
