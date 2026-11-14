def omelete():
    global ovos  # Transforma a variável 'ovos' em global
    ovos = 12    # Sobrescreve o 'ovos = 6'
    print(ovos)

ovos = 6
omelete()