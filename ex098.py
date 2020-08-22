def contador(x, y, z):
    print(f'CONTAGEM DE {x} ATÉ {y} DE {z} EM {z}: ')
    for i in range(x, y + 1, z):
        print(i, end=' ')
    print()


contador(1, 10, 1)
contador(10, 0, -2)

a = int(input('VALOR INICIAL: '))
b = int(input('VALOR FINAL: '))
c = int(input('PASSO: '))
contador(a, b, c)
