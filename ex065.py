resp = 'S'
maior = menor = soma = 0
cont = -1

while resp == 'S':
    num = int(input('Digite um numero: '))
    while cont == -1:
        maior = num
        menor = num
        cont = 0

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    soma += num
    cont += 1

    resp = str(input('Deseja continuar? [S/N]: ')).upper()

media = soma / cont

print(f'A média dos valores foi {media}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
