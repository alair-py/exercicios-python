from datetime import date

nasc = int(input('ANO DE NASCIMENTO: '))

idade = date.today().year - nasc

if idade < 9:
    print(f'{idade} anos. CATEGORIA: MIRIM.')
elif idade < 14:
    print(f'{idade} anos. CATEGORIA: INFANTIL.')
elif idade < 19:
    print(f'{idade} anos. CATEGORIA: JUNIOR.')
elif idade < 20:
    print(f'{idade} anos. CATEGORIA: SÊNIOR.')
else:
    print(f'{idade} anos. CATEGORIA: MASTER')
