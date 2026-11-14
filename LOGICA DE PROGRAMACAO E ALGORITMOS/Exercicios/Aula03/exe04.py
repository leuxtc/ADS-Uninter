print('Escolha uma operação:')
print('1) (+)')
print('2) (-)')
print('3) (*)')
print('4) (/)')

escolha = int(input())

if escolha > 0 and escolha < 5:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))

    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    if escolha == 1:
        print(f'{num1} + {num2} = {add}')
    elif escolha == 2:
        print(f'{num1} - {num2} = {sub}')
    elif escolha == 3:
        print(f'{num1} * {num2} = {mult}')
    elif escolha == 4:
        print(f'{num1} / {num2} = {div}')
else:
    print('Erro! Escolha um número de 1 a 4')
