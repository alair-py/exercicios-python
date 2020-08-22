from datetime import date

nasc = int(input('Seu ano de nascimento: '))

idade = date.today().year - nasc

if idade == 18:
    print(f'''Você tem {idade} anos.
    Apresente-se ao alistamento.''')
elif idade < 18:
    print(f'''Você tem {idade} anos.
    Ainda faltam {18 - idade} anos para se alistar.''')
else:
    print(f'''Você tem {idade} anos.
    Está há {idade - 18} anos atrasado para o alistamento.''')
