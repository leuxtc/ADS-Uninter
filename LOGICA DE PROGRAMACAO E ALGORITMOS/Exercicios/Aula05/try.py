def div():
    while True:
        try:
            num1 = int(input('Digite um valor: '))
            num2 = int(input('Digite outro valor: '))
            calc = num1 / num2
        except ValueError:
            print('Insira um valor válido! Tente novamente...')
        except ZeroDivisionError:
            print('Erro! Divisão por zero. Tente novamente...')
        except: # TRATAÇÂO GENÉRICA DE ERROS
            print('Ops! Algo aconteceu. Tente novamente...')
        else:
            return print(calc)
        finally:
            print('Dados enviados')

div()