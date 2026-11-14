import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while min > x < max:
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global v1, v2, empate

    if jogador1 == 1: #PEDRA
        if jogador2 == 1: #PEDRA
            empate += 1
        elif jogador2 == 2: #PAPEL
            v2 += 1
        elif jogador2 == 3: #TESOURA
            v1 += 1

    if jogador1 == 2: #PAPEL
        if jogador2 == 1: #PEDRA
            v1 += 1
        elif jogador2 == 2: #PAPEL
            empate += 1
        elif jogador2 == 3: #TESOURA
            v2 += 1

    if jogador1 == 3: #TESOURA
        if jogador2 == 1: #PEDRA
            v2 += 1
        elif jogador2 == 2: #PAPEL
            v1 += 1
        elif jogador2 == 3: #TESOURA
            empate += 1

    placar = [v1, v2, empate]
    return placar

#PROGRAMA PRINCIPAL
print('1 | Pedra')
print('2 | Papel')
print('3 | Tesoura')
print('---------')
print('0 | Sair')

escolhas = []
placar = []
v1 = 0
v2 = 0
empate = 0


while True:
    j1 = valida_int('Escolha uma opção: ', 0, 3)

    if not j1: # 1, 2, 3 = True; 0 = False | Se não for True: Parar
        break

    j2 = random.randint(1,3)

    escolhas.append([j1, j2])
    placar = vencedor(j1,j2)

for escolha in escolhas:
    for dados in escolha:
        if dados == 1:
            dados = 'Pedra'
        if dados == 2:
            dados = 'Papel'
        if dados == 3:
            dados = 'Tesoura'

        print(dados, end=' x ')
    print()

print(f'Vitórias do JOGADOR_1: {placar[0]}')
print(f'Vitórias do JOGADOR_2: {placar[1]}')
print(f'EMPATES: {placar[2]}')