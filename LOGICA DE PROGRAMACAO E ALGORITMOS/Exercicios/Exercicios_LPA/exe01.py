# Se valor_total for menor que 2500 o desconto será de 0%;
# • Se valor_total for maior ou igual que 2500 e menor que 6000 o desconto será de
# 4%;
# • Se valor_total for maior ou igual que 6000 e menor que 10000 o desconto será
# de 7%;
# • Se valor_total for maior ou igual que 10000 o desconto será de 11%;

print('BEM-VINDO A LOJA DO LEO\n')
val_unit = int(input('Entre com o valor do produto: '))
qntd = int(input('Entre com a quantidade do produto: '))

valor_total = qntd * val_unit

if valor_total >= 2500 and valor_total < 6000:
    desconto = valor_total * .04
elif valor_total >= 6000 and valor_total < 10000:
    desconto = valor_total * .07
elif valor_total >= 10000:
    desconto = valor_total * .11
else:
    desconto = 0

print(f'Valor SEM desconto: R$ {valor_total}')
print(f'Valor COM desconto: R$ {valor_total - desconto}')
