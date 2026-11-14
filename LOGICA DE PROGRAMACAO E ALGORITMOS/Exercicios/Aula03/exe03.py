A = int(input('Digite o 1o lado do triângulo: '))
B = int(input('Digite o 2o lado do triângulo: '))
C = int(input('Digite o 3o lado do triângulo: '))

if A == 0 or B == 0 or C == 0:
    print('Não pode haver lados igual a zero!')
elif A > B + C or B > A + C or C > A + B:
    print('Erro!')
else:
    if A == B == C:
        print('Triângulo Equilátero')
    elif A == B or B == C or A == C:
        print('Triângulo Isósceles')
    elif A != B != C:
        print('Triângulo Escaleno')