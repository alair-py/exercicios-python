num = list()

for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))

maior = menor = num[0]
posmenor = posmaior = 0
for c, v in enumerate(num):
    if num[c] < menor:
        menor = num[c]
        posmenor = c

    if num[c] > maior:
        maior = num[c]
        posmaior = c

print(f'O menor valor da lista é {menor} na posição {posmenor}')
print(f'O maior valor da lista é {maior} na posição {posmaior}')

