maisMil = total = menor = c = 0
prodMenor = ''

while True:
    prod = str(input('PRODUTO: ')).upper().strip()
    preco = float(input('PREÇO: R$ '))
    if c == 0:
        menor = preco
        c += 1

    total += preco

    if preco > 1000:
        maisMil += 1

    if preco < menor:
        menor = preco
        prodMenor = prod

    resp =''
    while resp not in 'SN':
        resp = input('CONTINUAR: [S/N] ').upper()[0].strip()

    if resp == 'N':
        break

print(f'TOTAL GASTO: R$ {total:.2f}')
print(f'QUANTIDADE ACIMA DE R$ 1.000: {maisMil:.2f}')
print(f'PRODUTO MAIS BARATO: {prodMenor} R$ {menor:.2f}')
