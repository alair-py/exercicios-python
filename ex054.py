from datetime import date

mais = 0
menos = 0

for c in range(0, 7):
    idade = int(input('Ano de nascimento: '))
    resp = date.today().year - idade
    if resp < 18:
        menos += 1
    elif resp >= 18:
        mais += 1

print(f'PESSOAS MENORES DE IDADE: {menos}')
print(f'PESSOAS MAIORES DE IDADE: {mais}')
