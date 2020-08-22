n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor valor foi: {menor}')
print(f'O maior valor foi: {maior}')





