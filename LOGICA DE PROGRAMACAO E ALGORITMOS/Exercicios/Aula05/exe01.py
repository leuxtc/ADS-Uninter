def calc_fatorial(num):
    """
    Calcula o fatorial de um número

    :param num:
    :return:
    """

    for i in range(num - 1, 0, -1):
        res = num * i
        num = res

    print(f'{num}! = {validar(num)}')

def validar(x):
    """
    Verifica se o número é positivo. Caso não seja, retorna um 'Erro'

    :param x:
    :return:
    """

    if x == 0:
        x = 1
        return x
    if x < 0:
        return 'Erro'
    else:
        return x


calc_fatorial(4)
calc_fatorial(0)
calc_fatorial(-3)
help(calc_fatorial)
help(validar)