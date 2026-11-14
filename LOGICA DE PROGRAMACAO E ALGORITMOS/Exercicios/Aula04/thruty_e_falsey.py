nome = '' # FALSE

while not nome: # TRUE
    nome = input('Digite seu nome: ')

valor = int(input('Digite um valor: '))
if valor: # SE VALOR FOR MAIOR QUE 0
    print(f'Você digitou {valor}')
else:
    print(f'{valor}')