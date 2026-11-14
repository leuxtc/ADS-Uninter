def colecao(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt+')
        print(a.read())
    except:
        print('Erro ao abrir o arquivo...')
    finally:
        a.close()

def cadastrar(nomeArquivo, nome_jogo, nome_console):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro!')
    else:
        a.write(f'| Jogo: {nome_jogo} |\n| Console: {nome_console} |\n')
    finally:
        a.close()

def limparColecao(nomeArquivo, decisao):
    if decisao == 's' or 'S':
        try:
            a = open(nomeArquivo, 'wt')
            a.close()
        except:
            print('Erro ao limpar o arquivo. Tente novamente...')
        else:
            print(f'{nomeArquivo} foi limpo com sucesso!')
    elif decisao == 'n' or 'N':
        print('Voltando para o menu...')


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt')
        a.close()
    except:
        print('Erro ao criar um arquivo! Tente novamente...')
    else:
        print(f'{nomeArquivo} criado com sucesso!\n')

def verificarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# PROGRAMA PRINCIPAL

arquivo = 'jogos.txt'
if verificarArquivo(arquivo):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo inexistente. Criando um novo arquivo')
    criarArquivo(arquivo)

while True:
    print(f'\n----- MENU ----- \n'
          f'1 | Cadastrar um novo jogo \n'
          f'2 | Ver coleção \n'
          f'3 | Apagar Coleção \n'
          f'4 | Sair')
    opcao = int(input(f': '))

    try:
        if opcao == 1:
            print('Cadastrar selecionado...\n')

            nome_jogo = input('Nome do jogo: ')
            nome_console = input('Nome do console: ')

            cadastrar(arquivo, nome_jogo, nome_console)

        elif opcao == 2:
            print('Abrindo coleção...\n')

            colecao(arquivo)

        elif opcao == 3:
            print('Tem certeza que deseja limpar sua coleção?')
            apagar = input('(s/n): ')

            limparColecao(arquivo, apagar)

        elif opcao == 4:
            print('Saindo...')
            break

        else:
            print('Escolha uma das opções acima!')

    except ValueError:
        print('Digite um valor válido!')
    except:
        print('Ops! Houve um erro. Tente novamente...')