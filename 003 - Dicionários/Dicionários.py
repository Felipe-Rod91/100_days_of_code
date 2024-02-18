# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos 
# durante o campeonato. Aprimore o desafio para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do 
# aproveitamento de cada jogador.

import time

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
        print('-=' * 20)
        cont = str(input('Deseja continuar?[S/N] ')).upper()
        print('-=' * 20)
        if cont == 'S' or cont == 'N':
            break
        else:
            print('VALOR INVÁLIDO! DIGITE "S" ou "N".')
    if cont == 'N':
        break

# Visualização geral de todos os jogadores e seus totais de gols
while True:
    while True:
        print(f'{"Nº":<4} {"JOGADOR":<14} {"GOLS":<2}')
        print('-' * 40)
        for i, p in enumerate(players):
            print(f'{i+1:<4} {p['name']:<14} {p['total_goals']:<2}')
        print('-' * 40)

# Sistema de visualização detalhada de jogadores ou encerramento do programa
        option = int(input('Digite o número do jogador(a) que deseja visualizar (digite 999 para sair do programa): '))
        if option == 999:
            break
        if option > len(players):
            print('OPÇÃO INVÁLIDA! DIGITE O NÚMERO DE UM DOS JOGADORES.')
        else:
            print('-' * 40)
            print(f'{players[option-1]['name']} fez {players[option-1]['total_goals']} gols durante {players[option-1]['matches']} jogos:')
            for n, match in enumerate(players[option-1]['goals']):
                print(f'    => Na {n+1}ª partida ele(a) fez {match} gols.')
                time.sleep(0.5)
            print('-' * 40)
    break

# Finalização do programa
print('-' * 27)
print('PROGRAMA ENCERRADO')
print('-' * 27)
