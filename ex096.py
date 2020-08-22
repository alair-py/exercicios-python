def lin():
    print('-' * 30)
    print(f'{"MEDIDOR DE ÁREA":^30}')
    print('-' * 30)


def area(a, b):
    print(f'ÁREA TOTAL: {a * b} M².')


lin()
c = int(input('QUAL COMPRIMENTO: '))
l = int(input('QUAL LARGURA: '))

area(c, l)

