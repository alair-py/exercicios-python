from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(num)

menor = maior = num[0]
for c in range(0, 5):
    if num[c] < menor:
        menor = num[c]
    if num[c] > maior:
        maior = num[c]

print(f'Maior valor gerado: {maior}')
print(f'Menor valor gerado: {menor}')
