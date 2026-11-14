game = {}
games = []

for i in range(3):
    game['nome'] = input('Nome do jogo: ')
    game['console'] = input('Nome do console: ')
    game['ano'] = input('Ano de lançamento: ')

    games.append(game.copy())

for jogos in games:
    for chaves, valor in jogos.items():
        print(f'{chaves} : {valor}')