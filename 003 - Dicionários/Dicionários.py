# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos 
# durante o campeonato. Aprimore o desafio para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento 
# de cada jogador.

# Criação da lista com todos os jogadores e dos dicionários com nome, número de partidas e gols de cada um
players = list()
player = dict()

# Sistema com os dados de cada jogador
while True:
    player['name'] = input('Nome do jogador(a): ')
    player['matches'] = int(input('Quantas partidas jogou? '))
    player['goals'] = list()
    for match in range(player['matches']):
        goals = int(input(f'Quantos gols marcou na {match+1}ª partida? '))
        player['goals'].append(goals)
        player['total_goals'] = sum(player['goals'])
    players.append(player.copy())
    player.clear()

# Loop perguntando ao usuário se deseja continuar com mais cadastros ou se deseja encerrar o programa e mostrar os resultados
    while True:
        print('-=' * 15)
        cont = str(input('Deseja continuar?[S/N] ')).upper()
        print('-=' * 15)
        if cont == 'S' or cont == 'N':
            break
        else:
            print('VALOR INVÁLIDO! DIGITE "S" ou "N".')
    if cont == 'N':
        break

# Visualização de todos os jogadores e seus desempenhos na temporada
for p in players:
    for keys, values in p.items():
        print(f'{keys}: {values}')
    print()
