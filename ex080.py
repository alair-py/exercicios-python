num = list()

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > num[-1]:
        num.append(valor)
    else:
        pos = 0
        while pos < len(num):
            if valor <= num[pos]:
                num.insert(pos, valor)
                break
            pos += 1


print(num)
