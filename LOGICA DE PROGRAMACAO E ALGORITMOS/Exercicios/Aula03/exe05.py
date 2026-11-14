qntd_kwh = int(input('Insira a quantidade de kWh consumida: '))

print('Insira o tipo de instalação:')
print('Residência = R')
print('Indústrias = I')
print('Comércios  = C')

tipo_inst = input()

if tipo_inst == 'R' or 'r':
    if qntd_kwh < 500:
        res = qntd_kwh * 0.40
    else:
        res = qntd_kwh * 0.65

    print(f'Preço: R${res}')

elif tipo_inst == 'I' or 'i' or tipo_inst == 'C' or 'c':
    if qntd_kwh < 1000:
        res = qntd_kwh * 0.55
    else:
        res = qntd_kwh * 0.60

    print(f'Preço: R${res}')
