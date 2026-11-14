# • Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
# • Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
# • Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;

valor_total = 0

print('BEM-VINDO A LOJA DE GELADOS DO LEO\n')

print('-' * 20, 'CARDÁPIO', '-' * 20)
print('--------------------------------------------------')
print('---|  Tamanho  |   Cupuaçu (CP) |  Açai (AC)  |---')
print('---|     P     |    R$ 9.00     |  R$ 11.00   |---')
print('---|     M     |    R$ 14.00    |  R$ 16.00   |---')
print('---|     G     |    R$ 18.00    |  R$ 20.00   |---')

while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

    if sabor == 'CP':
        sabor = 'Cupuaçu'

        if tamanho == 'P':
            valor = 9.00
        elif tamanho == 'M':
            valor = 14.00
        elif tamanho == 'G':
            valor = 18.00
        else:
            print('Tamanho inválido. Tente novamente')
            continue

        valor_total += valor

    elif sabor == 'AC':
        sabor = 'Açai'

        if tamanho == 'P':
            valor = 11.00
        elif tamanho == 'M':
            valor = 16.00
        elif tamanho == 'G':
            valor = 20.00
        else:
            print('Tamanho inválido. Tente novamente')
            continue

        valor_total += valor
    else:
        print('Sabor inválido. Tente novamente')
        continue

    print(f'Você pediu um {sabor} no tamanho {tamanho}: R$ {valor}')

    escolha = input('\nDeseja mais alguma coisa? (S/N): ').upper()

    if escolha != 'S':
        while True:
            escolha = input('\nDeseja mais alguma coisa? (S/N): ').upper()
            print('Digite um valor válido')

            if escolha == 'S':
                break
            elif escolha == 'N':
                print(f'\nO valor total a ser pago: R$ {valor_total}')
                break

    if escolha == 'S':
        continue
    else:
        break