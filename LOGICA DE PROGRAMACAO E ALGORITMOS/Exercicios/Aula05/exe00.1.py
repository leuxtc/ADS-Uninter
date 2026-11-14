def borda(palavra):
    tam = len(palavra)

    print('+','-' * tam, '+')
    print('|', palavra, '|')
    print('+', '-' * tam, '+')

borda('Leeeeo')
borda('Olá mundo')