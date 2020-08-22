def leiaint(a):
    if int(a) != a:
        return 'ERRO! NÚMERO INVÁLIDO!'


num = float(input('NUMERO: '))
while leiaint(num):
    print(leiaint(num))
    num = float(input('NUMERO: '))

