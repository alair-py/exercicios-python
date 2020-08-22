maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'{c}º PESO: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f'MAIOR PESO {maior:.1f} KG')
print(f'MENOR PESO {menor:.1f} KG')
