prod = ('Banana', 2, 'Tomate', 3, 'Frango', 9, 'Batata', 4, 'Peixe', 7)

print('-' * 35)
print(f'{"LISTA DE PREÇO":^35}')
print('-' * 35)


for c in range(len(prod)):
    if c % 2 == 0:
        print(f'{prod[c]:.<30}', end='')
    else:
        print(f'R${prod[c]:>6.2f}')