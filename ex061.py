pri = int(input('Primeiro número: '))
raz = int(input('Razão da progressão: '))
c = 1

print(pri)
while c <= 10:
    print(pri + raz)
    pri += raz
    c += 1
