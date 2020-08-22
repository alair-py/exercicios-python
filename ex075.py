
num = (
       int(input('Digite o 1 valor: ')),
       int(input('Digite o 2 valor: ')),
       int(input('Digite o 3 valor: ')),
       int(input('Digite o 4 valor: '))
       )

print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro 3 aparece na posição {num.index(3)}')
else:
    print(f'O numero 3 não foi digitado.')

for c in range(0, 4):
    if num[c] % 2 == 0:
        print(f'Números pares digitados: {num[c]}')
