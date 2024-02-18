# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos 
# durante o campeonato. Aprimore o desafio para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento 
# de cada jogador.

# Criação do dicionário com nome do jogador, partidas e gols
jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Quantas partidas jogou? '))
jogador['gols'] = list()

# Sistema que define, pelo número de partidas, quantos gols marcou em cada e o total da temporada, colocando cada número dentro de uma lista dentro do dicionário 
# do jogador
for partida in range(jogador['partidas']):
    gol = int(input(f'Quantos gols marcou na {partida+1}ª partida? '))
    jogador['gols'].append(gol)
    jogador['total_gols'] = sum(jogador['gols'])

# Resultado formatado do nome, número de partidas, quantidade de gols em cada partida e o total da temporada
print('-=' * 20)
print(f'O nome do jogador é {jogador["nome"]} e ele jogou {jogador["partidas"]} partidas:')
for keys, values in enumerate(jogador['gols']):
    print(f'    => Na partida {keys+1} ele fez {values} gols.')
print(f'No total, {jogador["nome"]} fez {jogador["total_gols"]} gols.')
