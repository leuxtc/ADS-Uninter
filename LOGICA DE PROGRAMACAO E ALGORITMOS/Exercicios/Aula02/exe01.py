# EXE 01
dias = int(input('Quantos dias? '))
horas = int(input('Quantas horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos? '))
total_segundos = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print(f'O total de segundos calculado é de {total_segundos}')
