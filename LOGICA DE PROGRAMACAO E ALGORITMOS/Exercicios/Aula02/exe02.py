# EXE 02
preco = int(input('Digite o preco do produto: R$'))
percentual = float(input('Digite o percentual de desconto (0-100%): '))
desconto = preco * (percentual/100)
final = preco - desconto

print(f'O preço do produto é R${preco} | Desconto de {percentual}% | '
      f'Valor calculado de desconto: {desconto} | Valor final: R${final}')