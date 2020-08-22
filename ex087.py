matriz = [[], [], []]
pares = somaTerceira = maior = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i].append(int(input(f'Valor na posição [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
        if j == 2:
            somaTerceira += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]


for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'[ {matriz[i][j]} ]', end='')
    print('')

print(f'A soma de todos pares digitados: {pares}')
print(f'A soma dos valores da terceira coluna: {somaTerceira}')
print(f'Maior valor da segunda linha: {maior}')
