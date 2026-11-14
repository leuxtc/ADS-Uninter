def validar_string(str, min, max):
    texto = input(str)
    tam = len(texto)

    while tam < min or tam > max:
        texto = input(str)
        tam = len(texto)

    return texto

x = validar_string('Digite uma palavra: ', 10, 30)
print(f'"{x}" | Dado válido. Encerrando programa...')