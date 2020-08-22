# SOMAR INTEIROS PARES

s = 0
for c in range(0, 6):
    num = int(input('UM NUMERO INTEIRO: '))
    if num % 2 == 0:
        s += num

print(f'A SOMA DOS PARES DIGITADOS FOI {s}')
