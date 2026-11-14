print('Escreva uma mensagem')
print('Para sair escreva: "sair"')

while True:
    txt = input()

    if txt == 'sair':
        break
    else:
        print(txt)

print('Saindo...')