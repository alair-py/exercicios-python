num2 = [[], [], [], []]

for i in range(0, 4):
    for j in range(0, 4):
        num2[i].append(int(input(f'Valor na posição [{i}, {j}]: ')))


for i in range(len(num2)):
    for j in range(len(num2)):
        print(f'[ {num2[i][j]} ]', end=' ')
    print('')

