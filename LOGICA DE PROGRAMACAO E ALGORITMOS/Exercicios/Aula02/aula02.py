# Print e Concatenação
print('Olá ' + 'Mundo')
print('Olá','Mundo')
print('A' + '-' * 5 + 'B')

# Expressões matemáticas
# a) 2 + 3 x 3
# b) 4² ÷ 3
# c) (9² + 2) x 6 - 1

a = 2 + 3 * 3
b = (4 ** 2)/3
c = (9 ** 2 + 2) * 6 - 1

print(f'a) {a} | b) {b} | c) {c}')
print('a) %.2f | b) %.2f | c) %.2f' % (a, b, c))

# Input
num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro: '))
soma = num_1 + num_2

print(f'A soma de {num_1} + {num_2} é {soma}')