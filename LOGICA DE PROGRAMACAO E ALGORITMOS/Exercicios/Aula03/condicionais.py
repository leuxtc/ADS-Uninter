x = int(input('Digite um número: '))
y = int(input('Digite outro: '))

if x > y:
    print(f'{x} é maior que {y}')
if x < y:
    print(f'{y} é maior que {x}')
else:
    print(f'Os dois números são iguais')

if x % 2 == 0:
    print(f'{x} é par')
else:
    print(f'{x} é ímpar')