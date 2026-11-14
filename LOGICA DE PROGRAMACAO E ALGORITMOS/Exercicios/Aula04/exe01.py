soma = 0
qtd = 0

for i in range (1, 101, 1):
    if i % 2 == 0:
        print(i)
        soma += i
        qtd += 1

media = soma / qtd
print(f'Média: {media}')