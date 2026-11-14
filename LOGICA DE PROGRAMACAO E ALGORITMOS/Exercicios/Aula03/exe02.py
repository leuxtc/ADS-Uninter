idade = 62
dano = 11
escudo = 10

norte = False
sul = False
leste = True
oeste = False

if idade > 60:
    print('Você tem direito aos benefícios!')

if dano > 10 and escudo - dano <= 0:
    print('Você está morto!')

if norte or sul or leste or oeste:
    print('Você escapou!')
