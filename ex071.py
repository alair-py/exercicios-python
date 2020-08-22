print('=' * 30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('=' * 30)

saque = int(input('VALOR DO SAQUE: R$ '))
total = saque

nota = 200
totalN = 0
if saque % 2 == 0:
    while True:
        if total >= nota:
            total -= nota
            totalN += 1
        else:
            if totalN > 0:
                print(f'{totalN} notas de R$ {nota}')
                totalN = 0

            if nota == 200:
                nota = 100

            elif nota == 100:
                nota = 50

            elif nota == 50:
                nota = 20

            elif nota == 20:
                nota = 10

            elif nota == 10:
                nota = 5

            elif nota == 5:
                nota = 2

            if total == 0:
                break
else:
    print('Valor inválido! somentes valores pares!')
