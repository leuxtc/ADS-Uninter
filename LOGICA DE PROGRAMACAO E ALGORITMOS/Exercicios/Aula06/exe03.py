ficha = {}
pessoa = []

while True:
    ficha['nome'] = input('Nome: ')
    ficha['ano_nasc'] = int(input('Ano de nascimento: '))
    ficha['sexo'] = input('Sexo: ')

    pessoa.append(ficha)
    print(pessoa)