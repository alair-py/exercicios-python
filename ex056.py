soma = 0
velho = 0
menos20 = 0

for c in range(0, 4):
    nome = input('SEU NOME: ')
    idade = int(input('SUA IDADE: '))
    sexo = input('SEU SEXO: [M / F] ')

    soma += idade

    if sexo.lower() == 'm':
        if idade > velho:
            nomeMvelho = nome
            velho = idade

    if sexo.lower() == 'f':
        if idade < 20:
            menos20 += 1

    if sexo.lower() != 'm' and sexo.lower() != 'f':
        print('Opção inválida: M ou F.')

media = soma / 4

print(f'A média de idade do grupo: {media}')
print(f'O homem mais velho é: {nomeMvelho}')
print(f'Quantas mulheres menores de 20 anos: {menos20}')
