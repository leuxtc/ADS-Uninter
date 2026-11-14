notas = [9,7,7,10,3,9,6,6,2]

print('Original: ', notas)
print('Total de notas 7:', notas.count(7))

notas.remove(2)
notas.append(4)
print('(1) Trocar o ultimo valor por 4: ', notas)

notas[-1] = 4
print('(2) Trocar o ultimo valor por 4: ', notas)

notas.sort()
print('(1) Pegar o maior valor: ', notas[-1])

print('(2) Pegar o maior valor: ', max(notas))

print('Lista ordenada: ', notas)

soma = 0

for indice in notas:
    soma += indice
    media = soma / len(notas)

print('(1) Média dos valores', media)

media2 = sum(notas) / len(notas)

print('(2) Média dos valores', media2)