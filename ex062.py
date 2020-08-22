pri = int(input('Primeiro numero da PA: '))
raz = int(input('Razão da PA: '))

c = 0
total = 0
passo = 10
resp = 'S'

while resp != 'N':
    total += passo
    while c <= total:
        print(pri + raz, end=' ')
        pri += raz
        c += 1

    resp = input('MAIS? [S/N]: ').upper()

    if resp == 'S':
        passo = int(input('Quanto mais? '))
    if resp == 'N':
        print('FECHANDO...')


