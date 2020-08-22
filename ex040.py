n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média {media} pts. REPROVADO! Estude mais.')
elif 5 <= media <= 6.9:
    print(f'Sua média {media} pts. RECUPERAÇÃO!')
else:
    print(f'Sua média {media} pts. APROVADO! PARABÉNS!')

