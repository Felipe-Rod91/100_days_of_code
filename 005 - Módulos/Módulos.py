# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date


def voto(year):
    old = date.today().year - year
    if old < 16:
        return f'A pessoa tem {old} anos, o voto é NEGADO.'
    elif 18 <= old < 65:
        return f'A pessoa tem {old} anos, o voto é OBRIGATÓRIO.'
    else:
        return f'A pessoa tem {old} anos, o voto é OPCIONAL.'


print(voto(1960))