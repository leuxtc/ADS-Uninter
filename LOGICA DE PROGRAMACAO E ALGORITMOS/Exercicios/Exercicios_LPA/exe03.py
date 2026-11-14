# dig = 1.10
# ico = 1
# ipb = 0.40
# fot = 0.20

print('Bem-vindo a Copiadora do Leo')
calc = 0
desconto = 0

def escolha_servico():
    while True:
        try:
            print('\nEntre com o tipo de serviço desejado')
            servico = input('DIG - Digitalização\n'
                            'ICO - Impressão Colorida\n'
                            'IPB - Impressão Preto e Branco\n'
                            'FOT - Fotocópia'
                            '\n>> ').lower()

            if servico == 'dig':
                return 1.10
            elif servico == 'ico':
                return 1
            elif servico == 'ipb':
                return 0.40
            elif servico == 'fot':
                return 0.20
            else:
                print('Por favor, digite um dos serviços acima!\n')
                continue

        except:
            print('!!!! Insira um valor válido !!!!')

def num_pagina():
    global desconto
    while True:
        try:
            paginas = int(input('\nEntre com o número de páginas: '))

            if paginas < 20:
                desconto = 0
            elif 20 <= paginas < 200:
                desconto = paginas * .15
            elif 200 <= paginas < 2000:
                desconto = paginas * .20
            elif 2000 <= paginas < 20000:
                desconto = paginas * .25

            if paginas <= 0 or paginas > 20000:
                print('Coloque um número válido de paginas.')
                continue

            paginas -= desconto
            return paginas
        except:
            print('!!!! Insira um valor válido !!!!')

def servico_extra():
    print('\nDeseja adicionar algum serviço?')
    while True:
        try:
            extra = int(input('1 - Encadernação Simples - R$ 15.00'
                              '\n2 - Encadernação Capa Dura - R$ 40.00'
                              '\n0 - Não desejo mais nada'
                              '\n>> '))

            if extra == 1:
                return 15.00
            elif extra == 2:
                return 40.00
            elif extra == 0:
                return 0
        except:
            print('!!!! Insira um valor válido !!!!')

# Programa principal

custo = escolha_servico()
qntd_paginas = num_pagina()
extras = servico_extra()

total = (custo * qntd_paginas) + extras

print(f'Total: ${total} (Serviço: ${custo} * Páginas: {qntd_paginas} + Extra: ${extras})')