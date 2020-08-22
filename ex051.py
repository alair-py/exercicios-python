# PROGRESSAO ARITMETICA

pri = int(input('PRIMEIRO TERMO DA PROGRESSÃO: '))
raz = int(input('RAZÃO DA PROGRESSÃO: '))

print(pri)

for c in range(1, 10, 1):
    print(pri + raz)
    pri += raz

