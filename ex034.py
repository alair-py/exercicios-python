sal = float(input('Seu salário: '))

if sal >= 1250:
    total = sal + sal * 0.10
    print(f'Seu novo salário com 10% de aumento: R$ {total:.2f}')
else:
    total = sal + sal * 0.15
    print(f'Seu salário com 15% de aumento: R$ {total:.2f}')
