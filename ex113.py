def leiaint(msg):
    while True:
        try:
            teste = int(input(msg))
            return teste
        except (ValueError, TypeError):
            print('ERRO! Informe um valor INTEIRO.')


def leiafloat(msg):
    while True:
        try:
            teste = float(input(msg))
            return teste
        except (ValueError, TypeError):
            print('ERRO! Informe um valor REAL.')


num = leiaint('VALOR INTEIRO: ')
print(num)

num2 = leiafloat('VALOR REAL: ')
print(num2)
