# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos 
# durante o campeonato. Aprimore o desafio para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento 
# de cada jogador.

jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Quantas partidas jogou? '))
print(jogador)


