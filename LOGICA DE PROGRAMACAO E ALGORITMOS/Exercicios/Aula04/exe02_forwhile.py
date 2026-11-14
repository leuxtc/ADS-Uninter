valor = 1

while valor <= 10:
    print(f'TABUADA DO {valor}')

    for i in range(1, 11, 1):
        print(f'{valor} x {i} = {valor * i}')
    valor += 1